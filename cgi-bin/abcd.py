#!/usr/bin/python36
import sys 
data = sys.argv
emal = data[1]
pas = data[2]
#f = open("/root/Desktop/login.csv","r")
import sys
import mysql.connector as mysql
db=mysql.connect(
host="localhost",
user="root",
password="Redhat@1",
database="data"
)
cursor=db.cursor()
query="select password from login where email='{}' ".format(emal)
cursor.execute(query)
x=cursor.fetchall()
m = ""
if x!=[]:
    if str(x[0][0]) == pas:
        m = 'lol'
    print(m)


