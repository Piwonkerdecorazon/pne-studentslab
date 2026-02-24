
def seq_ping():
    print("ok")

def seq_read_fasta(filename):
    FOLDER = "C:/Users/pablo/PycharmProjects/pne-studentslab/gene_files/"
    with open(FOLDER + filename, "r") as file:
        lines = file.read().splitlines()
    del lines[0]
    gene = "".join(lines)
    return gene

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    total_count = {"A": 0, "G": 0, "C": 0, "T": 0}
    length = len(seq)
    for j in range(0, length):
        total_count[seq[j]] += 1
    return total_count

def seq_reverse(seq):
    reversed_seq = ""
    for i in range(0, len(seq)):
        reversed_seq += (seq[len(seq) - 1 - i])
    return reversed_seq

def seq_complement(seq):
    bases = ["A", "G", "C", "T"]
    complements = ["T", "C", "G", "A"]
    complement_list = list(seq)
    for i in range (0, len(seq)):
        if seq[i] in bases:
            complement_list[i] = complements[bases.index(seq[i])]
    complement_strand = "".join(complement_list)
    return complement_strand

def seq_most_common_base(seq):
    total_count = {"A": 0, "G": 0, "C": 0, "T": 0}
    length = len(seq)
    most_common = ""
    repetitions = 0
    for j in range(0, length):
        total_count[seq[j]] += 1

    for k in total_count:
        if total_count[k] > repetitions:
            repetitions = total_count[k]
            most_common = k
    return most_common

if __name__ == "__main__":
    #Exercise 1
    print("\n-----| Exercise 1 |------")
    print("Testing the seq_pint() function")
    seq_ping()
    #Exercise 2
    print("\n-----| Exercise 2 |------")
    print("DNA file: U5.txt")
    print("First 20 bases: ", seq_read_fasta("U5.txt")[0:20])
    #Exercise 3
    print("\n-----| Exercise 3 |------")
    genes = ["U5", "ADA", "FRAT1", "FXN"]
    for i in range (0, len(genes)):
        print("Gene ", genes[i], "-> Length: ", seq_len(seq_read_fasta(genes[i] + ".txt")))
    #Exercise 4
    print("\n-----| Exercise 4 |------")
    for i in range (0, len(genes)):
        print(genes[i])
        print("A: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'A')))
        print("C: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'C')))
        print("T: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'T')))
        print("G: " + str(seq_count_base(seq_read_fasta(genes[i] + ".txt"), 'G')))
    #Exercise 5
    print("\n-----| Exercise 5 |------")
    for i in range(0, len(genes)):
        print("Gene ", genes[i], "-> ", seq_count(seq_read_fasta(genes[i] + ".txt")))
    #Exercise 6
    print("\n-----| Exercise 6 |------")
    print("DNA file: U5.txt")
    print("First 20 bases: ", seq_read_fasta("U5.txt")[0:20])
    print("Reversed: ", seq_reverse(seq_read_fasta("U5.txt")[0:20]))

    #Exercise 7
    print("\n-----| Exercise 7 |------")
    print("DNA file: U5.txt")
    print("First 20 bases: ", seq_read_fasta("U5.txt")[0:20])
    print("Complement: ", seq_complement(seq_read_fasta("U5.txt")[0:20]))

    #Exercise 8
    print("\n-----| Exercise 8 |------")
    print(seq_most_common_base("TAA"))
    for i in range(0, len(genes)):
        print("Gene ", genes[i], "-> ", "Most common base is: ", seq_most_common_base(seq_read_fasta(genes[i] + ".txt")))