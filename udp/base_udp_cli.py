#!/usr/bin/env python
# coding=utf-8
from socket import *
HOST='localhost'
BUFSIZE=1024
PORT=21567
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)

while True:
    data=raw_input('>')
    if not data:
        break;
    udpSerSock.sendto(data,ADDR)
    data,ADDR=udpSerSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data

udpSerSock.close()
