#!/usr/bin/python36
import subprocess
print("content-type: text/html\n")

print("""<html>
<title>Request</title>
<head>
<style>
.button {
  background-color: #4CAF50;
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
<center><h2>Your Request is Submitted.
We'll notify you as Soon as Possible!!</h2></center>

<center><a href="http://192.168.43.124/cgi-bin/dashboard.py" class="button">Go Back</a><center>""")
out=subprocess.getoutput("sudo ./call.py")