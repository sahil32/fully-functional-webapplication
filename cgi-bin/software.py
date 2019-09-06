#!/usr/bin/python36

print("content-type: text/html\n")
import subprocess as sp
import cgi 

mydata = cgi.FieldStorage()
m = mydata.getvalue('q')

ch = sp.getstatusoutput("sudo yum install -y {}".format(m))
if ch[0] == 0:
	print("your software is installed")
else:
	print("sorry for the incovinience: "+ch[1])

  

