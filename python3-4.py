import irc
from irc import client

query = client.IRC()

daytona675 = query.server().connect('irc.root-me.org',6667,'daytona675')
daytona675.join("#root-me_challenge")
daytona675.send_raw("bonjour")
daytona675.privmsg_many("daytona6752","bonjour")
daytona675.privmsg("daytona6752","test")



toto = query.server().connect('irc.root-me.org',6667,'daytona675')
toto.join("#root-me_challenge")
toto.send_raw("bonjour")
toto.privmsg_many("daytona6752","bonjour")
toto.privmsg("daytona6752","test")
