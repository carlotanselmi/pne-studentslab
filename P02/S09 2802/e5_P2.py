from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081

s = Seq()
c = Client(IP, PORT)
genome = "FRAT1"
s.read_fasta(f'../Genome Sequences/{genome}.fa')
print(f"Gene {genome}: {s}")

message = f'Sending {genome} Gene fragments to the server...'
print(f'To server: {message}')
send_msg = c.talk(message)

start = 0
end = 10
for i in range(5):  # Does the action 5 times
    f = str(s)[start:end]
    start += 10  # Changes the indexes every 10 positions
    end += 10
    frag = f"Fragment {i + 1}: {f}"
    print(frag)
    response = c.talk(frag)
