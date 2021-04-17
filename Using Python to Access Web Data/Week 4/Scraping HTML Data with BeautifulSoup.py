# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the 
# HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1079136.html (Sum ends with 13)





from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = ("http://py4e-data.dr-chuck.net/comments_1079136.html")
html = urlopen(url).read()

asd = BeautifulSoup(html,"html.parser")
tags = asd("span")

li = list()

for i in tags:
    y = str(i)    
    a = re.findall("[0-9]+",y)    
    li = li + a

total = 0

for b in li:
    total = total + int(b)
    
print(total) 
