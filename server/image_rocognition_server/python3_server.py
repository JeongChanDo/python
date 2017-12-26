#!/usr/bin/python
import os
import sys
import urllib.request
import socket
s = socket.socket()

host = "192.168.0.2"
port = 12346
s.bind((host,port))
s.listen(5)
try:
	while True:
		c, addr = s.accept()

		recv_data=c.recv(1024)
		print("rwa recv_data : " +str(recv_data))
		recv_data = str(recv_data.decode('utf-8'))
		print("recv_data : " + recv_data)

		client_id = "UsEgn2I1nWQmZuK9UU0M"
		client_secret = "rpXCTqYLtW"
		encText = urllib.parse.quote(recv_data)
		data = "source=en&target=ko&text=" + encText
		url = "https://openapi.naver.com/v1/papago/n2mt"
		request = urllib.request.Request(url)
		request.add_header("X-Naver-Client-Id",client_id)
		request.add_header("X-Naver-Client-Secret",client_secret)
		response = urllib.request.urlopen(request, data=data.encode("utf-8"))
		rescode = response.getcode()
		if(rescode==200):
			response_body = response.read()
			response = str(response_body.decode('utf-8'))

			str1="Text\":\""
			str2="\"}}}"
			idx1 = response.index(str1)+7
			idx2 = response.rindex(str2)
			result = response[idx1:idx2]
			print(response[idx1:idx2])
			print("type(result) : " + str(type(result)))
			print("type(result) : " + str(type(result.encode('utf-8'))))
			c.send(result.encode('utf-8'))
			print("response complete.  send_msg : "+result)
		else:
			print("Error Code:" + rescode)
except Exception as e:
	print("e : " + str(e))
	print("close socket")
	s.close()
except KeyboardInterrupt:
	print("close socket")
	s.close()

