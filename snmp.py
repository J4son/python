import subprocess,sys,os,re
fichier = open('/Users/brur/Desktop/integration.csv','w')
cmd = ['/opt/local/bin/nmap -sP 10.35.68.1-255']
host_list =  subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
sortie = host_list.stdout.readlines()
sortie = re.findall(r"Nmap scan report for (\d*.\d*.\d*.\d*)",str(sortie))

for i in range(len(sortie)):
    hostname = ['/usr/bin/snmpwalk -v2c -c 50guf4c3 ' + sortie[i] + ' 1.3.6.1.2.1.1.5']
    proc = subprocess.Popen(hostname, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    host = proc.stdout.readlines()
    host = host[0].split()[3]
    fichier.write(sortie[i] + ";" + host + ";cucm;50guf4c3;24x7;ncc;")
    command = [' /usr/bin/snmpwalk -v2c -c 50guf4c3 ' + sortie[i] + ' 1.3.6.1.2.1.25.4.2.1.2']
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    outputlines = proc.stdout.readlines()
    for j in range(len(outputlines)):
        resultat = outputlines[j].split()[3]
        print resultat
        resultat = str(resultat.replace("\"",""))
        fichier.write("snmp_process{" + resultat  + "},")
    fichier.write(";rtr108ncc" + "\n")
    
fichier.close()


"""
    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        outputlines = proc.stdout.readlines()
        for j in range(len(outputlines)):
            resultat = outputlines[j].split()[3]
            resultat = str(resultat.replace("\"",""))
            fichier.write("snmp_process{" + resultat  + "};" + "\n")
    except OSError, err:
          print 'Got execption running command "%s": %s' % (command, err)

fichier.close()



"""






    
