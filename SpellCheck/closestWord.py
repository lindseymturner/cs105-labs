from typing import List

from distanceEuclideanHamming import distanceE
from Logic import precondition

def closest_word(mainWord: str, words: List [str] ) -> str:


    """
    This function compares the euclidean distance between a reference word and each word in a list to return the word with the smallest distance.
    :param mainWord: This is the string that all the other strings in the list are compared to.
    :param words: This is the list of words that are each compared to the reference word.
    :return: It returns the word in the list that has the least euclidean distance to the reference word. This is a string.


    :examples:
    >>> closest_word('dog', ['sheep', 'dog', 'parrot'])
    'dog'
    >>> closest_word('dog', ['door', 'dip', 'dot'])
    'dot'
    >>> closest_word('dog', ['cat'])
    'cat'
    >>> closest_word('lip', ['caramel', 'coffee', 'put', 'kuo'])
    'kuo'

    """
   # precondition(mainWord.isalpha())
    # Start with a really big number so the first word distance is less
    minDistance = 1000000000000000000000000.0
    closest = None
# go through all of the words in the list and if that word has a lesser distance than the current minimum distance, that word now becomes the closest word, and the minimum distance is updated
    for word in words:
        wordDistance = distanceE(mainWord, word)
        if wordDistance < minDistance:
            minDistance = wordDistance
            closest = word
    return closest

