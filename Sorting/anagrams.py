# anagrams: program to check if two strings are anagrams of each other
# uses the "sort(s)" function
# Dave Wonnacott and John Dougherty    cs105    Haverford College

from Logic import *

# switch below to test your sort_letters; only one should be uncommented
from python_sort import sort_letters
# from selection_sort import sort_letters
# from insertion_sort import sort_letters
# from merge_sort import sort_letters
# from bubble_sort import sort_letters
# from quick_sort import sort_letters

from useful_functions import just_letters_as_lowercase


# returns true iff s1 is an anagram of s2; otherwise returns false
def anagrams(string1: str, string2: str) -> bool:
    """
    precondition: string1 and string2 must be only lower-case letters
    >>> anagrams('elvis', 'lives')
    True
    >>> anagrams('elvis', 'steve')
    False
    >>> anagrams('newyorktimes', 'monkeyswrite')
    True
    """
    precondition(just_letters_as_lowercase(string1.lower()) == string1 and
                 just_letters_as_lowercase(string2.lower()) == string2)

    if sort_letters(string1) == sort_letters(string2):
        return True
    else:
        return False
