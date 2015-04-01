from willie.module import *
from threading import Timer

timeout = {}
attempt = {}
@willie.module.event('JOIN')
@willie.module.rule('.*') #needs to be here
def kickNoAuth(bot, trigger):
    if 'gamesurge' in trigger.hostmask:
        print 'a-o-k ' + trigger.nick
    else:
        if not attempt[trigger.hostmask]:
            threading.Timer(900, expire, trigger.hostmask)
            addattempt(trigger.hostmask)
            bot.msg('Chanserv', trigger.sender + ' KICK ' + trigger.nick + ' Registration in this channel is required. Follow these instructions http://pastebin.com/p9WjjTnK to register for Gamesurge. Join back once you have registered! (Join attempt 1/3)')
        if attempt[trigger.hostmask] == 2:
            threading.Timer(900, expire, trigger.hostmask)
            addattempt(trigger.hostmask)
            bot.msg('Chanserv', trigger.sender + ' KICK ' + trigger.nick + ' Registration in this channel is required. Follow these instructions http://pastebin.com/p9WjjTnK to register for Gamesurge. Join back once you have registered! (Join attempt 2/3)')
        if attempt[trigger.hostmask] == 3:
            threading.Timer(1, expire, trigger.hostmask)
            bot.msg('Chanserv', trigger.sender + ' tb ' + trigger.nick + ' 2h You have reached Join attempt 3/3. You will be temporarily banned for 2 hours.')

def addattempt(hostmask):
    if not attempt[hostmask]:
        attempt[hostmask] = 1
    if attempt[hostmask] == 3:
        print "i just can't!"
    else:
        attempt[hostmask] +=1
        
def expire(hostmask):
    timeout[hostmask] = False
    
