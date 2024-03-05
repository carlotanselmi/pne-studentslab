from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.40"
PORT = 8081

s = Seq()
c = Client(IP, PORT)
s.read_fasta('Genome Sequences/U5.fa')

print("To server: Sending U5 Gene to the server...")
print("From server:", c.talk("To server: Sending U5 Gene to the server..."))
print("To server:", str(s))
print("From server:", c.talk(str(s)))




