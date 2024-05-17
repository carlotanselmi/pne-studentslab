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
            if e in base and e in dictionary:
                dictionary[e] += 1
        result = []
        seq_length = len(self.seq)
        if seq_length == 0:
            result = ""
        for key, value in dictionary.items():
            percentage = round((value/len(self.seq)) * 100, 1)
            result.append(f"{key}: {value}  ({percentage})%")
        return "<br>".join(result)
