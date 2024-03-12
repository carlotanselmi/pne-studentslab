import socket
from Game import NumberGuesser

PORT = 8080
IP = "127.0.0.1"
c = NumberGuesser()

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("GAME server configured!")

while True:

    response = ""
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Number {msg}")
        response = c.guess(msg)
        cs.send(str(response).encode())
        cs.close()
