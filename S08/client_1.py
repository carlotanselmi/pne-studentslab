import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the teacher's server
PORT = 8081
IP = "127.0.0.1"  # it depends on the machine the server is running


# First, create the socket
# We will always use these parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be sent, only bytes
# It necessary to encode the string into bytes
s.send(str.encode("Hello there!"))

# Close the socket
s.close()
