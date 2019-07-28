#!/usr/bin/python3

import mysql.connector


fp = open("label.txt","r")
label = fp.read()
fp.close()
f = open("/var/www/html/imageid.txt","r")
imageid = f.read()
f.close()
imgpath = "/cgi-bin/snaps/"+imageid
fptr = open("login_time.txt","r")
login_time = fptr.read()
fptr.close()
p = open("uname.txt","r")
name = p.read()
p.close()

newtable = name+label

connect=mysql.connector.connect(host='localhost',user='username',passwd='user password',database='database name')
mycur=connect.cursor()
#mycur.execute("insert into %s(imageid,sentiment) values('%s','%s')"%(name,imageid,label))
mycur.execute("update %s set imageid='%s', sentiment='%s' where login_time='%s'"%(name,imageid,label,login_time))
connect.commit()
connect.close()
