import socket
import random


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def ping(self):
        print("OK!\n")

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
        dna_sequences = ["AAGCCTCGAGTCGAGACTGC", "GCTAGCTAGCGGTGGCATCG", "CGGGTAGCTCCGGACTAGCA", "TCGATCGATCGAGGTCGAGC"]
        print(dna_sequences[number])

    def info(self, seq):
        length = len(seq)
        print(f"Sequence: {seq}\nTotal length: {length}")
        dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
        for e in seq:
            if e in dictionary:
                dictionary[e] += 1
        percentages = {}
        for base, count in dictionary.items():
            percentages[base] = (count / length) * 100
            print(f"{base}: {count} ({percentages[base]}%)")
