from Seq1 import Seq

s = Seq()
s.read_fasta("../gene_files/U5.txt")
print("Sequence 1: ( Length: " + str(s.len()), ") ", s)
print("Bases: ", str(s.count()))
print("Rev: ", s.reverse())
print("Comp: ", s.complement())
