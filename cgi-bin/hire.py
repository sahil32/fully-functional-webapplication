#!/usr/bin/python36
print("content-type: text/html")
import cgi
import mysql.connector as mysql
import subprocess as sp
data = cgi.FieldStorage()
eid = data.getvalue('eid')
uid = data.getvalue('uid')
ce = data.getvalue('ce')
location = data.getvalue('address')

import mysql.connector as mysql

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Redhat@1',    
    database = 'data'
)

cursor = db.cursor()



cursor.execute("INSERT INTO transaction (eid, labour_id, category, time_stamp, location) values("+eid+","+uid+",'"+ce+"', sysdate(),'"+location+"' )")
db.commit()





print("location: http://192.168.43.124/cgi-bin/list1.py\n")
