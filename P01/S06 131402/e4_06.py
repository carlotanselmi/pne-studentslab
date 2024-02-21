import termcolor


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

    def len(self):
        return len(self.seq)


def print_seqs(seq_list, color):
    n = 0
    for sequence in seq_list:
        termcolor.cprint(f"Sequence {n}: (Length: {sequence.len()}) {sequence}", color, force_color=True)
        n += 1


def generate_seqs(pattern, number):
    list_of_seq = []
    new_seq = ""
    n = 1
    while n < number:
        new_seq += pattern
        list_of_seq.append(Seq(new_seq))
        n += 1
    return list_of_seq


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)


termcolor.cprint("List 1:", 'blue', force_color=True)
termcolor.cprint(seq_list1, 'blue', force_color=True)
print()
termcolor.cprint("List 2:", 'green', force_color=True)
termcolor.cprint(seq_list2, 'green', force_color=True)
