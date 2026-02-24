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
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
def print_seqs(list):
    for i in range(0, len(list)):
        print("Sequence " + str(i) +
              "(Length: " + str(list[i].len()) +
              ") " + list[i].strbases)
# -- Printing the objects
print_seqs(seq_list)
