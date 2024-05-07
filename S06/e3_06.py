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

    def len(self):
        return len(self.seq)


def print_seqs(seq_list):
    n = 0
    for sequence in seq_list:
        print(f"Sequence {n}: (Length: {sequence.len()}) {sequence}")
        n += 1


def generate_seqs(pattern, number):
    list_of_seq = []
    new_seq = ""
    n = 1
    while n <= number:
        new_seq += pattern
        list_of_seq.append(Seq(new_seq))
        n += 1
    return list_of_seq


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print()
print("List 1:")
print_seqs(seq_list1)
print()
print("List 2:")
print_seqs(seq_list2)
