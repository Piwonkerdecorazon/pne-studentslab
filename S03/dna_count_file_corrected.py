from S03.dna_count import count_bases
file = open("dna.txt", "r")
lines = file.readlines()
file.close()
numberofsequences = len(lines)
totalCount = {"A": 0, "G": 0, "C": 0, "T": 0, "Total Bases": 0 }
#use .strip() function to remove spaces and /n characters at the end of a string
#do not copypaste the code, recall a function
for j in range (0, numberofsequences):
    length = len(lines[j].strip())
    sequence = lines[j].strip()
    totalCount = {k: totalCount[k] + count_bases(sequence)[k] for k in totalCount}

print(totalCount)