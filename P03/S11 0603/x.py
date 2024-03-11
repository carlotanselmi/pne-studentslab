print("* Testing GENE...")
s = Seq()
genome = "U5"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}')
genome = "ADA"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}')
genome = "FRAT1"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}')
genome = "FXN"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}')
genome = "RNU6_269P"
s.read_fasta(f'Genome Sequences/{genome}.fa')
message = f'GENE {genome}'
print(f'To server: {message}')
send_msg = c.talk(message)
print(f'From server: {send_msg}')