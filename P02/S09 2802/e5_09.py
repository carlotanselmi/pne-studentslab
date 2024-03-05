from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.40"
PORT = 8081

s = Seq()
c = Client(IP, PORT)
s.read_fasta('Genome Sequences/U5.fa')


