from Logic import precondition
import math
from keyboardQWERTY import key_positions

def distanceE(word_1: str, word_2: str) -> float:
    """
    This function takes in two words and determines the euclidean distance between them.
    :param word_1: This is the first word (string).
    :param word_2: This is the second word (string).
    :return: This is the euclidean distance between the words (integer).

    :examples:

    >>> distanceE('cat', 'car')
    1.0
    >>> distanceE('car', 'caf')
    1.0
    >>> distanceE('dog', 'dog')
    0.0
    >>> distanceE('dog', 'dogg')
    10.0

    """
#    precondition(word_1.isalpha() and word_2.isalpha())
    if len(word_1) < len(word_2):
        shortWord = word_1.lower()
        longWord = word_2.lower()
    else:
        shortWord = word_2.lower()
        longWord = word_1.lower()

    count = 0
# goes through all the letters in the shorter word and compares them to find the euclidean distance between them. it adds up the distances for each of the letters. if the letter is the same, the
# distance is 0.
    for index in range(len(shortWord)):
        letter_pos1 = key_positions[shortWord[index]]
        x_coord1 = letter_pos1["x"]
        y_coord1 = letter_pos1["y"]
        letter_pos2 = key_positions[longWord[index]]
        x_coord2 = letter_pos2["x"]
        y_coord2 = letter_pos2["y"]
        euclidean_distance = math.sqrt((x_coord1 - x_coord2) ** 2 + (y_coord1 - y_coord2) ** 2)
        count += euclidean_distance
# for every additional letter that the longer word contains, 10 is added to the total distance count.
    count += (len(longWord) - len(shortWord)) * 10

    return count





