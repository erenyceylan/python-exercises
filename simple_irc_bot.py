import socket
import requests

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "chat.freenode.org"
port = 6667
ch = "#8banana"
nick = "bobobobobotshow"
exitcode = "!bye"

ircsock.connect((host,port))
ircsock.send(bytes("USER "+ nick +" "+ nick +" "+ nick +" "+ nick +"\n", "UTF-8"))
ircsock.send(bytes("NICK "+ nick +"\n", "UTF-8"))

def joinchan(chan): # join channel(s).
    ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8"))
    print("Connected")

def ping(): # respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))

def sendmsg(msg, target=ch): # sends messages to the target.
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))

def cat_link_finder(cat_type):
    param = {"site" : "imghp", "tbm" : "isch", "q" : cat_type}
    r = requests.get("https://www.google.com/search", params=param)
    fleft = r.text.find("www")
    fright = r.text.find("&", fleft)
    url = r.text[fleft:fright]
    while url.find("google") != -1 or url.find("youtube") != -1:
        fleft = r.text.find("www", fright)
        fright = r.text.find("&", fleft)
        url = r.text[fleft:fright]
    return url

def main():
  joinchan(ch)
  while True:
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
    if ircmsg.find("PRIVMSG") != -1:
        name = ircmsg.split('!',1)[0][1:]
        message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
        if message.rstrip() == exitcode:
            sendmsg("oh...okay. :'(")
            ircsock.send(bytes("QUIT \n", "UTF-8"))
            return
        elif message.rstrip() == "!hi":
            sendmsg("Hi to you too!")
        elif message.rstrip() == "!who are you":
            sendmsg("I am a bot made by horusr for learning purposes")
        elif "!cat" in message.rstrip():
            arg = message.rstrip()[1:].replace(" ", "+")
            link = cat_link_finder(arg)
            sendmsg(link)
    elif ircmsg.find("PING :") != -1:
        ping()

main()