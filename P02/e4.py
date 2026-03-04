from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 3

s = Seq()
sequence_list = []
file_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for i in file_list:
    filename = "../gene_files/" + i + ".txt"
    s.read_fasta(filename)
    sequence_list.append(s.strbases)

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.88" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)
for i in file_list:
    print("To server: ", "Sending " + i + " gene to the server...")
    response = c.talk("Sending " + i + " gene to the server...")
    print("From server: ", f"Response: {response}")
    print("To server: ", sequence_list[file_list.index(i)])
    response = c.talk(sequence_list[file_list.index(i)])
    print("From server: ", f"Response: {response}")
#Exercise
