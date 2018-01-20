
class Ticker(object):
	# __slots__ = ('buy', 'sell','low','high','last','vol')

	def __init__(self, data):
    	self.__dict__ = data