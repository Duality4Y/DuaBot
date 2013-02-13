from Brain import BotBrain
import sys

server = "irc.freenode.net"
channel = "#test1123"
nick = "DuaBot"
botowner = "Duality"

brain = BotBrain(server,channel,nick,botowner)
brain.connect()

while True:
    data = brain.recieve()
    brain.parseCommand(data)
    if brain.found:
        brain.executeCommand()
        brain.logging(" >> found command."+brain.command)
    brain.logging("data >> "+data)
sys.exit(1)
