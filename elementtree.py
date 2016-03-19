import urllib2
from Tkinter import *
try:
    import xml.etree.ElementTree as ET
except ImportError:
    import cElementTree as ET

cve = urllib2.urlopen("http://nvd.nist.gov/download/nvd-rss.xml")
root = ET.parse(cve).getroot()
titles = []
for i in root.findall('{http://purl.org/rss/1.0/}item'):
    titles.append(i.find('{http://purl.org/rss/1.0/}title').text)

