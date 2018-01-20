# !/usr/bin python
#--*-- coding:utf-8 --*--

import time
import urllib2
from lib.client import Client, get_api_path
import json
from lib.coin import Coin
import mysql.connector
from threading import Timer
from lib.db import Mysql
import sys   
import time
import traceback
sys.setrecursionlimit(1000000)
sql = Mysql()

client = Client(access_key='sUgvQq9vpky9iJFztw53xBbcGXfs44KWCKFNYOhF', secret_key='YMM5qragJLoheCIKDWpqJpQJ85XqxemZ8ndm6qu1')

# markets =  client.get(get_api_path('markets'))
tableNamesDicts = {'etccny': 'ticker_etc','ethcny': 'ticker_eth','btscny':'ticker_bts','btccny':'ticker_btc'}

coinPrices = {'etccny': 0.0,'ethcny': 0.0,'btscny':0.0,'btccny':0.0}

coinPriceTendencies = {'etccny': 0,'ethcny': 0,'btscny':0,'btccny':0}

def compareCoinPrices(coinName,coin):
	price = coinPrices[coinName]
	sellPrice = coin.ticker.sell
	if price == 0:
		coinPrices[coinName] = sellPrice
	else:
		coinPrices[coinName] = sellPrice
		print coinName,price,sellPrice,
		if sellPrice > price:
			print "涨了"
			coinPriceTendencies[coinName] = coinPriceTendencies[coinName]+1
		elif sellPrice < price:
			coinPriceTendencies[coinName] = coinPriceTendencies[coinName]-1
			print "跌了"


def saveTicker(coin,tableName):
	sql.insert(coin,tableName)

def as_coin(dct):
	if 'ticker' in dct:
		return Coin(dct['ticker'])

# def saveCoin(coinName):
# 	result = client.getWithOutSign(get_api_path('tickers') % coinName)
# 	result = json.dumps(result)
# 	coin = json.loads(result, object_hook=Coin, strict=False)
# 	saveTicker(coin)
# 	print coin

# 	t = Timer(120, saveCoin(coinName))  
# 	t.start()

def saveCoin(coinName):
	print '-------begin-------'
	result = client.getWithOutSign(get_api_path('tickers') % coinName)
	# print 'result',result
	result = json.dumps(result)
	coin = json.loads(result, object_hook=Coin, strict=False)
	saveTicker(coin,tableNamesDicts[coinName])
	compareCoinPrices(coinName,coin)
	print '-------end-------'

if __name__ == '__main__':
	while True:
		try:
			for key in tableNamesDicts:
				saveCoin(key)
				time.sleep(5)
		except:
			traceback.print_exc()
