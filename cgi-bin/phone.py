#!/usr/bin/python36
print("content-type: text/html\n")
import mysql.connector as mysql
db = mysql.connect(
   host="localhost",
   user="root",
   password="Redhat@1",
   database="data"
)
cursor=db.cursor()
cursor.execute("SELECT phone FROM Persons where personid=143")
table = cursor.fetchall()

print(table[0][0])
