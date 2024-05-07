def seq_reverse(seq_dna, n):
    final_seq = seq_dna[:n][::-1]
    return final_seq


def seq_complement(seq_dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    final_seq = ""
    for e in seq_dna:
        sequence_complement = ''.join([complement[e]])
        final_seq += sequence_complement
    return final_seq[:20]


def seq_len(seq_dna):
    return len(seq_dna)


def seq_count_base(seq_dna, base):
    dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
    for e in seq_dna:
        if e == base:
            if e in dictionary:
                dictionary[e] += 1
    return dictionary[base]
