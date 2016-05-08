import irc
from irc import client

my_nickname = "daytona6752"
channels = "#root-me_challenge"
irc_server = "irc.root-me.org"
port = 6667

client_irc = irc.client.SimpleIRCClient()
client_irc.connection.connect(irc_server, port, my_nickname, channels)

if (client_irc.connection.is_connected()):
    print("youpi!!")

client_irc.connection.whois(irc_server)
print(client_irc.connection.as_nick(my_nickname))
print(client_irc.connection.get_nickname())
print(client_irc.connection.get_server_name)
print(client_irc.connection.info(irc_server))
client_irc.connection.join(channels,my_nickname)
client_irc.connection.privmsg("daytona675","bonjour le monde")