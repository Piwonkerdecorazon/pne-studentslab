import socket
import random

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []


    def guess(self, number):
        self.attempts.append(number)
        if number > self.secret_number:
            return "Too high"
        elif number < self.secret_number:
            return "Too low"
        else:
            return "You got it! Won in " + str(len(self.attempts)) + " attempts"


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
print("Game server is configured!")
game = NumberGuesser()


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
        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        # -- Print the received message
        print(f"Message received: {msg}")
        message_words = msg.strip().split(" ")
        user_number = message_words[0]
        if int(user_number) == 0:
            response = "Game finished!"
        else:
            response = str(game.guess(int(user_number)))

        # -- Send a response message to the client
        response += "\n"
        print(response)
        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

