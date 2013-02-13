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
    log = open('log.txt','w')
    quoteSys = QuoteSys.quote('quote.txt')
    def logging(self,data):
		#for test purposes we also print.
		print data+"\r\n"
		self.log.write(data)       
    def parseCommand(self,data):
        self.data = data
        self.found = self.findPing(data)
        if(self.found):
			self.command = "ping"
			self.found = True
			return;
        else:
			self.found = False
        """
        Maybe its a idea to add data.find("botowner") to the 
        check whether we found a command or not, just to see
        from who'm we had gotten the command actually is the 
        person who's supposed to give commands... but yea
        maybe it be better to check for the name in the protocol
        string since if a random user be giving commands and
        put the right name somewhere in there then there would
        be found the botowner name and thus comman is valid.
        but yea future stuff.
        """
        if data.find("PRIVMSG "+self.nick)!=-1 and self.findUser(data) == self.owner:
            if data.find(":!")!=-1:
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
                    self.command = "quote";
            """
            else:
                pass;
                
                #send = data.split(':',1)[1]
                #print "Pm: "+self.getUserName(data)+" >> ",send
                #self.Privmsg(self.getUserName(data),send)
            """
        else:
            self.found = False
        """a test for something else ment to send back what ever
           was entered in a chat channel not needed in parsing 
           for commands."""
        """
        if data.find("PRIVMSG "+self.channel)!=-1:
            #return ircmsg
            pass
        """
    def findPing(self,ping):
		ping = ping.split(" :")[0]
		if(ping == "PING"):
			return True
		else:
			return False
    def findUser(self,data):
		nick = data.split("!",1)[0][1:]
		self.logging("findUser >> "+nick)
		return nick
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
    def leaveChan(self,chan):
        for l in xrange(len(self.data)):
            if self.data[l] == ":":
                chan = self.data
                chan = chan[l+len("!join "):len(self.data)]
                self.logging("chan >> "+chan)
                self.leavechan(self.channel)
                self.join(chan)
                self.channel = chan.strip(' ')
    def join(self,chan):
        self.joinchan(chan)
    def extractChatMessage(self,data):
        return data.split(':!')[1][len("say: "):]
    def say(self,data):
        self.sendmsg(self.channel, data)
    def sayName(self):
        self.sendmsg(self.channel, "Hello everyone! I am Artie.")
    def master(self):
        self.sendmsg(self.channel,"Hello there! Duality is my Master.")
    def fourthyTwo(self):
        self.sendmsg(self.channel, 'Douglas Adams - "42 is a nice number that you can take home and introduce to your family."')
    def quit(self):
        self.log.close()
        self.quoteSys.close()
        sys.exit(1)
    
    
    
    
    
    
