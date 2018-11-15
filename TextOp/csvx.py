#!/usr/bin/env python
# coding=utf-8
import csv

from distutils.log import warn as printf

DATA=((9,'Web Client and Servers','base64 urllib'),(10,'Web Programing :CGI & WSGI','cgi,time,wsgiref'),(13,'Web Servers','urllib,twython'),)

printf('*** WRITE CSV DATA')
f=open('bookdata.csv','w')
writer=csv.writer(f)
for record in DATA:
    writer.writerow(record)
f.close()

printf('***REVIEW OF WAVED DATA')
f=open('bookdata.csv','r')
reader=csv.reader(f)
for chap,title,modpkgs in reader:
    printf('Chapter %s :%r (featuring %s) ' %(chap,title,modpkgs))
f.close()
