from pathlib import Path

def seq_ping():
    print("ok")

def seq_read_fasta(filename):
    lines = Path(filename).read_text().splitlines()
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
    for i in range (0, len(seq)):
        if seq[i] in bases:
            seq.replace(seq[i], complements[bases.index(seq[i])], 1)
    return seq
    #complementary_bases = str.maketrans("ATCG", "TAGC") #In the left the original characters and in the right the complements
    #return seq.translate(complementary_bases) #We translate our sequence using our method

print(seq_complement("ACGGT"))
