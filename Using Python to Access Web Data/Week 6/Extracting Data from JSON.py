# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment 
# counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1079139.json (Sum ends with 43)



import urllib.request
import json

url = ("http://py4e-data.dr-chuck.net/comments_1079139.json")
js = urllib.request.urlopen(url).read()
info = json.loads(js)

total = 0

for i in info["comments"]:
    asd = int(i["count"])
    total = total + asd

print(total)