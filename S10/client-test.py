import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.94"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

i=0
client_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()

    print("A client has connected to the server!")
    i+=1
    client_list.append(client_ip_port)
    print("CONNECTION " + str(i) + ": CLIENT IP, PORT: ", client_ip_port)
    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()

    # -- Print the received message
    print(f"Message received: {msg}")

    # -- Send a response message to the client
    response = "ECHO: " + msg + "\n"

    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()
    if i == 5:
        for j in range (0, len(client_list)):
            print("Client: " + str(j+1) + " IP,PORT: " + str(client_list[j]))