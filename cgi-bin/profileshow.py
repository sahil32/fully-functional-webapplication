#!/usr/bin/python36
import sys
import mysql.connector as mysql
import cgi
import subprocess
form=cgi.FieldStorage()
eid=form.getvalue('eid')
print("content-type: text/html\n")
print() # newline
db=mysql.connect(
host="localhost",
user="root",
password="Redhat@1",
database="data"
)
cursor=db.cursor()
print(eid)
query="select contact,work,location from employer where eid="+eid
print(query)
cursor.execute(query)
val=cursor.fetchall()
print(val)
print("""
Your contact: <input nm='cont' value='{}'/>
Your work: <input nm='work' value='{}'/>
Your location: <input nm='loc' value='{}'/>
Your bill: <input nm='bill' value='{}'/>
""")




