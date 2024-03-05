from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.84"
PORT = 8081

s = Seq()
c = Client(IP, PORT)
genome = "U5"
s.read_fasta(f'Genome Sequences/{genome}.fa')

print(f'To server: Sending {genome} Gene to the server...')
print("From server:", c.talk(f"Sending {genome} Gene to the server..."))
print(f'To server: {s}')
print("From server:", c.talk(str(s)))




