import sys

import irc
from irc import client

my_nickname = "daytona675"
channels = "#root-me_challenge"

c =irc.client.ServerConnection(irc.client.Reactor())
c.buffer_class = client.buffer.LineBuffer
c.buffer_class.errors = 'replace'

try:
    b = c.reactor.server().connect("irc.root-me.org",6667,my_nickname,channels)
except irc.client.ServerConnectionError as erreur:
        print("erreur:",erreur)
        sys.exit(1)

b.join("#root-me_challenge")
b.is_connected()
b.privmsg("daytona675","hello")


