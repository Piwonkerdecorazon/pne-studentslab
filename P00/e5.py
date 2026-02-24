from Sq0 import seq_count
from Sq0 import seq_read_fasta
#Exercise 5
genes = ["U5", "ADA", "FRAT1", "FXN"]
print("\n-----| Exercise 5 |------")
for i in range(0, len(genes)):
    print("Gene ", genes[i], "-> ", seq_count(seq_read_fasta(genes[i] + ".txt")))