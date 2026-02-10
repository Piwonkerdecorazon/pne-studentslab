sequence = input("Introduce the DNA sequence: ")
length = len(sequence)
print("Total length of the sequence: " + str(length))

adenosine = 0
guanine = 0
thymine = 0
cytosine = 0
for i in range (0, length):
    if sequence[i] == 'A':
        adenosine+= 1
    elif sequence[i] == 'G':
        guanine+= 1
    elif sequence[i] == 'C':
        cytosine+= 1
    elif sequence[i] == 'T':
        thymine+= 1

print("A: " + str(adenosine))
print("G: " + str(guanine))
print("C: " + str(cytosine))
print("T: " + str(thymine))
