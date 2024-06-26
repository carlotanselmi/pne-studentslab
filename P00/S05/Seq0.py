# Exercise 1:

def seq_ping():
    print("OK")


# Exercise 2:

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()

    first_line = file_contents.find("\n")
    seq_dna = file_contents[first_line:]

    seq = ""
    for line in seq_dna:
        seq += line.replace("\n", "")
    return seq


# Exercise 3:

def seq_len(seq):
    seq_dna = seq_read_fasta(seq)
    return len(seq_dna)


# Exercise 4:

def seq_count_base(seq, base):
    seq_dna = seq_read_fasta(seq)
    dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
    for e in seq_dna:
        for b in base:
            if e == b:
                if e in dictionary:
                    dictionary[e] += 1
    for key, value in dictionary.items():
        print(f"{key}: {value}")


# Exercise 5:

def seq_count(seq):
    seq_dna = seq_read_fasta(seq)
    sequence = ""
    for line in seq_dna:
        sequence += line.replace("\n", "")
    dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
    for e in sequence:
        if e in dictionary:
            dictionary[e] += 1
    return dictionary


# Exercise 6:

def seq_reverse(seq, n):
    seq_dna = seq_read_fasta(seq)
    final_seq = seq_dna[:n][::-1]
    print("Fragment:", seq_dna[:n], "\nReverse:", final_seq)


# Exercise 7:

def seq_complement(seq):
    seq_dna = seq_read_fasta(seq)
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    final_seq = ""
    for e in seq_dna:
        sequence_complement = ''.join([complement[e]])
        final_seq += sequence_complement
    print("Fragment:", seq_dna[:20], "\nComplement:", final_seq[:20])


# Exercise 8:

def most_frequent_base(seq):
    sequence = ""
    for line in seq:
        sequence += line.replace("\n", "")
    dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
    for e in sequence:
        if e in dictionary:
            dictionary[e] += 1
    max_count = max(dictionary.values())
    max_count_bases = [base for base, count in dictionary.items() if count == max_count]
    print("Most frequent base:", max_count_bases)
