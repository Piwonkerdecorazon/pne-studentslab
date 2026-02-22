from S03.dna_count import count_bases
def count_bases_file(lines):
    total_count = {"A": 0, "G": 0, "C": 0, "T": 0, "Total Bases": 0 }
    numberofsequences = len(lines)
    #use .strip() function to remove spaces and /n characters at the end of a string
    #do not copypaste the code, recall a function
    for j in range (0, numberofsequences):
        length = len(lines[j].strip())
        sequence = lines[j].strip()
        total_count = {k: total_count[k] + count_bases(sequence)[k] for k in total_count}
    return total_count


if __name__ == "__main__":
    file = open("dna.txt", "r")
    file_lines = file.readlines()
    file.close()
    print(count_bases_file(file_lines))
