import socket
from ClientSeq import Client

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ server configured!")

# Create infinite loop:
while True:
    # In order to let the server finish in a more elegant way,
    # we will add a try-except-else block in the main server's loop:
    response = ""
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:

        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it into a human-readable string
        msg = msg_raw.decode()
        msg = msg.rstrip("\n")
        msg = msg.upper()

        # -- Print the received message
        print(f"{msg} command")

        if msg == 'PING':
            response = c.ping()
            cs.send(str(response).encode())

        elif msg.startswith('GET'):
            number = int(msg.split()[1])
            response = c.get(number)
            cs.send(str(response).encode())

        elif msg.startswith('INFO'):
            sequence = msg.split()[1]
            response = c.info(sequence)
            cs.send(str(response).encode())

        elif msg.startswith('COMP'):
            sequence = msg.split()[1]
            response = c.comp(sequence)
            cs.send(str(response).encode())

        elif msg.startswith('REV'):
            sequence = msg.split()[1]
            response = c.rev(sequence)
            cs.send(str(response).encode())

        elif msg.startswith('GENE'):
            genome_name = msg.split()[1]
            if genome_name in ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']:
                response = c.gene(genome_name)
                cs.send(str(response).encode())
            else:
                print("There is NOT such Genome in the server")

        else:
            print("Error with the command")

        # -- Close the socket
        cs.close()
