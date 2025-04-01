"""

This is one of several "distance" functions one could import
into the spell-checker project.

It bases distance on the "perfectionist" scoring approach,
which is says that a perfect match is good (distance zero),
but anything at all different is imperfect and receives an
equally bad really high score of 10000.

Other files could define "distance" differently.

"""

# Logic tries to get the standard Haverford "logic" module, provides some parts if it fails
from Logic import precondition


def distance(word: str, possible_match: str) -> float:
    """
    :return: the 'perfectionist' distance between 'word' and 'possible_match',
             i.e., 0 (no distance) for exact match, and a consistent really big
             value, specifically 10000, for any non-perfect match. Both parameters
             must be made entirely of letters.

    :examples:
    >>> distance('bean', 'bean')
    0
    >>> distance('bean', 'been')
    10000
    >>> distance('bean', 'beans')
    10000
    >>> distance('bean', 'xyphoid')
    10000
    """
    # found "isalpha" on the python description of string methods:
    #  https://docs.python.org/3/library/stdtypes.html#string-methods
    # It returns true if (and only if) all characters of the string are alphabetic
   # precondition(word.isalpha() and possible_match.isalpha())

    word_lc: str = word.lower()  # same web page as for "isalpha"
    match_lc: str = possible_match.lower()

    if word_lc == match_lc:
        return 0
    else:
        return 10000

    # Note, equivalent short form of this function:
    # precondition(word.isalpha() and possible_match.isalpha())
    # return 0 if word.lower() == possible_match.lower() else 10000


#############################################################################################
# The following gets the DocTest system to check test cases in the documentation comments.  #
# In most Haverford CS course, you won't need to modify the stuff below.                    #
#############################################################################################

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all "+str(result[1])+" tests"))
    else:
        print("Rats!")
