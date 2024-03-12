with open('dna.txt', 'r') as dna:

    seq = ""
    for line in dna:
        seq += line.replace("\n", "")

    print("Total length:", len(seq))

    dictionary = {"A": 0, "C": 0, "T": 0, "G": 0}
    for e in seq:
        if e in dictionary:
            dictionary[e] += 1

    print(dictionary)
