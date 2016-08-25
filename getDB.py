from subprocess import call
import sqlite3 as lite
import sys
import csv

call(["sh","load.sh"])
# con = None
# try:
# 	con=lite.connect('db_yesterday.db')
# 	print "Database created and opened succesfully"
# 	queryStr1 = '.mode csv heart_rate'
# 	queryStr2 = '.import table3.csv heart_rate;'
# 	# cur = con.cursor()
# 	con.execute(queryStr1)
# 	con.execute(queryStr2)
# 	con.commit()
# except lite.Error, e:
# 	# print "Error %s:" % e.args[0]
# 	sys.exit(1)

# finally:
# 	if con:
# 		con.close()


# con=lite.connect('db_yesterday2.db')
con=lite.connect('db_week.db')
# print "Database created and opened succesfully"
# queryStr1 = ".mode csv heart_rate;"
# queryStr2 = '.import table3.csv heart_rate;'
# # cur = con.cursor()
# conn.execute(".mode csv heart_rate");
# # conn.execute("select count(*) from heart_rate");
# # con.execute(queryStr2)
# conn.commit()
# conn.close()

# on = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("drop table if exists heart_rate;")
cur.execute("CREATE TABLE heart_rate (device_id, tstamp, rri);")

with open('table3.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['device_id'], i['tstamp'],i['rri']) for i in dr]

cur.executemany("INSERT INTO heart_rate (device_id, tstamp, rri) VALUES (?, ?, ?);", to_db)
con.commit()