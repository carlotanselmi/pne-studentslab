from Seq0 import *
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
