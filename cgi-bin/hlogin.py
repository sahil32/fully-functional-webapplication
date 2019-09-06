#!/usr/bin/python36
print("content-type: text/html")
import numpy
import cgi
import subprocess as sp
import sys
import mysql.connector as mysql
data = cgi.FieldStorage()
pas=data.getvalue("pass")
email = data.getvalue("email")
db=mysql.connect(
host="localhost",
user="root",
password="Redhat@1",
database="data"
)
cursor=db.cursor()
query="select password from login where email='{}'".format(email)
cursor.execute(query)
x=cursor.fetchall()
cursor.execute("select E_id from login where email='{}'".format(email))
y =cursor.fetchall()


m = ""
if x!=[]:
    if str(x[0][0]) == pas:
        m = 'lol'
if m == 'lol':
    print("location: http://192.168.43.124/cgi-bin/dashboard.py?id={}\n".format(y[0][0]))
else:
    print("location: http://192.168.43.124/Login_v15/login.html\n")
    print("failed")

