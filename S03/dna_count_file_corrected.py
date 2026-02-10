file = open("dna.txt", "r")
lines = file.readlines()
file.close()

numberofsequences = len(lines)
adenosine = 0
guanine = 0
thymine = 0
cytosine = 0
totalBases = 0
#use .strip() function to remove spaces and /n characters at the end of a string
#do not copypaste the code, recall a function
for j in range (0, numberofsequences):
    length = len(lines[j].strip())
    sequence = lines[j].strip()
    for i in range (0, length):
        if sequence[i] == 'A':
            adenosine+= 1
        elif sequence[i] == 'G':
            guanine+= 1
        elif sequence[i] == 'C':
            cytosine+= 1
        elif sequence[i] == 'T':
            thymine+= 1
        totalBases += 1
print (lines)
print("The total number of bases is " + str(totalBases))
print("A: " + str(adenosine))
print("G: " + str(guanine))
print("C: " + str(cytosine))
print("T: " + str(thymine))