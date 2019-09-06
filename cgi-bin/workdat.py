#!/usr/bin/python36

import cgi
import subprocess
print("content-type: text/html")
print() # newline
print("""
	<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>""")
disp=subprocess.getstatusoutput("sudo cat /root/Desktop/1.csv")

dl=disp[1].split("\n")
for x in dl[3:]:
  y=x.split(",")
  print("""
  <div class="card">
  <h5 class="card-header">Featured</h5>
  <div class="card-body">
  <h5 class="card-title">Special title treatment</h5>
  <pre>
  Name: """+y[0]+"""
  Location: """+y[2]+""","""+y[3]+"""
  Current job: """+y[5]+"""
  Expected pay: """+y[8]+"""
  Age: """+y[11]+"""
  Education: """+y[12]+"""
  </pre>
  <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
  </div>""")
print("""<h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>""")



# 	print("""
# <pre>
# Name: """+y[0]+"""
# Location: """+y[2]+""","""+y[3]+"""
# Current job: """+y[5]+"""
# Expected pay: """+y[8]+"""
# Age: """+y[11]+"""
# Education: """+y[12]+"""
# </pre>""")