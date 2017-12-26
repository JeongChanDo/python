#!/usr/bin/env python
import socket
import time

host = "192.168.0.243"
port = 12345
buffer_size = 640*480

soc = socket.socket()
soc.bind((host,port))
soc.listen(1)
conn, address = soc.accept()
while True:
	data = []
	receive_len = 0

	data += conn.recv(buffer_size)
	receive_len += len(data)
	while True:
		left_len = len(data)-receive_len
		if left_len <= buffer_size:
			data += conn.recv(left_len)
			receive_len += left_len
			break
		data += conn.recv(buffer_size)
		receive_len += buffer_size

	print(data)
	print("len(data) : " + str(len(data)))
