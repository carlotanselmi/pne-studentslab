class Seq:
    def __init__(self, seq):
        bases = {'A', 'T', 'G', 'C'}
        for base in seq:
            if base in bases:
                self.seq = seq
            else:
                self.seq = "ERROR"

    def __str__(self):
        return self.seq
def print_seqs(seq_list):
    n = 0
    for sequence in seq_list:
        print(f"Sequence {n}: (Length: {len(str(sequence))}) {str(sequence)}")
        n += 1

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)