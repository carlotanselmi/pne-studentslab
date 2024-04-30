from Client0 import Client

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)

n = 0
while n < 5:
    message = f'Message {n}'
    print(f'To server: {message}')
    print(f'From server: ECHO: {message}\n')
    send_msg = c.talk(message)
    n += 1
