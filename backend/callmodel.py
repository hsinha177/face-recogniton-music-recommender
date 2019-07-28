#!/usr/bin/python3

import cgi      #for connecting webpage
import cgitb
import sys
import snap_testing 
import userdb

fp = open("label.txt","r")
label = fp.read()
fp.close()

print("Content-type:text/html") #information about the type of content it will read
print("")
 
#print("<meta http-equiiv='refresh' content='0;url=http://13.233.28.221/Sentiment.html'>")
print("<html> <head> <title>Search Results</title></head>")
print("<body style='background: rgba(233, 237, 123, 0.87); font-size: 18px;'>")
print("<h2>Facial Expression analysing ... </h2>")
print("<br>")
print("<pre>")
print("You seem to be :"+label+" ")
print("<a href=https://13.233.28.221/Sentiment.html target='_blank'>")
print("Back")
print("</a>")
print("</pre>")
print("</body></html>")
