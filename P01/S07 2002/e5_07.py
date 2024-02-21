from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")
# Prints
print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(f"A: {s1.count_base('A')}, C: {s1.count_base('C')}, "
      f"T: {s1.count_base('T')}, G: {s1.count_base('G')}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(f"A: {s2.count_base('A')}, C: {s2.count_base('C')}, "
      f"T: {s2.count_base('T')}, G: {s2.count_base('G')}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
print(f"A: {s3.count_base('A')}, C: {s3.count_base('C')}, "
      f"T: {s3.count_base('T')}, G: {s3.count_base('G')}")
