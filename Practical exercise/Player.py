from Client0 import Client


c = Client("127.0.0.1", 8080)
sequence_list = []
playing = True
while playing == True:
    guess = input("Introduce a number from 1-100:       (type 0 if you want to stop playing)\n")
    response = c.talk(guess)
    if response == "Game finished!":
        print (response)
        playing = False
    else:
        print (response)
