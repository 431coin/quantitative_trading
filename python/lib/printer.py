#coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def printHeader():
	print "╔═════════════════════════════════════════════════"

def printTail():
	print "╚═════════════════════════════════════════════════"

def printContent(content):
	print "║", content

def printContentWithUnderLine(content):
	print "║", content
	print "╟─────────────────────────────────────────────────"

def printContentWithUpLine(content):
	print "╟─────────────────────────────────────────────────"
	print "║", content

def printLine():
	print "╟─────────────────────────────────────────────────"

def printEmptyLine():
	print