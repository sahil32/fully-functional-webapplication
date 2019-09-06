#!/usr/bin/python36
import cgi
import subprocess
print("content-type: text/html\n")
print("""<form action='http://192.168.43.124/cgi-bin/predict.py'>
<input type='text' name='pre'>
<input type='submit' value='Predict'>
</form>""")     
     


        