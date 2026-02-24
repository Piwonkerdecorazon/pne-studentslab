from Sq0 import seq_complement
from Sq0 import seq_read_fasta

# Exercise 7
print("\n-----| Exercise 7 |------")
print("DNA file: U5.txt")
print("First 20 bases: ", seq_read_fasta("U5.txt")[0:20])
print("Complement: ", seq_complement(seq_read_fasta("U5.txt")[0:20]))