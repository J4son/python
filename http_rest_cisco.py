import xml.dom.minidom
from urllib.request import Request, urlopen

req = Request('https://64.103.26.61/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
response = urlopen(req)
responseString = response.read().decode("utf-8")
dom = xml.dom.minidom.parseString(responseString)
xml = dom.toprettyxml()
print(xml)
response.close()
