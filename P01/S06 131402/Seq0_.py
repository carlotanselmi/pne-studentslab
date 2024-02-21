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


def seq_len(seq=None):
    seq_dna = seq_read_fasta(seq)
    return len(seq_dna)


# Exercise 4:


def seq_count_base(sequence, base=None):
    dictionary = {"A": 0, "C": 0, "T": 0, "G": 0}
    for e in sequence:
        if e in dictionary:
            dictionary[e] += 1
    return dictionary[base]


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
    final_seq = seq[:n][::-1]
    return final_seq


# Exercise 7:


def seq_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    final_seq = ""
    for e in seq:
        sequence_complement = ''.join([complement[e]])
        final_seq += sequence_complement
    return final_seq


# Exercise 8:


def most_frequent_base(seq):
    sequence = ""
    for line in seq:
        sequence += line.replace("\n", "")
    dictionary = {"A": 0, "C": 0, "T": 0, "G": 0}
    for e in sequence:
        if e in dictionary:
            dictionary[e] += 1
    max_count = max(dictionary.values())
    max_count_bases = [base for base, count in dictionary.items() if count == max_count]
    print("Most frequent base:", max_count_bases)
