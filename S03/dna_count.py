def count_bases(sequence):
    adenosine = 0
    guanine = 0
    thymine = 0
    cytosine = 0
    totalBases = 0
    for i in range (0, len(sequence)):
        if sequence[i] == 'A':
            adenosine+= 1
        elif sequence[i] == 'G':
            guanine+= 1
        elif sequence[i] == 'C':
            cytosine+= 1
        elif sequence[i] == 'T':
            thymine+= 1
        totalBases+=1
    result = {"A": adenosine, "G": guanine, "C": cytosine, "T": thymine, "Total Bases": totalBases }
    return result



if __name__ == "__main__": #if importing the code, everything in this if is ignored by other programs, so use it to isolate
    sequence = input("Introduce the DNA sequence: ")
    length = len(sequence)
    print("Total length of the sequence: " + str(length))
    print(count_bases(sequence))
