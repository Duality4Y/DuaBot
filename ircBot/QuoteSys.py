import random

class quote(object):
	def __init__(self, source):
		self.source = source
		self.File = open(source,'a')
		self.FileLength = 1
		self.data = ""
		self.returnData = True
		self.commands = ["quote add","quote remove","quote num:","quote size","quote"]
		self.numCommands = len(commands)
	def process(self,data):
		if data.find(commands[0])!= -1:
			pass
		elif data.find(commands[1])!= -1:
			pass
		elif data.find(commands[2])!= -1:
			pass
		elif data.find(commands[3])!= -1:
			pass
		else:
			
	def close(self):
		self.File.close()
