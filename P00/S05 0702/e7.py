from Seq0 import *
def seq_complement(seq):
    sequence = seq_read_fasta(seq)
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    final_seq = ""
    for e in sequence:
        sequence_complement = ''.join([complement[e]])
        final_seq += sequence_complement
    print(final_seq)
