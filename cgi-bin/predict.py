#!/usr/bin/python36
print("content-type: text/html\n")
import cgi
import subprocess as sp
data = cgi.FieldStorage()
value = data.getvalue("pre")
x = sp.getoutput("sudo ./che.py {}".format(value))
print(x.split()[-1].split("'")[1])
print(x.split()[-2].split("'")[1])