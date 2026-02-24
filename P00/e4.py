from Sq0 import seq_count_base
from Sq0 import seq_read_fasta
#Exercise 4
genes = ["U5", "ADA", "FRAT1", "FXN"]
print("\n-----| Exercise 4 |------")
for i in range (0, len(genes)):
    print(genes[i])
    print("A: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'A')))
    print("C: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'C')))
    print("T: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'T')))
    print("G: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'G')))