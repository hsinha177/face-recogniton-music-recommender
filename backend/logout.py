#!/usr/bin/python3

import cgi      #for connecting webpage
import cgitb
import datetime
import mysql.connector

now = datetime.datetime.now()
ctime=now.strftime("%Y-%m-%d %H:%M:%S")

fptr = open("login_time.txt","r")
login_time = fptr.read()
fptr.close()
p = open("uname.txt","r")
name = p.read()
p.close()

print("Content-type:text/html") #information about the type of content it will read
print("")

connect=mysql.connector.connect(host="localhost",user="root",passwd="root",database="reko")
mycur=connect.cursor()
mycur.execute("update %s set logout_time='%s' where login_time='%s'"%(name,ctime,login_time))
connect.commit()
connect.close()
print("Come back soon ':)' ")
print("<meta http-equiv='refresh' content='0;url=https://13.233.28.221/mylogin.html'>")
