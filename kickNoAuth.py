from willie.module import *
from threading import Timer

attempt = {}

@willie.module.event('JOIN')
@willie.module.rule('.*') #needs to be here
def kickNoAuth(bot, trigger):
    if 'gamesurge' in trigger.hostmask:
        print 'a-o-k ' + trigger.hostmask
        return
    elif 'TTSocial' in trigger.hostmask:
        print 'a-o-k ' + trigger.hostmask
        return
    else:
        if trigger.hostmask not in attempt:
            Timer(900, expire, trigger.hostmask)
            attempt[trigger.hostmask] = 1
            bot.msg('Chanserv', trigger.sender + ' KICK ' + trigger.nick + ' Registration is required. Follow these instructions http://pastebin.com/p9WjjTnK to register for Gamesurge. Join back once registered! (Join attempt 1/3')
        elif attempt[trigger.hostmask] == 0:
            Timer(900, expire, trigger.hostmask)
            attempt[trigger.hostmask] = 1
            bot.msg('Chanserv', trigger.sender + ' KICK ' + trigger.nick + ' Registration is required. Follow these instructions http://pastebin.com/p9WjjTnK to register for Gamesurge. Join back once registered! (Join attempt 1/3')
        elif attempt[trigger.hostmask] == 1:
            Timer(900, expire, trigger.hostmask)
            attempt[trigger.hostmask] = 2
            bot.msg('Chanserv', trigger.sender + ' KICK ' + trigger.nick + ' Registration is required. Follow these instructions http://pastebin.com/p9WjjTnK to register for Gamesurge. Join back once registered! (Join attempt 2/3')
        elif attempt[trigger.hostmask] == 2:
            Timer(1, expire, trigger.hostmask)
            bot.msg('Chanserv', trigger.sender + ' tb ' + trigger.nick + ' 30m You have reached Join attempt 3/3 without being registered. You will be temporarily banned for 30 minutes.')
        else:
            bot.msg('The_Judge', '88')

def expire(hostmask):
    attempt[trigger.hostmask] = 0
