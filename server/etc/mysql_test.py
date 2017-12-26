#-*-coding:utf-8-*-
#!/usr/bin/env python
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn=pymysql.connect(host='localhost',user='root',password='ubuntu',db='ubuntu',charset='utf8')

conn.query("set character_set_connection=utf8;")
conn.query("set character_set_server=utf8;")
conn.query("set character_set_client=utf8;")
conn.query("set character_set_results=utf8;")
conn.query("set character_set_database=utf8;")

curs = conn.cursor()
received_data = "start"
translation = unicode("안녕")
print("trans : " + str(translation))
sql = "insert into translation_table(received_data,translation) values('"+str(received_data)+"','"+str(translation)+"')"

curs.execute(sql)

conn.commit()
curs.close()
conn.close()
