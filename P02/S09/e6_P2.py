from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT1 = 8081
PORT2 = 8082

s = Seq()
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
genome = "FRAT1"
s.read_fasta(f'../Genome Sequences/{genome}.fa')
print(f"Gene {genome}: {s}")

message = f'Sending {genome} Gene fragments to the server...'
print(f'To server: {message}')
send_msg1 = c1.talk(message)
send_msg2 = c2.talk(message)

start = 0
end = 10
for i in range(10):
    f = str(s)[start:end]
    start += 10
    end += 10
    frag = f"Fragment {i + 1}: {f}"
    print(frag)
    if (i + 1) % 2 == 0:
        response = c2.talk(frag)
    else:
        response = c1.talk(frag)
