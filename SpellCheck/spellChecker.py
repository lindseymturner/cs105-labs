from distanceHamming import distance
from closestWord import closest_word
from distanceEuclideanHamming import distanceE


print("Welcome to the spell checker")

print("A program by _Lindsey Turner___ and __Carter Rostron___")

# this is the word that each input word is compared to
word = "Computer"


def UI_oneword():
    # the function keeps asking the user to enter a word until they enter something other than a letter
    while True:
        user_word = input("Enter a word")
        if user_word.isalpha():
            # determines the distance between the main word and the user input
            print(distance(word, user_word))
        else:
            break


# UI_oneword()

def UI_list():
    # opens a file that contains all of the words in the english dictionary, each on different lines
    contents = open('/home/davew/lib/words-lowercase.txt', 'r')
    # reads the file all at once in a string
    readlines_file = contents.read()
    # removes the new line after each word in the file, and creates a list of all the words in the file
    readlines_file = readlines_file.split("\n")
    # creates a new file where each input and its closest word are placed in separate lines
    outfile = open('spelling_records.txt', 'w')

    while True:
        user_input = input("Please enter a word or type STOP")

        if user_input == "STOP":
            outfile.close()
            break
        closeWord = closest_word(user_input, readlines_file)
        line = user_input + "-" + closeWord
        outfile.write(line + "\n")
        print("The closest word is", closeWord)
        normalDistance = distance(user_input, closeWord)
        print("The regular distance between", user_input, "and", closeWord, "is", normalDistance)
        keyboardDistance = distanceE(user_input, closeWord)
        print("The euclidean distance between", user_input, "and", closeWord, "is", keyboardDistance)


UI_list()












