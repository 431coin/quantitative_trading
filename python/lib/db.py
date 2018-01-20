import mysql.connector

import datetime

conn = mysql.connector.connect(user='root', password='liuguanli', database='yunbi', use_unicode=True)

def changeDate(dataValue):
	dateArray = datetime.datetime.utcfromtimestamp(dataValue)
	dateArray = dateArray + datetime.timedelta(hours=8)
	otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
	return otherStyleTime

class Mysql(): 
	
# cursor = conn.cursor()

# cursor.execute('select * from ticker_etc')
# results = cursor.fetchall()
# for row in results:
# 	print row
# cursor.close()

	# update

	def update(coin):
		cursor = conn.cursor()
		cursor.execute('')


	# select

	def select(self):
		cursor.execute('select * from ticker_etc')
		results = cursor.fetchall()

	# insert
	# def insert(self,coin):
	# 	cursor = conn.cursor()
	# 	cursor.execute('insert into ticker_etc (time, sell,buy,last,vol,high,low) values (%s, %s, %s, %s, %s, %s, %s)', [changeDate(coin.at), coin.ticker.sell,coin.ticker.buy,coin.ticker.last,coin.ticker.vol,coin.ticker.high,coin.ticker.low])
	# 	conn.commit()
	# 	cursor.close()

	def insert(self,coin,tableName):
		cursor = conn.cursor()
		cursor.execute('insert into '+tableName+' (time, sell,buy,last,vol,high,low) values (%s, %s, %s, %s, %s, %s, %s)', [changeDate(coin.at), coin.ticker.sell,coin.ticker.buy,coin.ticker.last,coin.ticker.vol,coin.ticker.high,coin.ticker.low])
		conn.commit()
		cursor.close()

	# delete
	def delete(self,coin):
		cursor = conn.cursor()
		cursor.execute()
		conn.commit()
		cursor.close()

	# transaction

	# condition select

	def createTable(self):
		cursor = conn.cursor()
		cursor.execute("DROP TABLE IF EXISTS ticker_btc")
		sql = """CREATE TABLE ticker_btc (
	        id int(31) NOT NULL AUTO_INCREMENT,
		   	time varchar(255) NOT NULL,
		   	sell double(16,4) NOT NULL,
		   	buy double(16,4) NOT NULL,
		   	last double(16,4) NOT NULL,
		   	vol double(16,4) NOT NULL,
		   	high double(16,4) NOT NULL,
		   	low double(16,4) NOT NULL,
	        PRIMARY KEY (id) )"""
		cursor.execute(sql)


# DROP TABLE IF EXISTS `ticker_eth`;
# CREATE TABLE `ticker_eth` (
#   `id` int(31) NOT NULL AUTO_INCREMENT,
#   `time` varchar(255) NOT NULL,
#   `sell` double(16,4) NOT NULL,
#   `buy` double(16,4) NOT NULL,
#   `last` double(16,4) NOT NULL,
#   `vol` double(16,4) NOT NULL,
#   `high` double(16,4) NOT NULL,
#   `low` double(16,4) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=17204 DEFAULT CHARSET=utf8;

# SET FOREIGN_KEY_CHECKS = 1;
