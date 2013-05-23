from Brain import BotBrain
import sys

class Configs(object):
    config = {}
    def __init__(self,source):
        configFile = open(source,'r')
        for line in configFile:
            line = line.strip('\n')
            self.config[line.split(" = ")[0]] = line.split(" = ")[1]
        configFile.close()
    def Config(self):
        return self.config

def main(argv):
    
    #init configuration reading.
    config = Configs("config.txt")
    BotConf = config.Config()
    
    #load configurations
    server = BotConf["server"]
    channel = BotConf["channel"]
    nick = BotConf["nick"]
    botowner = BotConf["owner"]
    password = BotConf["password"]
    
    #delete config "cache"
    del BotConf
    del config
    
    #print configuration to be sure.
    #print "Server: %s, Channel: %s, Nick: %s, Owner: %s, Password: %s" %(server,channel,nick,botowner,password)
    
    brain = BotBrain(server,channel,nick,botowner,password)
    brain.connect()
    
    while True:
        data = brain.recieve()
        brain.parseCommand(data)
        if brain.found:
            brain.executeCommand()
            brain.logging(" >> found command."+brain.command)
        brain.logging("data >> "+data)
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
