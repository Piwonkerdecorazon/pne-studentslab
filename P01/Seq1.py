import termcolor
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL SEQUENCE CREATED")
            self.strbases = "NULL"
        else:
            self.strbases = strbases
            bases = ["A", "C", "G", "T"]
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
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count(self):
        total_count = {"A": 0, "G": 0, "C": 0, "T": 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            pass
        else:
            for j in range(0, len(self.strbases)):
                total_count[self.strbases[j]] += 1
        return total_count

    def count_base(self, base):
        return self.strbases.count(base)

    def reverse(self):
        reversed_seq = ""
        if self.strbases == "NULL":
            reversed_seq = "NULL"
        elif self.strbases == "ERROR":
            reversed_seq = "ERROR"
        else:
            for i in range(0, len(self.strbases)):
                reversed_seq += (self.strbases[len(self.strbases) - 1 - i])
        return reversed_seq

    def complement(self):
        bases = ["A", "G", "C", "T"]
        complements = ["T", "C", "G", "A"]
        complement_list = list(self.strbases)
        complement_strand = ""
        if self.strbases == "NULL":
            complement_strand = "NULL"
        elif self.strbases == "ERROR":
            complement_strand = "ERROR"
        else:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] in bases:
                    complement_list[i] = complements[bases.index(self.strbases[i])]
            complement_strand = "".join(complement_list)
        return complement_strand

    def read_fasta(self, filename):
        with open(filename, "r") as file:
            lines = file.read().splitlines()
        del lines[0]
        self.strbases = "".join(lines)

    def most_common_base(self):
        total_count = {"A": 0, "G": 0, "C": 0, "T": 0}
        length = len(self.strbases)
        most_common = ""
        repetitions = 0
        for j in range(0, length):
            total_count[self.strbases[j]] += 1

        for k in total_count:
            if total_count[k] > repetitions:
                repetitions = total_count[k]
                most_common = k
        return most_common

# --- Main program

# -- Printing the objects
