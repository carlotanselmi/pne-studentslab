from ClientSeq import Client
from Seq1 import Seq

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

print("* Testing PING...")
message = 'PING'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')

print("* Testing GET...")
message = 'GET 2'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')
message = 'GET 4'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')

print("* Testing INFO...")
message = 'INFO ACCTCCTCTCCAGCAATGCCAA'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')

print("* Testing COMP...")
message = 'COMP ACCTCCTCTCCAGCAATGCCAA'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')

print("* Testing REV...")
message = 'REV ACCTCCTCTCCAGCAATGCCAA'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')

print("* Testing GENE...")
s = Seq()
genome = "U5"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')
genome = "ADA"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')
genome = "FRAT1"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')
genome = "FXN"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')
genome = "RNU6_269P"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
# send_msg = c.talk(message)
# print(f'From server: {send_msg}')



