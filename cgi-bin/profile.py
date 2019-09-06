#!/usr/bin/python36
print("content-type: text/html\n")

import cgi
import mysql.connector as mysql
import subprocess as sp
data = cgi.FieldStorage()

eid = data.getvalue('eid')
uid = data.getvalue('uid')
ce = str(data.getvalue('ce'))

print("""
<!DOCTYPE html>
<html>
<title>Hiring</title>
<head>
  <link rel="stylesheet" href="css.css">
<style>
.button {
  background-color: #008CBA;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>
</head>
 <!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">KaamKaaZ</a>
    </div>
    <ul class="nav navbar-nav">	      
    </ul>
  </div>
</nav>
  
<div class="container">
  <h3></h3>
  <p></p>
</div>

</body>
</html>

<form action="http://192.168.43.124/cgi-bin/hire.py">
<center>
<input type="number" name="number" placeholder="Enter your number"><br><br>
<input type="text" value='"""+ce+"""' name='ce'><br><br>
<textarea placeholder="Address" name="address"></textarea><br><br>
<input type='hidden' value='"""+eid+"""' name='eid'><br><br>
<input type='hidden' value='"""+uid+"""' name='uid'><br><br>
<input type='submit' value='SUBMIT' class="button">
</center>
</form>
</body>
</html>
""")
#""".format(ce))
