def info(seq):
    length = len(seq)
    print(f"Sequence: {seq}\nTotal length: {length}")
    dictionary = {"A": 0, "T": 0, "C": 0, "G": 0}
    for e in seq:
        if e in dictionary:
            dictionary[e] += 1
    percentages = {}
    for base, count in dictionary.items():
        percentages[base] = (count / length) * 100
        print(f"{base}: {count} ({percentages[base]}%)")


info("ACGTT")

