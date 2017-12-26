#!/usr/bin/python

import socket

s = socket.socket()
host = "192.168.0.243"
port = 12345
print(host)
s.connect((host,port))
print(s.recv(1024))
s.close()
