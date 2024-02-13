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
def seq_len(seq=None):
    sequence = seq_read_fasta(seq)
    print("Total length:", len(sequence))

# Exercise 4:

def seq_count_base(sequence, base=None):
    seq = seq_read_fasta(sequence)
    genes = ["ADA", "FXN", "U5"]
    bases = ["A", "C", "T", "G"]
    for g in genes:
        for b in bases:
            f = seq + g + ".txt"
            bases = seq.read(f)
            total = seq.read(bases, b)

# Exercise 5:

def seq_count(seq):
    sequence = ""
    for line in seq:
        sequence += line.replace("\n", "")
    dictionary = {"A": 0, "C": 0, "T": 0, "G": 0}
    for e in sequence:
        if e in dictionary:
            dictionary[e] += 1
    print(dictionary)

# Exercise 6:

def seq_reverse(seq, n):
    sequence = seq_read_fasta(seq)
    final_seq = sequence[:n][::-1]
    print(final_seq)

# Exercise 7:

def seq_complement(seq):
    sequence = seq_read_fasta(seq)
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    final_seq = ""
    for e in sequence:
        sequence_complement = ''.join([complement[e]])
        final_seq += sequence_complement
    print(final_seq)
