from Sq0 import seq_len
from Sq0 import seq_read_fasta
#Exercise 3
print("\n-----| Exercise 3 |------")
genes = ["U5", "ADA", "FRAT1", "FXN"]
for i in range (0, len(genes)):
    print("Gene ", genes[i], "-> Length: ", seq_len(seq_read_fasta(genes[i] + ".txt")))