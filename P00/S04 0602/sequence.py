from pathlib import Path
FILENAME = "Genome Sequences/ADA.fa"
file_contents = Path(FILENAME).read_text()

first_line = file_contents.find("\n")
seq_dna = file_contents[first_line:]

seq = ""
for line in seq_dna:
    seq += line.replace("\n", "")
print("Total length:", len(seq))

# Print lists together: print(len(''.join(list_contents)))
# Get rid of the 1st line: list_contents.pop(0)