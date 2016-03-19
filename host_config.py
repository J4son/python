############################################
#   Dictionnaire Nagios:
#   pour chaque fichier il y a le dictionnaire associe
############################################



"""
define host{
host_name host_name
alias alias
display_name display_name
address address
parents host_names
hostgroups hostgroup_names
check_command command_name
initial_state [o,d,u]
max_check_attempts
check_interval
retry_interval
active_checks_enabled [0/1]
passive_checks_enabled [0/1]
check_period timeperiod_name
obsess_over_host [0/1]
check_freshness [0/1]
freshness_threshold
event_handler command_name
event_handler_enabled [0/1]
low_flap_threshold
high_flap_threshold
flap_detection_enabled [0/1]
flap_detection_options [o,d,u]
process_perf_data [0/1]
retain_status_information [0/1]
retain_nonstatus_information [0/1]
contacts contacts
contact_groups contact_groups
notification_interval
first_notification_delay
notification_period timeperiod_name
notification_options [d,u,r,f,s]
notifications_enabled [0/1]
stalking_options [o,d,u]
notes note_string
notes_url url
action_url url
icon_image image_file
icon_image_alt alt_string
vrml_image image_file
statusmap_image image_file
2d_coords x_coord,y_coord
3d_coords x_coord,y_coord,z_coord
}
"""
######################################################
"""
define hostgroup{
hostgroup_name hostgroup_name
alias alias
members hosts
hostgroup_members hostgroups
notes note_string
notes_url url
action_url url
}
"""
######################################################

"""
define service{
host_name host_name
hostgroup_name hostgroup_name
service_description service_description
display_name display_name
servicegroups servicegroup_names
is_volatile [0/1]
check_command command_name
initial_state [o,w,u,c]
max_check_attempts
check_interval
retry_interval
active_checks_enabled [0/1]
passive_checks_enabled [0/1]
check_period timeperiod_name
obsess_over_service [0/1]
check_freshness [0/1]
freshness_threshold
event_handler command_name
event_handler_enabled [0/1]
low_flap_threshold
high_flap_threshold
flap_detection_enabled [0/1]
flap_detection_options [o,w,c,u]
process_perf_data [0/1]
retain_status_information [0/1]
retain_nonstatus_information [0/1]
notification_interval
first_notification_delay
notification_period timeperiod_name
notification_options [w,u,c,r,f,s]
notifications_enabled [0/1]
contacts contacts
contact_groups contact_groups
stalking_options [o,w,u,c]
notes note_string
notes_url url
action_url url
icon_image image_file
icon_image_alt alt_string
}
"""
############################################################
"""
define servicegroup{
servicegroup_name servicegroup_name
alias alias
members services
servicegroup_members servicegroups
notes note_string
notes_url url
action_url url
}
"""
##########################################

"""
define contact{
contact_name contact_name
alias alias
contactgroups contactgroup_names
host_notifications_enabled [0/1]
service_notifications_enabled [0/1]
host_notification_period timeperiod_name
service_notification_period timeperiod_name
host_notification_options [d,u,r,f,s,n]
service_notification_options [w,u,c,r,f,s,n]
host_notification_commands command_name
service_notification_commands command_name
email email_address
pager pager_number or pager_email_gateway
addressx additional_contact_address
can_submit_commands [0/1]
retain_status_information [0/1]
retain_nonstatus_information [0/1]
}
"""
######################################################
"""
define contactgroup{
contactgroup_name contactgroup_name
alias alias
members contacts
contactgroup_members contactgroups
}
"""
######################################################

"""
define timeperiod{
timeperiod_name timeperiod_name
alias alias
[weekday] timeranges
[exception] timeranges
exclude [timeperiod1,timeperiod2,...,timeperiodn]
}
"""
####################################################

class command:
    command_name = ""
    command_line = ""
    
"""
define command{
command_name command_name
command_line command_line
}
"""
####################################################
"""
define servicedependency{
dependent_host_name host_name
dependent_hostgroup_name hostgroup_name
dependent_service_description service_description
host_name host_name
hostgroup_name hostgroup_name
service_description service_description
inherits_parent [0/1]
execution_failure_criteria [o,w,u,c,p,n]
notification_failure_criteria [o,w,u,c,p,n]
dependency_period timeperiod_name
}
"""
####################################################
"""
define serviceescalation{
host_name host_name
hostgroup_name hostgroup_name
service_description service_description
contacts contacts
contact_groups contactgroup_name
first_notification
last_notification
notification_interval
escalation_period timeperiod_name
escalation_options [w,u,c,r]
}
"""
###################################################
"""
define hostdependency{
dependent_host_name host_name
dependent_hostgroup_name hostgroup_name
host_name host_name
hostgroup_name hostgroup_name
inherits_parent [0/1]
execution_failure_criteria [o,d,u,p,n]
notification_failure_criteria [o,d,u,p,n]
dependency_period timeperiod_name
}
"""
####################################################
"""
define hostescalation{
host_name host_name
hostgroup_name hostgroup_name
contacts contacts
contact_groups contactgroup_name
first_notification
last_notification
notification_interval
escalation_period timeperiod_name
escalation_options [d,u,r]
}
"""
########################################################
"""
define hostextinfo{
host_name host_name
notes note_string
notes_url url
action_url url
icon_image image_file
icon_image_alt alt_string
vrml_image image_file
statusmap_image image_file
2d_coords x_coord,y_coord
3d_coords x_coord,y_coord,z_coord
}
"""
########################################################
"""
define serviceextinfo{
host_name host_name
service_description service_description
notes note_string
notes_url url
action_url url
icon_image image_file
icon_image_alt alt_string
}
"""






