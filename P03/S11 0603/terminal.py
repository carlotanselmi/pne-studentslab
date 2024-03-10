from Client0 import Client

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)

message = 'INFO AACCGTA'
print(f'To server: {message}')
send_msg = c.talk(message)
