from pathlib import Path
FILENAME = "../Genome Sequences/U5.fa"
file_contents = Path(FILENAME).read_text()

# PF way
first_line = file_contents.find("\n")
seq_dna = file_contents[first_line:]
print(seq_dna)

# PNE way
list_contents = file_contents.split("\n")
for i in range(1, len(list_contents)):
    print(list_contents[i])