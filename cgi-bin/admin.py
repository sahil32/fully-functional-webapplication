#!/usr/bin/python36
print("content-type: text/html\n")
import mysql.connector as mysql
db = mysql.connect(
    host='localhost',
    user ='root',
    password='Redhat@1',
    database='data'
)

cursor = db.cursor()
cursor.execute('select eid , labour_id, category , time_stamp ,transaction_id , location , phone from Persons, transaction where Persons.Personid=transaction.labour_id')
text = cursor.fetchall()



print("""<!DOCTYPE html>
<html>
<head>
<style>
table {
  width:20%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  text-align: left;
}
table#t01 tr:nth-child(even) {
  background-color: white;
}
table#t01 tr:nth-child(odd) {
 background-color: white;
}
table#t01 th {
  background-color: black;
  color: white;
}
.to1{

text-align: center;
color:black;
}

</style>
</head>
<body>


<table id="t01" class="rk">
  <tr>
    <th>employee_id</th>
    <th>labour_id</th> 
    <th>category</th>
	<th>time_stamp</th>
	<th>transaction_id</th>
	<th>location</th>
	<th>Phone_number</th>
  </tr>
  <tr>""")
for i in text:
    m=0
    for j in i:
        print("""<td>{}</td>
        """.format(i[m]))
        m = m+1
    print("""<td>
        <a href="#">OK</a></td>
        </tr>""")
print("""</table>
        <a href="http://192.168.43.124/cgi-bin/reccommend.py">ADD NEW</a>
        </body>
        </html>""")
      