import http.client
import termcolor
import json


class Seq:
    def __init__(self, seq=None):
        bases = ['A', 'T', 'G', 'C']
        dna_seq = ""
        if seq is None:
            print("NULL sequence created")
            self.seq = "NULL"
        else:
            for base in seq:
                if base in bases:
                    dna_seq += base
            if len(dna_seq) == len(seq):
                print("NEW sequence created")
                self.seq = seq
            else:
                print("INVALID sequence")
                self.seq = "ERROR"

    def __str__(self):
        return self.seq

    def len(self):
        if self.seq != "ERROR" and self.seq != "NULL":
            return len(self.seq)
        else:
            return 0

    def count_base(self, base):
        dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
        for e in self.seq:
            if e in dictionary:
                dictionary[e] += 1
        return dictionary[base]

    def count(self):
        dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
        for e in self.seq:
            if e in dictionary:
                dictionary[e] += 1
        return dictionary

    def reverse(self):
        if self.seq != "ERROR" and self.seq != "NULL":
            rev_seq = self.seq[::-1]
            return rev_seq
        else:
            return self.seq

    def complement(self):
        if self.seq != "ERROR" and self.seq != "NULL":
            complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            comp_seq = ""
            for e in self.seq:
                sequence_complement = ''.join([complement[e]])
                comp_seq += sequence_complement
            return comp_seq
        else:
            return self.seq

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()

        first_line = file_contents.find("\n")
        seq_dna = file_contents[first_line:]

        seq = ""
        for line in seq_dna:
            seq += line.replace("\n", "")
        self.seq = seq

    def most_frequent_base(self):
        sequence = ""
        for line in self.seq:
            sequence += line.replace("\n", "")
        dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
        for e in sequence:
            if e in dictionary:
                dictionary[e] += 1
        max_count = max(dictionary.values())
        max_count_bases = [base for base, count in dictionary.items() if count == max_count]
        return ' '.join(max_count_bases)


gene_name = input("Write the gene name: ")

gene = ['FRAT1', 'ADA', 'FXN', 'RNU6_269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']
id = ['ENSG00000165879', 'ENSG00000196839', 'ENSG00000165060', 'ENSG00000212379', 'ENSG00000207552', 'ENSG00000228296',
      'ENSG00000227633', 'ENSG00000068078', 'ENSG00000128052', 'ENSG00000145362']
genes = dict(zip(gene, id))

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
ID = f'/{genes.get(gene_name)}'
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + ID + PARAMS

print(f"\nServer: {SERVER}\nURL: {URL}")
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + ID + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")
person = json.loads(data1)

termcolor.cprint('Gene', 'green', force_color=True, end="")
print(": MIR633")
termcolor.cprint('Description', 'green', force_color=True, end="")
print(f': {person["desc"]}')
termcolor.cprint('Bases', 'green', force_color=True, end="")
print(f': {person ["seq"]}')

