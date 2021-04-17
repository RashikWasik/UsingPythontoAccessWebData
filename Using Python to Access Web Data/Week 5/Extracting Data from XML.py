# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts 
# from the XML data, compute the sum of the numbers in the file.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1079138.xml (Sum ends with 63)



import urllib.request
import xml.etree.ElementTree as ET

url = ("http://py4e-data.dr-chuck.net/comments_1079138.xml")
xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)

total = 0

for i in tree.findall("comments/comment"):
    asd = int(i.find("count").text)
    total = total + asd

print(total)