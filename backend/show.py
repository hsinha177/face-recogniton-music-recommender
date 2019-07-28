#!/usr/bin/python3

import mysql.connector
import cgi
import cgitb
mySQLconn = mysql.connector.connect(host='localhost',
                             database='reko',
                             user='root',
                             password='root')

p = open("uname.txt","r")
name = p.read()
p.close()
print("Content-type:text/html")
print("")

sql_select_Query = "select login_time,logout_time,sentiment from "+name+";"
cursor = mySQLconn.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("<html> <head> <title>Search Results</title></head>")
print("<body style='background: rgba(233, 237, 123, 0.87); font-size: 18px;'>")
print("<h2>User's History </h2>")
print("<br>")
print("<pre>")
print("Total number of rows = ", cursor.rowcount)
print("(Login_time		Logout_time		Sentiment)")
for row in records:
	#print("Login_time = ", row[0], )
	print(row)
print("</pre>")
print("</body></html>")
cursor.close()
   
