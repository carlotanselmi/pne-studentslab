import socket

# SERVER IP, PORT
PORT = 8081
IP = "127.0.0.1"  # depends on the computer the server is running

while True:
    # -- Ask the user for the message
    msg_input = input("Enter your message: ")
    # -- Create the socket
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- Establish the connection to the Server
    ls.connect((IP, PORT))
    # -- Send the user message
    ls.send(str.encode(msg_input))
    # -- Close the socket
    ls.close()
