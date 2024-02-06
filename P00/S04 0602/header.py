from pathlib import Path
FILENAME = "Genome Sequences/RNU6_269P.fa"
file_contents = Path(FILENAME).read_text()

# PF way
first_line = file_contents.find("\n")
seq_dna = file_contents[:first_line]
print(seq_dna)

# OR PNE way
list_contents = file_contents.split("\n")
print(list_contents[0])