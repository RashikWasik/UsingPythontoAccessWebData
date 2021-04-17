# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1079134.txt (There are 91 values and the sum ends with 461)

# The basic outline of this problem is to read the file, look for integers using the re.findall(), 
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.



import re

li = list()

total = 0

with open("regex_sum_1079134.txt","r") as textfile:
    for i in textfile:
        numbers = re.findall("[0-9]+",i)
        
        if numbers == []:
            continue      # It's gonna skip all the None values
            
        else:
            for a in numbers:
                total = total+int(a) # Here 'a' is string. So I have to convert it into integer
print(total)        