# !/usr/bin python
#--*-- coding:utf-8 --*--

import time
import urllib2
from lib.client import Client, get_api_path
import json
from lib.db import Mysql
from lib.bidItem import BidItem
from lib.currencyInfo import CurrencyInfo
import lib.printer as printer

# sql = Mysql()
# sql.createTable()

client = Client(access_key='sUgvQq9vpky9iJFztw53xBbcGXfs44KWCKFNYOhF', secret_key='YMM5qragJLoheCIKDWpqJpQJ85XqxemZ8ndm6qu1')

#sell 10 dogecoins at price 0.01
# params = {'market': 'sccny', 'side': 'sell', 'volume': 10, 'price': 0.01}
# res = client.post(get_api_path('orders'), params)
# print res

#buy 10 SC at price 0.001
# params = {'market': 'sccny', 'side': 'buy', 'volume': 10, 'price': 0.002}
# res = client.post(get_api_path('orders'), params)
# print res

# cancel order
# params = {"id": 431278171}
# res = client.post(get_api_path('delete_order'), params)
# print res

def order_book():
	result = client.get(get_api_path('order_book'), params={'market': 'sccny','asks_limit':1,'bids_limit':1})
	result = json.dumps(result)
	result = json.loads(result)

	bids = result["bids"]

	asks = result["asks"]

	for item in bids:
		printBuyOrders(item)

	for item in asks:
		printBuyOrders(item)		

		# print bid.id # 唯一的 Order ID 
		# print bid.side # Buy/Sell 代表买单/卖单
		# print bid.price # 出价
		# print bid.avg_price # 平均成交价
		# print bid.state # wait   表明订单正在市场上挂单,done   代表订单已经完全成交, cancel 代表订单已经被撤销
		# print bid.market # 订单参与的交易市场
		# print bid.created_at # 下单时间 ISO8601格式
		# print bid.volume # 数量
		# print bid.remaining_volume # 还未成交的数量
		# print bid.executed_volume # 已成交的数量 
		# print bid.trades_count # 订单的成交数 整数值

def printBuyOrders(item):
	printer.printEmptyLine()
	item = json.dumps(item)
	bid = json.loads(item, object_hook=BidItem, strict=False)
	printer.printHeader()
	printer.printContentWithUnderLine("Order ID %s" % bid.id)
	printer.printContentWithUnderLine("买/卖     %s" % bid.side)
	printer.printContentWithUnderLine("出价      %s" % bid.price)
	printer.printContentWithUnderLine("平均成交价 %s" % bid.avg_price)
	printer.printContentWithUnderLine("状态      %s" % bid.state)
	printer.printContentWithUnderLine("交易市场   %s" % bid.market)
	printer.printContentWithUnderLine("下单时间   %s" % bid.created_at)
	printer.printContentWithUnderLine("总量      %s" % bid.volume)
	printer.printContentWithUnderLine("未成交量   %s" % bid.remaining_volume)
	printer.printContentWithUnderLine("已成交量   %s" % bid.executed_volume)
	printer.printContent("订单成交数  %s" % bid.trades_count)
	printer.printTail()

def myCurrencyInfo():
	result = json.dumps(client.get(get_api_path('members')))
	result = json.loads(result,strict=False)
	print result['accounts']
	printer.printHeader()
	printer.printContent("云币网资产列表")
	for item in result['accounts']:
		currencyInfo = json.dumps(item)
		currencyInfo = json.loads(currencyInfo, object_hook=CurrencyInfo, strict=False)
		if (float(currencyInfo.balance)-0.0) > 0.0000001:
			printCurrencyInfo(currencyInfo)
	printer.printTail()

def printCurrencyInfo(currencyInfo):
	printer.printContentWithUpLine("Name    %s" % currencyInfo.currency)
	printer.printContent("balance %s" % currencyInfo.balance)
	

if __name__ == '__main__':
	# order_book()
	myCurrencyInfo()

# print result

# #demo of GET APIs

# #get member info
# print client.get(get_api_path('members'))

# #get markets
# markets =  client.get(get_api_path('markets'))
# print "markets:", markets

# #get tickers of each market
# #market should be specified in url
# print 
# print "tickers in markets"
# for market in markets:
#     print client.get(get_api_path('tickers') % market['id'])

# #get orders of each market
# #market should be specified in params
# print 
# print "orders in markets"
# for market in markets:
#     print client.get(get_api_path('orders'), {'market': market['id']})

# #get order book
# print client.get(get_api_path('order_book'), params={'market': 'btccny'})

# #get tardes
# print client.get(get_api_path('trades'), params={'market': 'btccny'})

# #get my trades
# print client.get(get_api_path('my_trades'), params={'market': 'btccny'})

# #get k line
# print client.get(get_api_path('k'), params={'market': 'etccny'})


#demo of POST APIs
#DANGROUS, you better use test account to debug POST APIs

"""
markets =  client.get(get_api_path('markets'))
print markets

#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 10, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res

#buy 10 dogecoins at price 0.001
params = {'market': 'dogcny', 'side': 'buy', 'volume': 10, 'price': 0.001}
res = client.post(get_api_path('orders'), params)
print res

#clear all orders in all markets
res = client.post(get_api_path('clear'))
print res
#delete a specific order by order_id

#first, let's create an sell order
#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 12, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res
order_id = res['id']

#delete this order
params = {"id": order_id}
res = client.post(get_api_path('delete_order'), params)
print res

#create multi orders
params = {'market': 'dogcny', 'orders': [{'side': 'buy', 'volume': 12, 'price': 0.0002}, {'side': 'sell', 'volume': 11, 'price': 0.01}]}
res = client.post(get_api_path('multi_orders'), params)
print res
"""