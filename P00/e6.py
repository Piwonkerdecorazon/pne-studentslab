from Sq0 import seq_reverse
from Sq0 import seq_read_fasta
#Exercise 6
print("\n-----| Exercise 6 |------")
print("DNA file: U5.txt")
print("First 20 bases: ", seq_read_fasta("U5.txt")[0:20])
print("Reversed: ", seq_reverse(seq_read_fasta("U5.txt")[0:20]))