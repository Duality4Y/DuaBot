from ircBot import ircBot

class BotBrain(ircBot):
    found = False;
    command = "";
    def parseCommand(self,data):
        if data.find("PING :")!=-1:
            self.found = True
            self.command = "ping"
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
                self.found = False
                """
                #send = data.split(':',1)[1]
                #print "Pm: "+self.getUserName(data)+" >> ",send
                #self.Privmsg(self.getUserName(data),send)
                """
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
    def join(self):
        pass