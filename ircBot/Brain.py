from irc import irc
import QuoteSys
import sys
import signal
import urllib2
from bs4 import BeautifulSoup as BS


"""
Why not return a value that is parsed?
Don't know maybe because in this way I 
could keep all the data handling inside this class.
Just to do as little as possible in the main loop.
"""

class BotBrain(irc):
    found = False
    command = ""
    data = ""
    ident = False
    
    #clear log data
    log = open('log.txt','w')
    log.close()
    
    #give it the file name it needs to work with.
    quoteSys = QuoteSys.quote('quote.txt')
    
    def logging(self,data):
        """function for logging progress."""
        #we keep a log, so i keep data on the irc log and results of
        #of the tests and module data.
        log = open('log.txt','a')
        #for test purposes we can also print.
        #print data+"\n"
        log.write(data+"\n")
        log.close()
    def parseCommand(self,data):
        """
        function that parses commands from input data
        messages are checked to see if there is a username/nickname
        in it that matches the botowner.
        private commands are:
        !join
        !quit
        !master
        !say name
        !say:
        !ident

        public:
        !42
        maybe !quote
        and the sub commands of !quote private.
        """
        self.data = data
        self.found = self.findPing(data)
        if(self.found):
            self.command = "ping"
            self.found = True
            return
        else:
            self.found = False
            
        #private meaning only listens to self.owner in a pm
        if data.find("PRIVMSG "+self.nick)!=-1 and self.getUserName(data) == self.owner:
            if data.find(" :!")!=-1:
                self.found = True
                if data.find("join ")!=-1:
                    self.command = "join"
                elif data.find("quit")!=-1:
                    self.command = "quit"
                elif data.find("master")!=-1:
                    self.command = "master"
                elif data.find("say name")!=-1:
                    self.command = "sayname"
                elif data.find("say: ")!= -1:
                    self.command = "say"
                elif data.find("ident")!= -1:
                    if self.getUserName(data) == self.owner:
                        self.command = "ident"
                    else:
                        pass
                #elif data.find("42")!= -1:
                #    self.command = "42"
                #elif data.find("quote")!= -1:
                #    self.command = "quote"
                else:
                    self.found = False
        #public private message meaning it listens to anyone in a pm. (when identified)
        #and sends actuall irc data to owner and trollololo to the person in question.
        if data.find("PRIVMSG "+self.nick)!=-1 and self.ident:
            self.Privmsg(self.owner,self.data)
            if self.getUserName(data) != self.owner:
				self.Privmsg(self.getUserName(data),"Trollololo")
            
        #commands that can be used in a channel by me. thus only self.owner (owner)
        if data.find("PRIVMSG "+self.channel)!=-1 and self.getUserName(data) == self.owner:
            if data.find(" :!")!=-1:
                self.found = True
                if data.find("42")!=-1:
                    self.command = "42"
                elif data.find("caveQuote")!=-1:
					self.command = "caveQuote"
                else:
                    self.found = False
                    
        #commands that are used in the channel by anyone
        elif data.find("PRIVMSG "+self.channel)!=-1:
            if data.find(" :@")!=-1:
                self.found = True
                if data.find("help")!=-1:
                    if data.find("quote"):
                        self.command = "quote help"
                if data.find(" :!")!=-1:
					if data.find("quote")!=-1:
						self.command = "quote"
					else:
						self.found = False
                
        #else:
        #    self.found = False
    def findPing(self,ping):
        """
        look wheter there was a ping found from the server
        and return acordingly
        """
        ping = ping.split(" :")[0]
        if(ping == "PING"):
            return True
        else:
            return False
    
    def executeCommand(self):
        """execute parsed commands."""
        if self.command == "ping":
            self.logging("Ponged ")
            self.ping()
        if self.command == "join":
            self.leaveChan(self.channel)
        if self.command == "say":
            self.say(self.extractChatMessage(self.data))
        if self.command == "sayname":
            self.sayName()
        if self.command == "quit":
            self.quit()
        if self.command == "master":
            self.master()
        if self.command == "42":
            self.fourthyTwo()
        if self.command == "caveQuote":
			self.caveQuote()
        if self.command == "quote help":
            """
            !quote
            !quote add
            !quote remove <num>
            !quote request <num>
            !quote list size
            !quote help
            """
            self.say("This is quote help:")
            self.say("some only work when you are allowed to use,")
            self.say("meaning you need to be a known user to the bot.")
            self.say("!quote <help>:        gives you a random quote, and optional help for detailed help.")
            self.say("!quote add <quote> :  allows you to add quote")
            self.say("!quote remove <num> : allows you to remove a specific quote")
            self.say("!quote request <num>: allows you to request a specific quote")
            self.say("!quote list size :    gives you the number of quotes in a list")
        if self.command == "quote":
            self.quoteSys.process(self.data,self.getUserName(self.data),self.owner)
            if self.quoteSys.returnData:
                self.say(self.quoteSys.data)
                self.quoteSys.returnData = False
        if self.command == "ident":
            pass
            #if self.data.find(self.nick+" :"+self.nick+" is not a registered"):
            #    self.Privmsg(self.owner, "user not registered")
            #    self.ident = False
            #else:
            #    self.Privmsg("nickserv","identify "+self.password)
            #    self.ident = True
    
    def leaveChan(self,chan):
        """
			#if self.data.find(self.nick+" :"+self.nick+" is not a registered"):
				self.Privmsg(self.owner, "user not registered")
				self.ident = False
			#else:
				self.Privmsg("nickserv","identify "+self.password)
				self.ident = True
		"""	"""
        function for leaving a irc channel
        also leaves and joins a other channel
        it leaves the global channel (self.channel) and joins 
        channel passed through the chan param.
        """
        for l in xrange(len(self.data)):
            if self.data[l] == ":":
                chan = self.data
                chan = chan[l+len("!join "):len(self.data)]
                self.logging("chan >> "+chan)
                self.leavechan(self.channel)
                self.join(chan)
                self.channel = chan.strip(' ')
    def getCaveQuote(self):
		response = urllib2.urlopen('http://www.cavejohnsonhere.com/random/')
		html = response.read()
		soup = BS(html)
		elem = soup.findAll('div', {'class':'quote_main'})
		return elem[0].text
    """function for joining a channel"""
    def join(self,chan):
        self.joinchan(chan)
    """get what is to be sayed for a command. """
    def extractChatMessage(self,data):
        return data.split(':!')[1][len("say: "):]
    """function for sending something to the current channel it is in."""
    def say(self,data):
        self.sendmsg(self.channel, data)
    """function for saying it's name (brain name)."""
    def sayName(self):
        self.sendmsg(self.channel, "Hello everyone! I am Artie.")
    """Tell who is it's master"""
    def master(self):
        self.sendmsg(self.channel,"Hello there! "+self.owner+" is my Master.")
    """tell a lovely qoute"""
    def fourthyTwo(self):
        self.sendmsg(self.channel, 'Douglas Adams - "42 is a nice number that you can take home and introduce to your family."')
    def caveQuote(self):
		currentCaveQuote = self.getCaveQuote();
		self.sendmsg(self.channel, currentCaveQuote)
    """Quit (still needs to be updated properly to quit from the channel the right way)"""
    def quit(self):
        self.ircQuit("There I go die again! good bye cruel world, maybe see you another time again, at another place and time maybe.")
        sys.exit(1)
