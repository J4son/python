#!/usr/bin/python
import MySQLdb,logging,suds,suds.xsd.doctor,sys,string
cache = suds.cache.ObjectCache(location="/tmp",months=24)# je stocke le cache pendant 24 mois
logging.basicConfig(level=logging.INFO) 
doctor = suds.xsd.doctor  #mise en oeuvre due l'inspection du WSDL
imp = suds.xsd.doctor.Import('http://schemas.xmlsoap.org/soap/encoding/') 
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/soap/')
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://www.w3.org/2001/XMLSchema')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/ControlCenterServices/')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/LogCollection/')
doctor =  suds.xsd.doctor.ImportDoctor(imp)

#-------------------------------------------------------------------------------
#je recupere les parametres de la ligne de commande
#-------------------------------------------------------------------------------

if(len(sys.argv) < 2):
	print "usage : [todo]"
	sys.exit(-2)
IP = sys.argv[1]
Classe = sys.argv[2]



#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#je me connecte au CallManager (suds.client ...) et je me connecte a la DB cacti (db_connect ...)
#-------------------------------------------------------------------------------
url_perfmon = 'https://' + IP + ':8443/perfmonservice/services/PerfmonPort?wsdl'
Perfmon_Service = suds.client.Client(url_perfmon,username='brurauc',password='00000',doctor=doctor)
resultat = Perfmon_Service.service.PerfmonCollectCounterData(IP,Classe)
try:
    db_connect = MySQLdb.connect (user="root",
			          passwd="disraeli",
			          host ="127.0.0.1",
                                  db="cacti")
except MySQLdb.Error, e:
   print "error %d: %s" % (e.args[0], e.args[1])


#-------------------------------------------------------------------------------
#je cree un curseur pour effectuer les requetes sur les tables Cacti
#-------------------------------------------------------------------------------

cursor = db_connect.cursor()

#-------------------------------------------------------------------------------
#Sur la base Cacti il faut gerer les clefs primaire.
#Donc pour chaque table je gere la cle primaire et j'effectue l'insertion
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#Ensemble de tables pour le DATA_INPUT_METHODE
#-------------------------------------------------------------------------------
cursor.execute("""select max(id) from data_input;""")
data_input = cursor.fetchone()
data_input = int(data_input[0])
cursor.execute("""
INSERT INTO `data_input` (`id`, `hash`, `name`, `input_string`, `type_id`) VALUES
("""+ str(data_input + 1) +""", '','CCM_TLS_""" + Classe + """', '/usr/bin/python /usr/share/cacti/scripts/beau-script.py <host> <class>', 1);
""")

cursor.execute("""select max(data_input_field_id) from data_input_data;""")
data_input_field_id = cursor.fetchone()
data_input_field_id = int(data_input_field_id[0])
cursor.execute("""
INSERT INTO `data_input_data` (`data_input_field_id`, `data_template_data_id`, `t_value`, `value`) VALUES
("""+ str(data_input_field_id +1) + """, 1, '','""" + IP + """'),
("""+ str(data_input_field_id +2) + """, 1, '','""" + Classe + """');
""")

cursor.execute("""select id from data_input where name ="CCM_TLS_""" + Classe + """";""")
data_input_id = cursor.fetchone()
data_input_id = int(data_input_id[0])
cursor.execute("""select max(id) from data_input_fields;""")
data_input_fields = cursor.fetchone()
data_input_fields = int(data_input_fields[0])

cursor.execute("""
INSERT INTO `data_input_fields` (`id`, `hash`, `data_input_id`, `name`, `data_name`, `input_output`, `update_rra`, `sequence`, `type_code`, `regexp_match`, `allow_nulls`) VALUES
("""+str(data_input_fields +1) +""", '', """+str(data_input_id) + """, 'Name of the counter collection', 'class', 'in', '', 2, '', '', ''),
("""+ str(data_input_fields +2) +""", '', """+str(data_input_id)+ """, 'IP Adress of the CallManager', 'host', 'in', '', 1, 'hostname', '', '');
""")

for j in range(len(resultat)):
    resultat[j].Name = resultat[j].Name.replace(("\\" + IP + "\\"),"")
    resultat[j].Name = resultat[j].Name.replace(Classe,"")
    resultat[j].Name = resultat[j].Name.replace("\\","")
    resultat[j].Name = resultat[j].Name.replace(" ","")
    
    cursor.execute("""select max(id) from data_input_fields;""")
    data_input_fields = cursor.fetchone()
    data_input_fields = int(data_input_fields[0])
    cursor.execute("""
    INSERT INTO `data_input_fields` (`id`, `hash`, `data_input_id`, `name`, `data_name`, `input_output`, `update_rra`, `sequence`, 
    `type_code`, `regexp_match`, `allow_nulls`) VALUES
    (""" + str(data_input_fields + 1) + """, '',"""+ str(data_input_id) +""", '""" + resultat[j].Name + """', '""" 
    + resultat[j].Name + """', 'out', 'on', 0, '', '', '');
    """)


#INSERT INTO `data_local` (`id`, `data_template_id`, `host_id`, `snmp_query_id`, `snmp_index`) VALUES
#(1102, 286, 84, 0, '');
	
#-------------------------------------------------------------------------------
#Ensemble de tables pour le DATA_TEMPLATE
#-------------------------------------------------------------------------------	
	
cursor.execute("""select max(id) from data_template;""")
data_template_id = cursor.fetchone()
data_template_id = int(data_template_id[0])

cursor.execute("""
INSERT INTO `data_template` (`id`, `hash`, `name`) VALUES
("""+ str(data_template_id + 1) + """, '', 'CallManager_""" + Classe+ """');
""")

cursor.execute("""select max(id) from data_template_data;""")
data_template_data_id = cursor.fetchone()
data_template_data_id = int(data_template_data_id[0])

cursor.execute("""
INSERT INTO `data_template_data` (`id`, `local_data_template_data_id`, `local_data_id`, `data_template_id`, `data_input_id`, `t_name`, `name`, `name_cache`, `data_source_path`, `t_active`, `active`, `t_rrd_step`, `rrd_step`, `t_rra_id`) VALUES
("""+str(data_template_data_id +1) +""", 0, 0,"""+ str(data_template_id +1) +""", """+str(data_input_id)+""", NULL, 
'CallManager_"""+Classe+"""','CallManager_"""+Classe+"""', '<path_rra>/callmanager_cisco_callmanager.rrd', NULL, 'on', NULL, 10, 2);
""")

cursor.execute("""select max(data_template_data_id) from data_template_data_rra;""")
data_template_data_rra_id = cursor.fetchone()
data_template_data_rra_id = int(data_template_data_rra_id[0])


cursor.execute("""
INSERT INTO `data_template_data_rra` (`data_template_data_id`, `rra_id`) VALUES
("""+str(data_template_data_rra_id +1)+ """, 1),
("""+str(data_template_data_rra_id +1)+ """, 2),
("""+str(data_template_data_rra_id +1)+ """, 3),
("""+str(data_template_data_rra_id +1)+ """, 4),
("""+str(data_template_data_rra_id +1)+ """, 5);
""")

for j in range(len(resultat)):
    resultat[j].Name = resultat[j].Name.replace(("\\" + IP + "\\"),"")
    resultat[j].Name = resultat[j].Name.replace(Classe,"")
    resultat[j].Name = resultat[j].Name.replace("\\","")
    resultat[j].Name = resultat[j].Name.replace(" ","")
    cursor.execute("""select max(id) from data_template_rrd;""")
    data_template_rrd_id = cursor.fetchone()
    data_template_rrd_id = int(data_template_rrd_id[0])
    
    cursor.execute("""select id from data_input_fields where name='"""+resultat[j].Name+ """';""")
    data_input_field_id = cursor.fetchone()
    data_input_field_id = data_input_field_id[0]
    
    cursor.execute("""
    INSERT INTO `data_template_rrd` (`id`, `hash`, `local_data_template_rrd_id`, `local_data_id`, `data_template_id`, `t_rrd_maximum`, 
    `rrd_maximum`, `t_rrd_minimum`, `rrd_minimum`, `t_rrd_heartbeat`, `rrd_heartbeat`, `t_data_source_type_id`, `data_source_type_id`, 
    `t_data_source_name`, `data_source_name`, `t_data_input_field_id`, `data_input_field_id`) VALUES("""+str(data_template_rrd_id +1) +""",
    '491d2561e39a484b39231054dc2f4637', 0, 0, """ +str(data_template_id +1)+""", '', '100000000000000000', '', '0', '', 600, '', 1, '', 
    '"""+resultat[j].Name+"""', '', '"""+str(data_input_field_id)+"""');
    """)

#-------------------------------------------------------------------------------
#Ensemble des tables pour le GRAPH TEMPLATE
#-------------------------------------------------------------------------------
cursor.execute("""select max(id) from graph_templates;""")
graph_templates_id = cursor.fetchone()
graph_templates_id = int(graph_templates_id[0])

cursor.execute("""
INSERT INTO `graph_templates` (`id`, `hash`, `name`) VALUES
("""+str(graph_templates_id +1)+""", '', 'CallManager_"""+Classe+"""');
""")

cursor.execute("""select max(id) from graph_templates_graph;""")
graph_templates_graph_id = cursor.fetchone()
graph_templates_graph_id = int(graph_templates_graph_id[0])

cursor.execute("""
INSERT INTO `graph_templates_graph` (`id`, `local_graph_template_graph_id`, `local_graph_id`, `graph_template_id`, `t_image_format_id`, `image_format_id`, `t_title`, `title`, `title_cache`, `t_height`, `height`, `t_width`, `width`, `t_upper_limit`, `upper_limit`, `t_lower_limit`, `lower_limit`, `t_vertical_label`, `vertical_label`, `t_slope_mode`, `slope_mode`, `t_auto_scale`, `auto_scale`, `t_auto_scale_opts`, `auto_scale_opts`, `t_auto_scale_log`, `auto_scale_log`, `t_scale_log_units`, `scale_log_units`, `t_auto_scale_rigid`, `auto_scale_rigid`, `t_auto_padding`, `auto_padding`, `t_base_value`, `base_value`, `t_grouping`, `grouping`, `t_export`, `export`, `t_unit_value`, `unit_value`, `t_unit_exponent_value`, `unit_exponent_value`) VALUES
("""+str(graph_templates_graph_id +1)+""", 0, 0, """+str(graph_templates_id +1)+""", '', 1, '', '|host_description|-"""+Classe+"""', '', '', 120, 
'', 500, '', '100', '', '0', '', '', '', 'on', '', 'on', '', 2, '', '', '', '', '', '', '', 'on', '', 1000, '0', '', '', 'on', '', '', '', '');
""")

for j in range(len(resultat)):
    resultat[j].Name = resultat[j].Name.replace(("\\" + IP + "\\"),"")
    resultat[j].Name = resultat[j].Name.replace(Classe,"")
    resultat[j].Name = resultat[j].Name.replace("\\","")
    resultat[j].Name = resultat[j].Name.replace(" ","")
    
    cursor.execute("""select max(id) from graph_templates_item;""")
    graph_templates_item_id = cursor.fetchone()
    graph_templates_item_id = int(graph_templates_item_id[0])
    cursor.execute("""
    INSERT INTO `graph_templates_item` (`id`, `hash`, `local_graph_template_item_id`, `local_graph_id`, `graph_template_id`, `task_item_id`, 
    `color_id`, `alpha`, `graph_type_id`, `cdef_id`, `consolidation_function_id`, `text_format`, `value`, `hard_return`, `gprint_id`, 
    `sequence`) VALUES
    ("""+str(graph_templates_item_id +1)+""", '', 0, 0, """+str(graph_templates_id +1)+""", """+str(graph_templates_item_id +1)+""", 0, 'FF', 9, 0, 1, 'Average:', '', '', 1, 27),
    ("""+str(graph_templates_item_id +2)+""", '', 0, 0, """+str(graph_templates_id +1)+""", """+str(graph_templates_item_id +1)+""", 0, 'FF', 9, 0, 4, 'Current:', '', '', 4, 26),
    ("""+str(graph_templates_item_id +3)+""", '', 0, 0, """+str(graph_templates_id +1)+""", """+str(graph_templates_item_id +1)+""", 0, 'FF', 9, 0, 3, 'Maximum:', '', '', 2, 24),
    ("""+str(graph_templates_item_id +4)+""", '', 0, 0, """+str(graph_templates_id +1)+""", """+str(graph_templates_item_id +1)+""", 
    """+str(j)+""", 'CC', 7, 0, 1, '"""+resultat[j].Name +"""', '', '', 3, 1);
    """)
    

    cursor.execute("""select max(id) from graph_template_input;""")
    graph_template_input_id = cursor.fetchone()
    graph_template_input_id = int(graph_template_input_id[0])
    cursor.execute("""
    INSERT INTO `graph_template_input` (`id`, `hash`, `graph_template_id`, `name`, `description`, `column_name`) VALUES
    ("""+str(graph_template_input_id +1)+""", '', """+str(graph_templates_id +1)+""", '"""+resultat[j].Name+"""'
    , NULL, 'task_item_id');
    """)

    cursor.execute("""select max(id) from graph_templates_item;""")
    graph_templates_item_id = cursor.fetchone()
    graph_templates_item_id = int(graph_templates_item_id[0])
    cursor.execute("""select max(id) from graph_template_input;""")
    graph_template_input_id = cursor.fetchone()
    graph_template_input_id = int(graph_template_input_id[0])
    cursor.execute("""
    INSERT INTO `graph_template_input_defs` (`graph_template_input_id`, `graph_template_item_id`) VALUES
    ("""+str(graph_template_input_id)+""", """+str(graph_templates_item_id)+""");
    """)

#INSERT INTO `graph_local` (`id`, `graph_template_id`, `host_id`, `snmp_query_id`, `snmp_index`) VALUES
#(1085, 234, 84, 0, '');



#-------------------------------------------------------------------------------
#Ensemble de tables pour le GRAPH TREE
#-------------------------------------------------------------------------------
cursor.execute("""select max(id) from graph_tree_items;""")
graph_tree_items_id = cursor.fetchone()
graph_tree_items_id = int(graph_tree_items_id[0])

cursor.execute("""select max(id) from graph_tree;""")
graph_tree_id = cursor.fetchone()
graph_tree_id = int(graph_tree_id[0])

cursor.execute("""
INSERT INTO `graph_tree_items` (`id`, `graph_tree_id`, `local_graph_id`, `rra_id`, `title`, `host_id`, `order_key`, `host_grouping_type`, `sort_children_type`) VALUES
("""+str(graph_tree_items_id +1)+""", 1, 0, 0, '', 84, '001001000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 1, 1);
""")
#-------------------------------------------------------------------------------
#Ensemble de tables pour le HOST
#-------------------------------------------------------------------------------
#cursor.execute("""select max(id) from host;""")
#host_id = cursor.fetchone()
#host_id = int(host_id[0])
#cursor.execute("""select max(id) from host_template where name='CCM_V6X';""")
#host_template_id = cursor.fetchone()
#host_template_id = int(host_template_id[0])
#cursor.execute("""
#INSERT INTO `host` (`id`, `host_template_id`, `description`, `hostname`, `notes`, `snmp_community`, `snmp_version`, `snmp_username`, `snmp_password`, `snmp_auth_protocol`, `snmp_priv_passphrase`, `snmp_priv_protocol`, `snmp_context`, `snmp_port`, `snmp_timeout`, `availability_method`, `ping_method`, `ping_port`, `ping_timeout`, `ping_retries`, `max_oids`, `disabled`, `monitor`, `status`, `status_event_count`, `status_fail_date`, `status_rec_date`, `status_last_error`, `min_time`, `max_time`, `cur_time`, `avg_time`, `total_polls`, `failed_polls`, `availability`, `wmi_account`) VALUES
#("""+str(host_id +1) +""", """+str(host_template_id)+""", 'CallManager', '"""+IP+"""', '', '50guf4c3', 2, '', '', '', '', '', '', 161, 500, 2, 1, 0, 500, 2, 10, '', 'on', 3, 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', 1.12915, 556.91290, 49.48211, 55.01569, 225, 0, 100.00000, 0);
#""")

#-------------------------------------------------------------------------------
#je ferme le curseur et la connexion a la database Cacti
#-------------------------------------------------------------------------------
 
cursor.close()
db_connect.close()
