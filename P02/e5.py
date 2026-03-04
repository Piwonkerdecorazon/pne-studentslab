from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 3

s = Seq()
file_list = ["FRAT1"]
seq_list = []
for i in file_list:
    filename = "../gene_files/" + i + ".txt"
    s.read_fasta(filename)
    sequence = s.strbases[0:100]

for i in range(0,len(sequence), 10):
    seq_list.append(sequence[i:i+10])

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.88" # your IP address
PORT_1 = 8080
PORT_2 = 8081

# -- Create a client object
c1 = Client(IP, PORT_1)
c2 = Client(IP, PORT_2)

print(c1)
print(c2)

for i in file_list:
    print("To server: ", "Sending FRAT1 gene to the server in fragments...")
    response = c1.talk("Sending " + i + " gene to the server...")
    print("From server: ", f"Response: {response}")
    response = c2.talk("Sending " + i + " gene to the server...")
    print("From server: ", f"Response: {response}")
    for i in range (0,len(seq_list)):
        if i % 2 != 0:
            print("To server: ", seq_list[i])
            response = c1.talk(seq_list[i])
            print("From server: ", f"Response: {response}")
        else:
            print("To server: ", seq_list[i])
            response = c2.talk(seq_list[i])
            print("From server: ", f"Response: {response}")

#Exercise