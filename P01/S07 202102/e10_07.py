from Seq1 import *
print("-----| Practice 1, Exercise 10 |------")
s = Seq()
s.read_fasta("Genome Sequences/U5.fa")
print("Gene U5: Most frequent Base:", s.most_frequent_base())
s.read_fasta("Genome Sequences/ADA.fa")
print("Gene ADA: Most frequent Base:", s.most_frequent_base())
s.read_fasta("Genome Sequences/FRAT1.fa")
print("Gene FRAT1: Most frequent Base:", s.most_frequent_base())
s.read_fasta("Genome Sequences/FXN.fa")
print("Gene FXN: Most frequent Base:", s.most_frequent_base())
s.read_fasta("Genome Sequences/RNU6_269P.fa")
print("Gene RNU6_269P: Most frequent Base:", s.most_frequent_base())
