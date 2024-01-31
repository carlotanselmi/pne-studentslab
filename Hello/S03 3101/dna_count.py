# Introduce the sequence: CATGTAGACTAG
# Total length: 12
# A: 4
# C: 2
# T: 3
# G: 3

def get_appearances_dna_seq():
    input_seq = input("Enter a DNA sequence:")
    print("Total length:", len(input_seq))
    dictionary = {"A": 0, "C": 0, "T": 0, "G": 0}
    for e in input_seq:
        if e in dictionary:
            dictionary[e] += 1
    return dictionary
print(get_appearances_dna_seq())