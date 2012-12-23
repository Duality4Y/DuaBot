from ircBot import ircBot
import sys

"""
Why not return a value that is parsed?
Don't know maybe because in this way I 
could keep all the data handling inside this class.
Just to do as little as possible in the main loop.
"""

class BotBrain(ircBot):
    found = False;
    command = "";
    data = "";
    def parseCommand(self,data):
        self.data = data;
        if data.find("PING :")!=-1:
            self.found = True
            self.command = "ping"
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
        if data.find("PRIVMSG "+self.nick)!=-1:
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
            else:
                pass;
                """
                #send = data.split(':',1)[1]
                #print "Pm: "+self.getUserName(data)+" >> ",send
                #self.Privmsg(self.getUserName(data),send)
                """
        else:
            self.found = False
        """a test for something else mend to send back what ever
           was entered in a chat channel not needed in parsing 
           for commands."""
        if data.find("PRIVMSG "+self.channel)!=-1:
            #return ircmsg
            pass
    def executeCommand(self):
        if self.command == "ping":
            self.ping()
            print "ping"
        if self.command == "join":
            self.leaveChan(self.channel)
        if self.command == "say":
            self.say();
        if self.command == "sayname":
            self.sayName();
        if self.command == "quit":
            self.quit();
        if self.command == "master":
            self.master();
        if self.command == "42":
            self.fourthyTwo();
    def leaveChan(self,chan):
        for l in xrange(len(self.data)):
            if self.data[l] == ":":
                chan = self.data
                chan = chan[l+len("!join "):len(self.data)]
                print "chan >> ",chan
                self.leavechan(self.channel)
                self.join(chan)
                self.channel = chan.strip(' ')
    def join(self,chan):
        self.joinchan(chan)
    def say(self):
        chatMsg = self.data.split(':!')[1][len("say: "):]
        self.sendmsg(self.channel, chatMsg)
    def sayName(self):
        self.sendmsg(self.channel, "Hello everyone! I am Artie.")
    def master(self):
        self.sendmsg(self.channel,"Hello there! Duality is my Master.")
    def fourthyTwo(self):
        self.sendmsg(self.channel, 'Douglas Adams - "42 is a nice number that you can take home and introduce to your family."')
    def quit(self):
        sys.exit(1);
    
    
    
    
    
    