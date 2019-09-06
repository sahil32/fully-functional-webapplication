#!/usr/bin/python36
import cgi
import mysql.connector as mysql
db = mysql.connect(
host = "localhost",
user = "root", 
password = "Redhat@1",
database = "data"
)
cursor = db.cursor()

f = open("/root/Desktop/worker.csv", "r")
x = f.read()
y = x.split("\n")
for a in y[1:-1]:
    m = a.split(",")
    phone = m[0]
    pe = m[1]
    curr = m[2]
    fam = m[3]
    me = m[4]
    query = "INSERT INTO Persons ( phone, past_exp, present, family_mem, earning_members) value("+phone+",'"+pe+"','"+curr+"',"+fam+","+me+")"
   
    cursor.execute(query)
    db.commit()
