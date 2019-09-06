#!/usr/bin/python36
import subprocess


print("content-type: text/html\n")
ch = subprocess.getoutput("date")


print(ch)
