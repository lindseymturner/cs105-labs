from Logic import precondition

def distance(word_1: str, word_2: str) -> int:
    """
    This function takes in two words and checks if the corresponding letters (with the same index) are different. If one word is longer, all the additional letters are counted.
    :param word_1: The first word.
    :param word_2: The second word.
    :return: The count of the number of letters that are different for each index.

    :examples:
    >>> distance("apple", "apble")
    1

    >>> distance("chicken", "thomas")
    6

    >>> distance("oh", "qwertyuiop")
    10


    """
   # precondition(word_1.isalpha() and word_2.isalpha())
    if len(word_1) < len(word_2):
        shortWord = word_1.lower()
        longWord = word_2.lower()
    else:
        shortWord = word_2.lower()
        longWord = word_1.lower()

    count = 0
    # goes through each letter in the short word, if the letter is different from the corresponding letter in the long word, then 1 is added to the total distance.
    for index in range(len(shortWord)):
        if shortWord[index] != longWord[index]:
            count += 1
    # for each additional letter the long word contains, 1 is added to the count.
    count += len(longWord) - len(shortWord)
    return count



