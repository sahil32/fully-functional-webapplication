#!/usr/bin/python36
print("content-type: text/html")
import subprocess
import cgi
data = cgi.FieldStorage()
ip = data.getvalue("ip")
#ip = "192.168.43.1"
pas = data.getvalue('pass')
print(ip)
print(pas)
out=subprocess.getstatusoutput("sudo ./filehand.py "+ip+" "+pas)

print(out)