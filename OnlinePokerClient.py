import websocket
import json

serverURL = input("What Server Should I connect to (with port)?: ")
socket = websocket.create_connection("ws://" + serverURL)

while True:
    data = socket.recv()
    if data[-1] == "p":
        print(data[:-1])
    else:
        sending = input(data)
        socket.send(sending)
