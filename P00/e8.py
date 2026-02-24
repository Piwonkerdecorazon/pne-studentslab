from Sq0 import seq_read_fasta
from Sq0 import seq_most_common_base

#Exercise 8
genes = ["U5", "ADA", "FRAT1", "FXN"]
print("\n-----| Exercise 8 |------")
for i in range(0, len(genes)):
    print("Gene ", genes[i], "-> ", "Most common base is: ", seq_most_common_base(seq_read_fasta(genes[i] + ".txt")))