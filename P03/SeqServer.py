import socket
from Seq1 import Seq

""""Server setup code"""
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")


while True:
    # -- Waits for a client to connect
    print("--[Waiting for Clients to connect]--")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("--[A client has connected to the server!]--\n")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)
        response = ""
        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        sequence_list = ["ACTGACTGACTGACTGACTG","CTGACTGACTGACTGACTGA", "TGACTGACTGACTGACTGAC", "GACTGACTGACTGACTGACT","GGGGACTGACTGACTGACTG"]
        # -- Print the received message
        print(f"Message received: {msg}")
        message_words = msg.strip().split(" ")
        if message_words[0] == "PING":
            print("PING command received")
            response = "OK!"
        elif message_words[0] == "GET":
            print("GET command received")
            response = sequence_list[int(message_words[1])]
        elif message_words[0] == "INFO":
            print("INFO command received")
            sequence = Seq(message_words[1])
            sequence_info = sequence.count()
            totalBases = 0
            for i in sequence_info:
                totalBases += sequence_info[i]
            response += "Sequence: " + message_words[1] + "\n" + "Total Bases: " + str(totalBases) + "\n"
            print(f"Sequence: " + str(sequence))
            for i in sequence_info:
                response += i + "(" + str(sequence_info[i]/totalBases * 100) + "%)" +"\n"
        elif message_words[0] == "COMP":
            print("COMP command received")
            sequence = Seq(message_words[1])
            response = sequence.complement()
        elif message_words[0] == "REV":
            print("REV command received")
            sequence = Seq(message_words[1])
            response = sequence.reverse()
        elif message_words[0] == "GENE":
            print("GENE command received")
            sequence = Seq()
            sequence.read_fasta("../gene_files/" + message_words[1] + ".txt")
            response = str(sequence)

        # -- Send a response message to the client
        response += "\n"
        print(response)
        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

