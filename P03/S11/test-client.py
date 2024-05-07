from ClientSeq import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------\n")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

print("* Testing PING...\n")
message = 'PING'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')

print("* Testing GET...\n")
message = 'GET 2'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')
message = 'GET 4'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')

print("* Testing INFO...\n")
message = 'INFO ACCTCCTCTCCAGCAATGCCAA'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')

print("* Testing COMP...\n")
message = 'COMP ACCTCCTCTCCAGCAATGCCAA'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')

print("* Testing REV...\n")
message = 'REV ACCTCCTCTCCAGCAATGCCAA'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')

print("* Testing GENE...")
message = 'GENE U5'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')
message = 'GENE ADA'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')
message = 'GENE FRAT1'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')
message = 'GENE FXN'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')
message = 'GENE RNU6_269P'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}\n')
