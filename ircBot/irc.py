import socket

class irc:
    """(server,channel,nick) for initialization."""
    def __init__(self, server, channel, nick, owner,password, port=6667):
        self.server = server
        self.channel = channel
        self.nick = nick
        self.owner = owner
	self.password = password
        self.port = port
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    """used for keeping the bot in the air"""
    def ping(self):
        self.ircsock.send("PONG :Pong\n")
    """used to send a msg to a chat channel"""
    def sendmsg(self,chan, msg):
        self.ircsock.send("PRIVMSG "+chan+" :"+msg+"\n")
    """used to send a priv msg to a user"""
    def Privmsg(self,_nick, msg):
        self.ircsock.send(":"+_nick+" PRIVMSG "+_nick+" :"+msg+"\n")
    """used to join a channel"""
    def joinchan(self,chan):
        self.ircsock.send("JOIN "+chan+"\n")
    """used to leave a channel"""
    def leavechan(self,chan):
        self.ircsock.send("PART "+chan+"\n");
    """used to connect to a chat channel"""
    def connect(self):
        self.ircsock.connect((self.server, 6667))
        self.ircsock.send("USER "+self.nick+" "+self.nick+" "+self.nick+" :funBot\n")
        self.ircsock.send("NICK "+self.nick+"\n")
        self.joinchan(self.channel)
    """used to get a username from raw irc input data."""
    def getUserName(self,data):
        return data.split('~')[0][1:-1]  #extract nick
    """used to get chat en irc data i the first place."""
    def recieve(self):
        data = self.ircsock.recv(2048)
        data = data.strip('\n\r')
        return data
    """Quiting irc and leaving the propper way."""
    def ircQuit(self,message):
        self.ircsock.send("QUIT :"+message+"\n")
    """Change your nick"""
    def changeNick(self,nick):
        self.ircsock.send("NICK :"+nick+"\n")
