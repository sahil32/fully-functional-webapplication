#!/usr/bin/python36
print("content-type: text/html")


import cgi
import subprocess as sp

data=cgi.FieldStorage()
email=data.getvalue("email")
pass1=data.getvalue("password1")
name=data.getvalue("name")
phon = data.getvalue("number")
register_data = sp.getoutput("sudo ./register_data.py {} {} {} {}".format(name,phon,email,pass1))
print("location: http://192.168.43.124/Login_v15/login.html\n")

