from pathlib import Path

# -- Constant with the name of the file to open
FILENAME = "Genome Sequences/RNU6_269P.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)
