from Client0 import Client

file_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]

c = Client("127.0.0.1", 8080)
sequence_list = []
for i in range(0,5):
    sequence_list.append(c.talk("GET " + str(i)))
for i in range(0,len(sequence_list)):
    print(c.talk("INFO "+ sequence_list[i]))

print("--Testing the COMP method with the sequence " + sequence_list[1])
print(c.talk("COMP "+ sequence_list[1]))
print("--Testing the REV method method with the sequence " + sequence_list[1])
print(c.talk("REV "+ sequence_list[2]))
for i in range(0,len(file_list)):
    print("Printing the gene " + file_list[i])
    print(c.talk("GENE "+ file_list[i]) + "\n")

