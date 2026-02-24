class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        bases= ["A", "C", "G", "T"]
        length = len(strbases)
        valid = True
        for j in range(0, length):
            if strbases[j] not in bases:
                valid = False
            elif strbases[j] in bases:
                pass


        if valid == True:
            print("New sequence created!")
        else:
            print("Invalid sequence!")
            self.strbases = "ERROR"


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
def generate_seqs(pattern, number):
    sequences = []
    for i in range(0, number):
        strand = pattern * i
        sequences.append(Seq(strand))
    return sequences
def print_seqs(list):
    for i in range(0, len(list)):
        print("Sequence " + str(i) +
              "(Length: " + str(list[i].len()) +
              ") " + list[i].strbases)



# -- Printing the objects

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
