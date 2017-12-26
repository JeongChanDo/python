import socket

host = '192.168.0.2'
port = 12345

s = socket.socket()
s.bind((host,port))
s.listen(5)

c, addr = s.accept()
c.send('abcd')

c.close()
s.close()

