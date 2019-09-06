#!/usr/bin/python36


import subprocess as sp
import cgi
print("content-type: text/html")
m1 = cgi.FieldStorage()
p = m1.getvalue('osname')

q = m1.getvalue('os')
ch = sp.getoutput('sudo docker run -itd --name {} {}'.format(p, q))
print("location:dockerui.py\n")
#if ch[0] == 0:
	# print("our OS is launched")
# else:
	# print(":( sorry it seems to have some trouble try to change name of os")
