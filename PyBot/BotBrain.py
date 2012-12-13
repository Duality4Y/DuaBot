from ircBot import ircBot

class BotBrain(ircBot):
    def parseCommand(self,data):
        if data.find("PING :")!=-1:
            return "ping"
        if data.find("PRIVMSG "+self.nick)!=-1:
            if data.find(":!")!=-1:
                if data.find("join ")!=-1:
                    return "join"
                elif data.find("quit")!=-1:
                    return "quit"
                elif data.find("master")!=-1:
                    return "master"
                elif data.find("say name")!=-1:
                    return "sayname"
                elif data.find("say: ")!= -1:
                    return "say"
                elif data.find("42")!= -1:
                    return "42"
            else:
                send = data.split(' : ',1)[1]
                print "Pm: "+self.getUserName(data)+" >> ",send
                self.Privmsg(self.getUserName(data),send)
        """a test for something else mend to send back what ever
           was entered in a chat channel not needed in parsing 
           for commands."""
        if data.find("PRIVMSG "+self.channel)!=-1:
            #return ircmsg
            pass