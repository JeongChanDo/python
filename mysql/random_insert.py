import pymysql
import time
import random

conn = pymysql.connect(host='localhost',user='root',password='ubuntu',db='ubuntu',charset='utf8')
try:

	curs = conn.cursor(pymysql.cursors.DictCursor)

	sql ="insert into pyplot(x1,x2,x3) values (%s,%s,%s)"

	while True:
		x1 = random.random()
		x2 = random.random()
		x3 = random.random()
		curs.execute(sql,(x1,x2,x3))
		time.sleep(0.2)
		conn.commit()
except:
	print("error happened")
	conn.close()
