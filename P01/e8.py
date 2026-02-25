from Seq1 import Seq
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1: ( Length: " + str(s1.len()), ") ", s1)
print("Bases: ", str(s1.count()))
print("Rev: ", s1.reverse())
print("Comp: ", s1.complement())
print("Sequence 2: ( Length: " + str(s2.len()), ") ", s2)
print("Bases: ", str(s2.count()))
print("Rev: ", s2.reverse())
print("Comp: ", s2.complement())
print("Sequence 3: ( Length: " + str(s3.len()), ") ", s3)
print("Bases: ", str(s3.count()))
print("Rev: ", s3.reverse())
print("Comp: ", s3.complement())

