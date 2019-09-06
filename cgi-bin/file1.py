#!/usr/bin/python36
import sys
data = sys.argv
phone = data[1]
payment = data[2]
hired = data[3]
category = data[4]
other = data[5]
payment = data[6]
line = phone+","+payment+","+hired+","+category+","+other+","+payment+"\n"
file = open("/root/Desktop/company_data.csv","a")
file.write(line)
file.close()
file = open("/root/Desktop/company_data.csv","r")
x = file.read()
file.close()
print(x)