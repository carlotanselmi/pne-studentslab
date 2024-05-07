import socket


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def ping(self):
        return "OK!"

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

    def get(self, number):
        dna_sequences = ["AAGCCTCGAGTCGAGACTGC", "GCTAGCTAGCGGTGGCATCG", "CGGGTAGCTCCGGACTAGCA",
                         "TCGATCGATCGAGGTCGAGC", "CACACAGTGACAGTCGTACG"]
        return dna_sequences[number]

    def info(self, seq):
        length = len(seq)
        info_string = f"Sequence: {seq}\nTotal length: {length}\n"
        dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}

        for e in seq:
            if e in dictionary:
                dictionary[e] += 1
        percentages = {}

        for base, count in dictionary.items():
            percentages[base] = (count / length) * 100
            info_string += f"{base}: {count} ({percentages[base]:.2f}%)"
        return info_string

    def comp(self, seq):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp_seq = ""

        for e in seq:
            sequence_complement = ''.join([complement[e]])
            comp_seq += sequence_complement
        return comp_seq

    def rev(self, seq):
        rev_seq = seq[::-1]
        return rev_seq

    def gene(self, filename):
        from pathlib import Path
        filename = f'../Genome Sequences/{filename}.fa'
        file_contents = Path(filename).read_text()

        first_line = file_contents.find("\n")
        seq_dna = file_contents[first_line:]

        seq = ""
        for line in seq_dna:
            seq += line.replace("\n", "")
        return seq

