#!/usr/bin/python36
import mysql.connector as mysql
import cgi
print("content-type: text/html\n")
db = mysql.connect(
    host='localhost',
    user='root',
    password='Redhat@1',
    database='data'
)
cursor = db.cursor()
data = cgi.FieldStorage()
eid = data.getvalue('eid')
