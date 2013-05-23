import socket

class irc:
<<<<<<< HEAD
    def __init__(self, server, channel, nick, owner,password, port=6667):
        """(server,channel,nick) for initialization."""
=======
    """(server,channel,nick) for initialization."""
    def __init__(self, server, channel, nick, owner,password, port=6667):
>>>>>>> 7d019e7bdfd21f94d1ed88dd6b3b4e1dbb5e946c
        self.server = server
        self.channel = channel
        self.nick = nick
        self.owner = owner
<<<<<<< HEAD
        self.password = password
        self.port = port
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
=======
	self.password = password
        self.port = port
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    """used for keeping the bot in the air"""
>>>>>>> 7d019e7bdfd21f94d1ed88dd6b3b4e1dbb5e946c
    def ping(self):
	"""used for keeping the bot in the air"""
        self.ircsock.send("PONG :Pong\n")
    
    def sendmsg(self,chan, msg):
	"""used to send a msg to a chat channel"""
        self.ircsock.send("PRIVMSG "+chan+" :"+msg+"\n")
    
    def Privmsg(self,_nick, msg):
	"""used to send a priv msg to a user"""
        self.ircsock.send(":"+_nick+" PRIVMSG "+_nick+" :"+msg+"\n")
    
    def joinchan(self,chan):
	"""used to join a channel"""
        self.ircsock.send("JOIN "+chan+"\n")
    
    def leavechan(self,chan):
        """used to leave a channel"""
        self.ircsock.send("PART "+chan+"\n");
    
    def connect(self):
	"""used to connect to a chat channel"""
        self.ircsock.connect((self.server, self.port))
        self.ircsock.send("USER "+self.nick+" "+self.nick+" "+self.nick+" :funBot\n")
        self.ircsock.send("NICK "+self.nick+"\n")
        self.joinchan(self.channel)
        self.Privmsg("Duality",("Server: %s, Channel: %s, BotNick: %s, BotOwner: %s, Password: %s " 
            %(self.server,self.channel,self.nick,self.owner,self.password)))
    
    def getUserName(self,data):
	"""used to get a username from raw irc input data."""
        return data.split('~')[0][1:-1]  #extract nick
    
    def recieve(self):
	"""used to get chat en irc data i the first place."""
        data = self.ircsock.recv(2048)
        data = data.strip('\n\r')
        return data
    
    def ircQuit(self,message):
	"""Quiting irc and leaving the propper way."""
        self.ircsock.send("QUIT :"+message+"\n")
<<<<<<< HEAD
    
=======
    """Change your nick"""
>>>>>>> 7d019e7bdfd21f94d1ed88dd6b3b4e1dbb5e946c
    def changeNick(self,nick):
	"""Change your nick"""
        self.ircsock.send("NICK :"+nick+"\n")
