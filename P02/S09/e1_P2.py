from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# Preliminary test of the Client Class:
# -- Test the ping method
c.ping()
