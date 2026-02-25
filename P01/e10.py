from Seq1 import Seq
s = Seq()
file_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for i in file_list:
    filename = "../gene_files/" + i + ".txt"
    s.read_fasta(filename)
    print("Gene: ", i, "Most frequent base: ", s.most_common_base())


