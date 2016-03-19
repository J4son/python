#!/usr/bin/env python
import logging,suds,suds.xsd.doctor,sys,re,CDRonDemandService_client,RISService_client,ControlCenterServices_client



CDRonDemandService_client.get_file_listRequest


"""
cache = suds.cache.ObjectCache(location="/tmp/suds",months=24)
logging.basicConfig(level=logging.ERROR)
doctor = suds.xsd.doctor #mise en oeuvre due l'inspection du WSDL
imp = suds.xsd.doctor.Import('http://schemas.xmlsoap.org/soap/encoding/') #ajout des URL des schemas pour interpreter le WSDL
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/soap/')
imp.filter.add('http://schemas.cisco.com/ast/soap/')
imp.filter.add('http://www.w3.org/2001/XMLSchema')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/ControlCenterServices/')
imp.filter.add('http://cisco.com/ccm/serviceability/soap/LogCollection/')
doctor = suds.xsd.doctor.ImportDoctor(imp) #parsing du WSDL sur le serveur CCM distant
buf=""

#variable de connexion
cucm = '172.16.5.133'
ccmuser = 'ccmadmin'
ccmpwd = 'Tel1ndus$'
#classe = 'Cisco SIP'
#compteur = sys.argv[5]
#filtre = sys.argv[6]

url_perfmon = 'https://' + cucm + ':8443/CDRonDemandService/services/CDRonDemand?wsdl'
CDRonDemandService  = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
resultat2 = CDRonDemandService.service.get_file_list('201010040000', '201010040000', '1')
     
#variable de connexion
cucm = '10.35.68.10'
ccmuser = 'brurauc'
ccmpwd = '00000'
#classe = 'Cisco SIP'
#compteur = sys.argv[5]
#filtre = sys.argv[6]

url_perfmon = 'https://' + cucm + ':8443/CDRonDemandService/services/CDRonDemand?wsdl'
CDRonDemandService  = suds.client.Client(url_perfmon,username=ccmuser,password=ccmpwd,doctor=doctor)
#resultat = CDRonDemandService.service.get_file_list('201010270000')
resultat2 = CDRonDemandService.service.get_file('10.35.68.10','brurauc','00000','/','*')


"""




"""
CDR on Demand Service

The CDR On-Demand Service comprises a public SOAP/HTTPS interface that is exposed to third-party billing applications or customers to allow them to query
the Cisco Unified Communications Manager CDR Repository Node to retrieve CDR/CMR files on demand through the use of two new API calls, get_file_list and get_file.

In previous releases, the CDR database stored CDR records, and third-party applications could query the database directly for the CDR records. In this release, CDRs no longer get stored in the CDR database, but as flat files.

The CDR On-Demand Service allows applications to obtain CDR files in a two-step process. First, the application requests
CDR file lists based on a specific time interval; then, it can request specific CDR files from those lists that are returned via a (s)FTP session.

The billing application can acquire a list of CDR files that match a specified time interval (get_file_list), with the maximum time span being 1 hour.
If the application needs to retrieve CDR files that span an interval over 1 hour, multiple get_file_list requests must be made to the servlet.

After the list of files is retrieved, the third-party application can then request a specific file (get_file). Upon receiving the request,
the servlet initiates a (s)FTP session and sends the requested file to the application. Only one file per request is allowed, to avoid timeouts and other potential complications.

The CDR Repository node normally transfers CDR files to the billing servers once on a preconfigured schedule, then deletes them per
the Cisco Unified Communications Manager configuration and other criteria. If for some reason the billing servers do not receive the CDR files, or want to have them sent again,
they can do so using the SOAP/HTTPS CDR On-Demand APIs. After CDR files are deleted, you cannot retrieve them.

The CDR On-Demand Service provides the following features:

•API to get a list of files that match a specified time interval (get_file_list)

•API to request a specific file that matches a specified filename (get_file)

•Limit of 1300 file names get returned from the get_file_list API

•Specified time range cannot span over 1 hour

•Service not available during CDR repository file maintenance window

•CDR files are sent via standard FTP or (s)FTP, which is user configurable

•API to request specific file (get_file) can return only one file per request

•Servlet needs to be activated through Service Activation Page

Before an application can access the CDR files, you must ensure that the SOAP APIs are activated from the Service Activation window on the CDR Repository Node where the CDR Repository Manager is activated.

Step 1	Go to http://<IP Address of Unified CM node>:8080/ccmservice

Step 2	Choose Tools Æ Service Activation.

Step 3	Select the server where the CDR Repository Manager resides.

Step 4	Under the CDR Services section, start the following services:

•Cisco SOAP - CDRonDemandService

•CDR Repository Manager

The CDR On-Demand Service depends on the CDR Repository Manager, so both must be activated.

Step 5	Click Update and wait until the page refreshes.


Tip	Remember that the On-Demand Service will not function during the Maintenance period.
Security

You can use standard FTP or SFTP to deliver the CDR files. Refer to RFC959 and RFC2228 for further details of these applications.

The CDR On-Demand Service will create either a standard FTP or SFTP session with the billing server each time that a CDR file is to be sent.
Exceptions get thrown whenever an error occurs on the Servlet side. In addition, all errors will get written into log files.

On the billing application side, Cisco recommends that billing applications implement code to catch these exceptions and display the exception string for detailed error conditions.

The following sections describe the two APIs that comprise the CDR On-Demand Service.

get_file_list

The get_file_list API allows the application to query the CDR Repository Node for a list of all the files that match a specified time interval.
The time interval of the request cannot exceed 1 hour. If you want a list of files that span more than the 1 hour time interval that is allowed, you must make multiple requests to the servlet to acquire multiple lists of filenames.

The get_file_list API returns an array of strings that contain the list of all the filenames that match the specified time interval. If no filenames exist that match the time range,
the value that is returned from the API call is simply null. If any time errors are encountered, exceptions get thrown. In addition, logs will be kept detailing the errors. Find these log files in the /var/log/active/tomcat/logs/soap/log4j directory.

A limit of 1300 file names can be returned to the application as a result of a get_file_list API call. If the file list that is returned contains 1300 file names,
but does not span the entire requested time interval, you should make additional requests with the start time of the subsequent requests as the time of the last file name that was returned in the previous request.

Parameters

The get_file_list API expects the following parameters:

Start Time

Mandatory parameter that specifies the starting time for the search interval. The format is a string: YYYYMMDDHHMM. No default value exists.

End Time

Mandatory parameter that specifies the ending time for the search interval. The format is a string: YYYYMMDDHHMM. No default value exists.


Note	The time span between Start Time and End Time must constitute a valid interval, but be not longer than 1 hour.

Where to get the files from

Mandatory parameter that tells the servlet whether to include those files that were successfully sent to the third-party billing servers. The format is boolean.

•True = Include both files that were sent successfully and files that failed to be sent.

•False = Send only the files that failed to be sent. Do not include files that were sent successfully.

get_file

The get_file API allows customers to request a specific CDR file that matches the specified filename. The resulting CDR file then gets sent to the customer via standard FTP or secure FTP,
depending on the third-party billing application preference. The only constraint provides that the servlet can only process one file per request.

The get_file API returns normally with no value to indicate that the file has been successfully sent to the third-party billing server. If the transfer fails for any reason, exceptions get thrown.
In addition, logs detailing the errors get saved in the /var/log/active/tomcat/logs/soap/log4j directory.

Parameters

The get_file API expects the following parameters:

Host Name

Mandatory parameter (string) that specifies the hostname of the third-party billing application server, information that the servlet needs to connect to the billing server to deliver the CDR files.

User Name

Mandatory parameter (string) that specifies the username for the third-party billing application server, information that the servlet needs to connect to the billing server to deliver the CDR files.

Password

Mandatory parameter (string) that specifies the password for the third-party billing application server, information that the servlet needs to connect to the billing server to deliver the CDR files.

Remote Directory

Mandatory parameter (string) that specifies the remote directory on the third-party billing application server to that the CDR servlet is to send the CDR files.

File Name

Mandatory parameter (string) that specifies the filename of the CDR file that the third-party billing application wants delivered from the CDR On-Demand Service.

Secure FTP

Mandatory parameter (Boolean) that specifies whether to use standard FTP or secure (s)FTP to deliver the CDR files. This depends on the third-party billing application configuration and preferences.

Fault

The CDR On-Demand Service throws exceptions when certain error conditions are met:

•The servlet gets used during the maintenance period.

•The values that are entered for starting and ending time do not reflect the correct length - 
12 bytes in the format YYYYMMDDHHMM is the correct length.

•The starting and ending time spans an interval of more than 1 hour.

•The starting time is greater than or equal to the ending time (invalid interval).

•No files exist in the CDR Repository.

•The (s)FTP connection to the remote node did not get established.

•The (s)FTP application failed to send the files that the third-party billing application requested.

The exception string describes the error condition that the billing application can print with the toString() function.

"""
