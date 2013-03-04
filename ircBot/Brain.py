from irc import irc
import QuoteSys
import sys
import signal

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
    
    """function for logging progress."""
    def logging(self,data):
        #we keep a log, so i keep data on the irc log and results of
        #of the tests and module data.
        log = open('log.txt','a')
        #for test purposes we also print.
        print data+"\n"
        log.write(data+"\n")
        log.close()
    """function that parses commands from input data"""
    def parseCommand(self,data):
        self.data = data
        self.found = self.findPing(data)
        if(self.found):
			self.command = "ping"
			self.found = True
			return
        else:
			self.found = False
        """
        messages are checked to see if there is a username/nickname
        in it that matches the botowner.
        """
        #private meaning only listens to self.owner 
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
                elif data.find("42")!= -1:
                    self.command = "42"
                elif data.find("quote")!= -1:
                    self.command = "quote"
                elif data.find("ident")!= -1:
                    self.command = "ident"
                else:
                    self.found = False
        #public private message meaning it listens to anyone in a pm.
        elif data.find("PRIVMSG "+self.nick)!=-1 and self.ident:
            self.Privmsg(self.owner,self.data)
            self.Privmsg(self.getUserName(data),"Trollololo")
        #else:
        #    self.found = False
    def findPing(self,ping):
		ping = ping.split(" :")[0]
		if(ping == "PING"):
			return True
		else:
			return False
    """execute parsed commands."""
    def executeCommand(self):
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
        if self.command == "quote":
            self.quoteSys.process(self.data)
            if self.quoteSys.returnData:
                self.say(self.quoteSys.data)
                self.quoteSys.returnData = False
        if self.command == "ident":
            self.Privmsg("nickserv","identify <@wereld12>")
            self.ident = True;
    """
        function for leaving a irc channel
        also incidently leaves and joins a other channel
        it leaves the global channel (self.channel) and joins 
        channel passed through the chan param.
    """
    def leaveChan(self,chan):
        for l in xrange(len(self.data)):
            if self.data[l] == ":":
                chan = self.data
                chan = chan[l+len("!join "):len(self.data)]
                self.logging("chan >> "+chan)
                self.leavechan(self.channel)
                self.join(chan)
                self.channel = chan.strip(' ')
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
        self.sendmsg(self.channel,"Hello there! Duality is my Master.")
    """tell a lovely qoute"""
    def fourthyTwo(self):
        self.sendmsg(self.channel, 'Douglas Adams - "42 is a nice number that you can take home and introduce to your family."')
    """Quit (still needs to be updated properly to quit from the channel the right way)"""
    def quit(self):
        sys.exit(1)
    
    
    
    
    
    
