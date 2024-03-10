from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.84"  # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# Testing the talk() method.
# The client should send a message to the server and print the response from the server:
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")