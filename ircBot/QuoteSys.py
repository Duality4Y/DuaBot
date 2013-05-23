import random

class quote(object):
	"""
	commands are:
	!quote
	!quote add
	!quote remove
	!quote num: <num>
	!quote list size ,return number of lines in the list thus the numbers of quotes.
	
	__future__:
	Idea: A !quote lists. for available list you can quote from.
	needs to implement catagories.
	"""
	def __init__(self, source):
		self.source = source
		self.FileLength = self.getNumOfLines()
		self.data = ""
		self.returnData = False
		self.commands = ["quote add","quote remove","quote request","quote list size","quote"]
		self.numCommands = len(self.commands)
	def process(self,Process_Data,foundNick,owner):
		has_access = foundNick == owner
		print "Got Private access?: "+str(has_access)
		#quote only is to determine if it's only !quote or !quote pluss extra's (advance commands)
		quote_only = not bool(Process_Data.split(":!quote")[1])
		#find first command, add line.
		if Process_Data.find(self.commands[0])!= -1 and has_access:
			self.addLine(Process_Data)
			self.data = "Thanks for adding a quote!"
			self.returnData = True
		#find second command, remove a line.
		elif Process_Data.find(self.commands[1])!= -1 and has_access:
			self.data = "Not implemeted removing a Quote yet"
			self.returnData = True
		#find third command, return requested quote.
		elif Process_Data.find(self.commands[2])!= -1 and has_access:
			self.data = "Not implemented requesting a Quote yet"
			self.returnData = True
		#find fourth command, return list size.
		elif Process_Data.find(self.commands[3])!= -1 and has_access:
			self.data = "The list size is: "+str(self.getNumOfLines())+"!";
			self.returnData = True
		#find fith command !quote anyone can use.
		elif Process_Data.find(self.commands[4])!=-1 and quote_only:
			randomLine = random.randint(1,self.getNumOfLines())
			print "list length: ", self.getNumOfLines()
			print "a random line number: ",randomLine
			print "a random quote: ",self.getLine(randomLine)
			self.data = self.getLine(randomLine)
			self.returnData = True
		elif not (Process_Data.split(":!")[1] in self.commands):
			self.data = "None Existing Command?"
			self.returnData = True
		elif not has_access:
			self.data = "your not authorized to do that!"
			self.returnData = True
		else:
			return None
		return None
		
	"""adds a Quote to a file."""
	def addLine(self,line):
		line = line.join(line.split(" :!")[1:])[len(self.commands[0]):]
		line = line.strip('\n\r')
		print "line to add>> ",line
		QuoteList = open(self.source,'a')
		QuoteList.write(line+'\n')
		QuoteList.close()
		
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
		"""alsways be sure to close a file!"""
		QuoteList.close()
	
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
