import random

class quote(object):
	def __init__(self, source):
		self.source = source
		self.FileLength = 1
		self.data = ""
		self.returnData = True
		self.commands = ["quote add","quote remove","quote num:","quote size","quote"]
		self.numCommands = len(self.commands)
	
	def process(self,data):
		if data.find(self.commands[0])!= -1:
			pass
		elif data.find(self.commands[1])!= -1:
			pass
		elif data.find(self.commands[2])!= -1:
			pass
		elif data.find(self.commands[3])!= -1:
			pass
		else:
			randomLine = random.randint(1,self.getNumOfLines())
			print "list length: ", self.getNumOfLines()
			print "a random line number: ",randomLine
			print "a random quote: ",self.getLine(randomLine)
			self.data = self.getLine(randomLine)
	
	"""return the requested line at the line number."""
	def getLine(self,lineNumberRequest):
		QuoteList = open(self.source, 'r')
		#start at zero
		LineNumber = 1
		line = []
		#if request was the first line
		if lineNumberRequest == LineNumber:
			for char in QuoteList.read():
				if char != '\n':
					line.append(char)
				else:
					QuoteList.close()
					return "".join(line)
		#if the request was not the first line.
		else:
			for char in QuoteList.read():
				if LineNumber == lineNumberRequest:
					if char != '\n':
						line.append(char)
					else:
						QuoteList.close()
						return "".join(line)
				elif char == '\n':
					LineNumber+=1
	
	"""return the number of lines in a quote file. assuming the file is not empty."""
	def getNumOfLines(self):
		QuoteList = open(self.source, 'r')
		#start at zero
		NumOfLines = 0
		for char in QuoteList.read():
			if char == '\n':
				NumOfLines += 1
		QuoteList.close
		return NumOfLines
