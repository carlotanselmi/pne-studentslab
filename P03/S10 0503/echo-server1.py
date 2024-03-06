import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"  # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# Create infinite loop:
while True:
    # In order to let the server finish in a more elegant way,
    # we will add a try-except-else block in the main server's loop:

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

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it into a human-readable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Received Message: {msg}")

        # -- Send a response message to the client
        response = f"ECHO: {msg}"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the socket
        cs.close()


#  TO TEST WRITE IN TERMINAL:
#  echo "Test1..." | nc 127.0.0.1 8080
#  echo "Test2..." | nc 127.0.0.1 8080
#  echo "Test3..." | nc 127.0.0.1 8080
