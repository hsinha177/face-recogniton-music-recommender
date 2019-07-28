#!/usr/bin/python3

import cgi
import cgitb   
import subprocess
import pandas as pd
import re
from itertools import islice

#to show common error in webbrowser
cgitb.enable()

print("Content-type:text/html")
print("")

import webbrowser,time

print("<html>")
print(" <head> <title>Search Results</title></head>")
print("<body style='background: rgba(233, 237, 123, 0.87); font-size: 18px;'>")
print("<h2>Your Top Songs</h2>")

#with open(filename, 'r') as input_file:
#input_file.seek(0)
#songlist = islice(input_file, number_of_lines)
#for line in songlist:

#filename = "songlist.txt"
#number_of_lines = 5

fp = open("songlist.txt","r+",encoding="utf-8")
fp.seek(0)

for line in fp:
	#print("<h4>"+line+"</h4>")
	#print("<pre>")
	print("<a href= https://www.youtube.com/results?search_query="+line+">")
	print("<h4>"+line+"</h4>")
	print("</a>")
	#print("</pre>")
print("</body></html>")

fp.close()
#print("<meta http-equiv='refresh' content='60;url=https://13.233.28.221/index.html'>") 	
