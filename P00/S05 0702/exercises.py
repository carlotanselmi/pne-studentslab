from Seq0 import *

# Exercise 1:

print("----EXERCISE 1----")
# Asterisk to import everything from another file
# Testing the seq_ping() function:
seq_ping()

# Exercise 2:

print("\n----EXERCISE 2----")
seq_read_fasta = seq_read_fasta("../Genome Sequences/U5.fa")
print(seq_read_fasta[:21])

# Exercise 3:

print("\n----EXERCISE 3----")
print("Gene U5:", seq_len("../Genome Sequences/U5.fa"))
print("Gene ADA:", seq_len("../Genome Sequences/ADA.fa"))
print("Gene FRAT1:", seq_len("../Genome Sequences/FRAT1.fa"))
print("Gene FXN:", seq_len("../Genome Sequences/FXN.fa"))


# Exercise 4:

print("\n----EXERCISE 4----")
print("Gene U5:")
seq_count_base("../Genome Sequences/U5.fa", "A")
seq_count_base("../Genome Sequences/U5.fa", "C")
seq_count_base("../Genome Sequences/U5.fa", "T")
seq_count_base("../Genome Sequences/U5.fa", "G")
print("Gene ADA:")
seq_count_base("../Genome Sequences/ADA.fa", "A")
seq_count_base("../Genome Sequences/ADA.fa", "C")
seq_count_base("../Genome Sequences/ADA.fa", "T")
seq_count_base("../Genome Sequences/ADA.fa", "G")
print("Gene FRAT1:")
seq_count_base("../Genome Sequences/FRAT1.fa", "A")
seq_count_base("../Genome Sequences/FRAT1.fa", "C")
seq_count_base("../Genome Sequences/FRAT1.fa", "T")
seq_count_base("../Genome Sequences/FRAT1.fa", "G")
print("Gene FXN:")
seq_count_base("../Genome Sequences/FXN.fa", "A")
seq_count_base("../Genome Sequences/FXN.fa", "C")
seq_count_base("../Genome Sequences/FXN.fa", "T")
seq_count_base("../Genome Sequences/FXN.fa", "G")

# Exercise 5:

print("\n----EXERCISE 5----")
print("Gene U5:", seq_count("../Genome Sequences/U5.fa"))
print("Gene ADA:", seq_count("../Genome Sequences/ADA.fa"))
print("Gene FRAT1:", seq_count("../Genome Sequences/FRAT1.fa"))
print("Gene FXN:", seq_count("../Genome Sequences/FXN.fa"))

# Exercise 6:

print("\n---EXERCISE 6---\n")
print("Gene U5:")
seq_reverse("../Genome Sequences/U5.fa", 20)
print("Gene ADA:")
seq_reverse("../Genome Sequences/ADA.fa", 20)
print("Gene FRAT1:")
seq_reverse("../Genome Sequences/FRAT1.fa", 20)
print("Gene FXN:")
seq_reverse("../Genome Sequences/FXN.fa", 20)

# Exercise 7:

print("\n---EXERCISE 7---\n")
print("Gene U5:")
seq_complement("../Genome Sequences/U5.fa")
print("Gene ADA:")
seq_complement("../Genome Sequences/ADA.fa")
print("Gene FRAT1:")
seq_complement("../Genome Sequences/FRAT1.fa")
print("Gene FXN:")
seq_complement("../Genome Sequences/FXN.fa")

# Exercise 8:

print("\n---EXERCISE 8---\n")
print("Gene U5:")
most_frequent_base("../Genome Sequences/U5.fa")
print("Gene ADA:")
most_frequent_base("../Genome Sequences/ADA.fa")
print("Gene FRAT1:")
most_frequent_base("../Genome Sequences/FRAT1.fa")
print("Gene FXN:")
most_frequent_base("../Genome Sequences/FXN.fa")