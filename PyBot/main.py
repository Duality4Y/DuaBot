from BotBrain import BotBrain
import sys

server = "irc.freenode.net"
channel = "#test1123"
nick = "TestAduaD"
botowner = "Duality"

brain = BotBrain(server,channel,nick,botowner)
brain.connect()

while True:
    data = brain.recieve()
    brain.parseCommand(data);
    if brain.found:
        brain.executeCommand();
        print " >> found command.",brain.command
    print "data >> ",data

sys.exit()