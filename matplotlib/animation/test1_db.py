import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import pymysql

def animate(i):
	conn2 = pymysql.connect(host='localhost',user='root',password='ubuntu',db='ubuntu',charset='utf8')

	del ys1[0]

	curs = conn2.cursor(pymysql.cursors.DictCursor)
	sql = "select * from pyplot order by id desc limit 1"
	curs.execute(sql)
	rows = curs.fetchall()
	for row in rows:
		y1 = row['x1']
		ys1.append(y1)
		print(y1)

	conn2.close()
	ax1.clear()
	ax1.plot(xs, ys1)


conn = pymysql.connect(host='localhost',user='root',password='ubuntu',db='ubuntu',charset='utf8')


try:

	xs =[]

	for i in range(1,300):
		xs.append(i)


	curs = conn.cursor(pymysql.cursors.DictCursor)
	sql = "select * from pyplot order by id desc limit 299"
	curs.execute(sql)
	rows = curs.fetchall()

	ys1 =[]

	for row in rows:
		y1 = row['x1']
		ys1.append(y1)



	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)



	ani = animation.FuncAnimation(fig, animate, interval=200)
	plt.show()


except Exception as e:
	print("error occurred - " + str(e))

conn.close()


