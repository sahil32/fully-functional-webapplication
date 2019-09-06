#!/usr/bin/python36

import subprocess
import cgi
data = cgi.FieldStorage()

usr = data.getvalue('user')
pas = data.getvalue('pass')

print("content-type: text/html\n")

ch = subprocess.getstatusoutput("sudo useradd {}".format(usr))
c2 = subprocess.getstatusoutput("echo {} | sudo passwd --stdin {}".format(pas, pas))

print(ch)

