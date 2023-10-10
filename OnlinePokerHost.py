import random
from websock import *
from threading import *
from Cards import *
deck = Deck()
playerList = []
currentBet = 0
sockets = []
Data = None
waiter = Condition()
def getData():
    waiter.acquire()
    waiter.wait()
    waiter.release()
    return Data[0]
def Bet():
    global sockets
    global currentBet
    logbet = -1
    while currentBet>logbet:
        i = 1
        while i <= len(playerList):
            logbet = currentBet
            s = sockets[i-1]
            server.send(s, playerList[i-1].name + ", your cards:" + str(playerList[i-1].dispHand()) + "p")
            server.send(s, playerList[i-1].name + ": raise, call or fold? Current bet: " + str(currentBet))
            rorc = getData()
            match rorc:
                case "raise":
                    server.send(s,"How much do you want to raise by?")
                    r = float(getData())
                    if r > 0:
                        currentBet += r
                    else:
                        print("invalid. called.")
                    i+=1
                case "call":
                    i+=1
                case "fold":
                    playerList.remove(playerList[i-1])
                    if len(playerList) == 1:
                        for socket in sockets:
                            server.send(socket, playerList[0].name + " Wins! Winnings: " + str(currentBet) + "p")
                        return False
                    i+=1
                case _:
                    continue
    return True
def Poker():
    global deck
    global sockets
    deck = Deck()
    print("ran")
    waitPlayers = True
    for i in range(20):
        deck.shuffle()
    for s in sockets:
        server.send(s, "What's your name?")
        response = getData()
        playerList.append(Player(response))
        print(response)
    for i in playerList:
        i.draw(deck, 2)
    if not Bet():
        return
    hRaw = deck.draw(3)
    h = []
    for i in hRaw:
        h.append(i.name)
    for s in sockets:
        server.send(s, "House cards:" + str(h) + "p")
    if not Bet():
        return
    for i in range(2):
        n = deck.draw()[0]
        hRaw.append(n)
        h.append(n.name)
        for s in sockets:
            server.send(s, "House cards:" + str(h) + "p")
        if not Bet():
            return
    for s in sockets:
        server.send(s, "FINAL REVEAL" + "p")
        server.send(s, "____________________________________" + "p")
        server.send(s, "House cards:" + str(h) + "p")
        for i in playerList:
            server.send(s, i.name + ", your cards:" + str(i.dispHand()))
poker = Thread(target = Poker)
def starterThread():
    if input("start game?") != "no":
        poker.start()
        return
startThread = Thread(target = starterThread)
startThread.start()
def on_data_receive(client, data):
    global Data
    waiter.acquire()
    Data = [data, client]
    waiter.notify_all()
    waiter.release()
def on_connection_open(client):
    sockets.append(client)
def on_error(exception):
    print(exception)
def on_connection_close(client):
    print(client)
def on_server_destruct():
    print("descrutied")
server = WebSocketServer(
    "0.0.0.0",        # Example host.
    8080,               # Example port.
    on_data_receive     = on_data_receive,
    on_connection_open  = on_connection_open,
    on_error            = on_error,
    on_connection_close = on_connection_close,
    on_server_destruct  = on_server_destruct
)
server_thread = Thread(target=server.serve_forever(), args=(), daemon=True)
server_thread.start()
