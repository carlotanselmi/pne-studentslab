from Seq1 import *
print("-----| Practice 1, Exercise 9 |------")
s = Seq()
s.read_fasta("../Genome Sequences/U5.fa")
print(f"Sequence: (Length: {s.len()}) {s}")
print(f"Bases: {s.count()}")
print(f"Reverse: {s.reverse()}")
print(f"Complement: {s.complement()}")
