import socket
from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

flag = True
while flag:

    print("* Guessing...\n")
    message = int(input("Enter a number: "))
    print(f'To server: {message}')
    send_msg = c.talk(message)
    print(f'From server: {send_msg}\n')
    if send_msg.startswith("You"):
        flag = False
