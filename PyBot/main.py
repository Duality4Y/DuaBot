from ircBot import ircBot
import sys

server = "irc.freenode.net"
channel = "#test1123"
nick = "TestAduaD"
botowner = "Duality"

Aduad = ircBot(server,channel,nick,botowner)
Aduad.connect()

while True:
    data = Aduad.recieve()

sys.exit()