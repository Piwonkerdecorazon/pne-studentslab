from Seq1 import Seq
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1: ( Length: " + str(s1.len()), ") ", s1)
print("Sequence 1: ( Length: " + str(s2.len()), ") ", s2)
print("Sequence 1: ( Length: " + str(s3.len()), ") ", s3)