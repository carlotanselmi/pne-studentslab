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
            for b in base:
                if e == b:
                    if e in dictionary:
                        dictionary[e] += 1
        for key, value in dictionary.items():
            percentage = round((value/len(self.seq)) * 100, 1)
            print(f"{key}: {value}  ({percentage})%")

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


genes = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379',
         'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633',
         'FGFR3': 'ENSG00000068078', 'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362'}

for key, value in genes.items():
    gene_name = key

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
    print(f": {gene_name}")
    termcolor.cprint('Description', 'green', force_color=True, end="")
    print(f': {person["desc"]}')
    sequence = person["seq"]
    sequence = Seq(sequence)
    termcolor.cprint('Total length', 'green', force_color=True, end="")
    print(f": {sequence.len()}")
    bases = ["A", "C", "G", "T"]
    sequence.count_base(bases)
    termcolor.cprint('Most frequent base', 'green', force_color=True, end="")
    print(f": {sequence.most_frequent_base()}")
