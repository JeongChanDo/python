#-*-coding:utf-8-*-
#!/usr/bin/python
import socket
import cv2
import io
import os
from array import array
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.models.image.imagenet import classify_image
import time
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print(unicode('한글'))
#client code

def insert_data(received_data,translation):

	conn=pymysql.connect(host='localhost',user='root',password='ubuntu',db='ubuntu',charset='utf8')

	conn.query("set character_set_connection=utf8;")
	conn.query("set character_set_server=utf8;")
	conn.query("set character_set_client=utf8;")
	conn.query("set character_set_results=utf8;")
	conn.query("set character_set_database=utf8;")

	curs = conn.cursor()
	translation = unicode(translation)
	sql = "insert into translation_table(received_data,translation) values('"+str(received_data)+"','"+str(translation)+"')"

	curs.execute(sql)

	conn.commit()
	curs.close()
	conn.close()



def send_msg(result_string):
	host2 = "192.168.0.2"
	port2 = 12346
	s2 =socket.socket()
	s2.connect((host2,port2))
	string = str(result_string)
	print("string : " + string)
	result = b""
	try:
		s2.send(string)

		print('send_msg : ' + result_string)
		result = s2.recv(1024)
		print("recv result : " + str(result))
		print("trasnlation complete")
		s2.close()
	except Exception as e:
		print("send msg - e : " + str(e))
		s2.close()
	print("send_msg completed")
	return result

def image_recognition(cv_image):

	#cv2.imshow('image',cv_image)
#		cv2.waitKey(1000)

	image_data = cv2.imencode('.jpg', cv_image)[1].tostring()
		# Creates graph from saved GraphDef.
	softmax_tensor =session.graph.get_tensor_by_name('softmax:0')
	predictions = session.run(softmax_tensor,{'DecodeJpeg/contents:0':image_data})
	predictions = np.squeeze(predictions)
		# Creates node ID --> English string lookup.
	node_lookup = classify_image.NodeLookup()
	top_k = predictions.argsort()[use_top_k:][::-1]
	strings = []
	scores = []
	result_num = 0
	for node_id in top_k:
		human_string = node_lookup.id_to_string(node_id)
		score = predictions[node_id]
		if score > score_threshold:
			strings.append(human_string)
			scores.append(float(score))
			result_num += 1


	return strings, scores,result_num


def translation(string,scores):
	result_string = ""
	max_index = scores.index(max(scores))
	score = scores[max_index]
	result_string = strings[max_index]
	print("result_string : "+result_string+" score : %.5f"%(score))

	#start send_msg translation
	trans_str = send_msg(result_string)
	insert_data(result_string,trans_str)


	return trans_str

def save_image(c):

	recv_data =[]
	idx=0
	print("start while")

	length_len = c.recv(1)
	length_len = ord(length_len)
	print("length_len : " + str(length_len))

	recv_length = c.recv(length_len)
	length = 0
	for l in recv_length:
		length *= 10
		length += int(str(l))

	print("length : " + str(length))


	while True:
		data = c.recv(int(buffer_size))
#	print("data received... len(data) : " + str(len(data)))
		idx = 0
		for i in data:
			idx +=1
			recv_data.append(i)
		print("len : " + str(len(recv_data)) +"   total_len : " + str(length))
		if len(recv_data) == length:
			break
	print("end while")

	arr = np.array(recv_data)
	bytearr = arr.tobytes()

	print("recv_data length : " + str(len(recv_data)))
	image = Image.open(io.BytesIO(bytearr))
	image.save('python.jpg')

#server code

classify_image.maybe_download_and_extract()
session = tf.Session()
classify_image.create_graph()

host = "192.168.0.2"
port = 12345
buffer_size=1024
score_threshold = 0.1
use_top_k = 5


s = socket.socket()


try:
	s.bind((host,port))

	s.listen(5)
	while True:
		print("wait request...")
		c, addr = s.accept()
		print("connection established..")
#start image recv

		save_image(c)

#end image receive

##image recognition
		cv_image = cv2.imread('python.jpg',cv2.IMREAD_COLOR)
		strings, scores,result_num = image_recognition(cv_image)

		trans_str = "no data".encode('utf-8')
		print("result_num : " +str(result_num))
		if result_num != 0:
			trans_str = translation(strings,scores)


##end image recognition

#start send_trans_str
		print type(trans_str)
		print(str(trans_str))

		c.send(trans_str)
		print("translation string sended.")
#end send_trans_str


except KeyboardInterrupt:
	print("keyboard interrupt - socket close")
	s.close()
except Exception as e:
	print("socket close")
	print(e)
	s.close()
except socket.error:
	print("socket close")
	s.close()

