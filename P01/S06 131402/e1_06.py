class Seq:
    def __init__(self, seq):
        bases = {'A', 'T', 'G', 'C'}
        dna_seq = ""
        for base in seq:
            if base in bases:
                dna_seq += base
                self.seq = seq
        if len(dna_seq) == len(seq):
            print("New sequence created!")
        else:
            self.seq = "ERROR"
            print("ERROR!!")

    def __str__(self):
        return self.seq


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
