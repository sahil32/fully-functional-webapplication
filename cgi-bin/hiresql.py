#!/usr/bin/python36
import sys
import mysql.connector as mysql
data = sys.argv
db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Redhat@1',
    database = 'data'
)

cursor = db.cursor()



cursor.execute("INSERT INTO transaction (eid, labour_id, category, time_stamp, location) values("+data[1]+","+data[2]+",'"+data[3]+"', sysdate(),'"+data[4]+"' )")
db.commit()

cursor.execute("select * from Persons where Personid={}".format(data[2]))
line = cursor.fetchall()
print(line)
