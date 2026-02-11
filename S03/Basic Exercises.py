#Exercise 1
def word_properties(word):
    print ("The length " + str(len(word)))
    print ("First 5 " + str(word[0: 5]))
    print("Last 3 " + str(word[len(word) - 3: len(word)]))
    print("Lowercase " + word.lower())
    print("ATC count " + str(word.count("ATC")))
    print("Transcribed " + word.replace("T", "U"))

#Exercise 2
def more_strings(phrase):
    print("Phrase: " + phrase.strip())
    print("Words: " + str(len(phrase.split())))
    print("Capitalized: " + phrase.title())
    print("Starts with Hello: " + str(phrase.strip().startswith("Hello")))
    print("Ends with ing: " + str(phrase.strip().endswith("ing")))
    print("Position of the word Python: " + str(phrase.strip().find("Python")))
    print("Rephrase: " + " - ".join(phrase.strip().split()))

#Exercise 3
def list_exercise(list):
    print("Wednesday: " + str(list[2]))
    print("Max: " + str(max(list)))
    print("Min: " + str(min(list)))
    print("AVG: " + str((round(sum(list)/len(list)), 1)))
    days = 0
    for i in range (0, len(list)):
        if list[i] >= 17:
            days += 1
    print("Days above 17: " + str(days))
    print("Sorted: " + str(sorted(list)))

#Exercise 4
def grade(number):
    if number >= 9:
        print(str(number) + "-> A")
    elif number >= 7:
        print(str(number) + "-> B")
    elif number >= 5:
        print(str(number) + "-> C")
    elif number >= 3:
        print(str(number) + "-> D")
    else:
        print(str(number) + "-> F")

#Exercise 5
def count_letters (list):
    for i in range(0, len(list)):
        print(list[i] + " -> " + str(len(list[i])))

def multiplication():
    running = True
    i = 1
    while running == True:
        print(i)
        i *= 2
        if i > 1000:
            print(i)
            running = False

#Exercise 6
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

def classify_triangle(a, b, c):
    if a == b and b == c:
        print("equilateral")
    elif a == b or a == c or c == b:
        print("isosceles")
    elif a != b and a != c and b !=c:
        print("scalene")

#Exercise 7
def dictionary_exercise(dictionary):
    print(dictionary["name"])
    print(len(dictionary["subjects"]))
    if "PNE" in dictionary["subjects"]:
        print("PNE is in")
    else:
        print("PNE is not")
    print(str(dictionary["grades"]["Databases"]))
    average = dictionary["grades"]["PNE"] + dictionary["grades"]["Networks"] + dictionary["grades"]["Networks"] / len(dictionary["grades"])
    print (str(round(average, 2)))
student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}
dictionary_exercise(student)