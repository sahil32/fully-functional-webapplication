#!/usr/bin/python36
import sys
import mysql.connector as mysql
db=mysql.connect(
host="localhost",
user="root",
password="Redhat@1",
database="data"
)
cursor=db.cursor()
data = sys.argv


#user_id = data[4]+ ","+data[1] + "\n"

#query="insert into login (email,password,id) values({} , {})".format(data[4],data[1])

#file_data.write(user_id)


query="insert into login (name,phone,email,password) values('{}' , '{}' ,'{}',{})".format(data[1],data[2],data[3],data[4])

cursor.execute(query)
db.commit()


#full_data = data[1]+","+data[2]+","+data[3]+","+data[4]+","+data[5]+","+data[6]+","+data[7]+","+data[8] + "\n"
#file_data1 = open("/root/Desktop/register_data.csv","a")
#file_data1.write(full_data)

 


