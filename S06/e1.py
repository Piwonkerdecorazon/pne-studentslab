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
s1 = Seq("AGTACrACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")
