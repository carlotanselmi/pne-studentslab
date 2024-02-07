# Exercise 1
def seq_ping():
    print("OK")

# Exercise 2
def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()

    first_line = file_contents.find("\n")
    seq_dna = file_contents[first_line:]

    seq = ""
    for line in seq_dna:
        seq += line.replace("\n", "")
    return seq

# Exercise 3
def seq_len(seq):
    sequence = seq_read_fasta(seq)
    print("Total length:", len(sequence))

# Exercise 4:

def seq_count_base(seq, base):
    sequence = seq_read_fasta(seq)
    bases = ["A", "C", "T", "G"]
    for b in sequence:


