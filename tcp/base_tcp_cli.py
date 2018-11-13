#!/usr/bin/env python
# coding=utf-8
from socket import *

HOST=''
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=raw_input('>')
    if not data:
        break
    print data.decode('utf-8')
tcpCliSock.close()

