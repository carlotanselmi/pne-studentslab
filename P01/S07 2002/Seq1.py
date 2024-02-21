class Seq:
    def __init__(self, seq=None):
        bases = {'A', 'T', 'G', 'C'}
        dna_seq = ""
        if seq is None:
            print("NULL sequence created")
        else:
            for base in seq:
                if base in bases:
                    dna_seq += base
                    self.seq = seq
            if len(dna_seq) == len(seq):
                print("New sequence created!")
            else:
                self.seq = "ERROR"
                print("ERROR!!")

    def __str__(self, seq=None):
        return self.seq

    def len(self):
        return len(self.seq)


def print_seqs(sequence):
    print(f"Sequence: (Length: {sequence.len()}) {sequence}")


def generate_seqs(sequence):
    return Seq(sequence)


def print_nolength_seq(sequence):
    if sequence is None:
        print(f"Sequence: NULL")
    else:
        print(f"Sequence: {sequence}")

