# checking functions: functions that may be of use in reasoning about sorting
# John Dougherty and Dave Wonnacott    cs105    Haverford College

from Logic import precondition, postcondition

# ToDo: These could all use some doctest examples,
# ToDo: The "for i in range(len(s))" loops below could mostly be "for e in s"


# returns true iff s is sorted in ascending order, basic recursive design version
def is_sorted(s: str) -> bool:
    """
    >>> is_sorted("")
    True
    >>> is_sorted("e")
    True
    >>> is_sorted("def")
    True
    >>> is_sorted("gef")
    False
    >>> is_sorted("dbf")
    False
    >>> is_sorted("dgf")
    False
    >>> is_sorted("dea")
    False
    """
    if len(s) < 2:                          # empty or singleton
        return True
    else:               # first pair in order & remaining sorted
        return (s[0] <= s[1]) and (is_sorted(s[1:]))


# return true if and only if s1 and s2 have the same collection of things
def same_elements(s1: str, s2: str) -> bool:
    """
    >>> same_elements("abccba", "cabcab")
    True
    >>> same_elements("cabcab", "abccba")
    True
    >>> same_elements("abceba", "cabcab")
    False
    >>> same_elements("cabcab", "adccba")
    False
    """
    # How many times does x appear in s?
    def count_occurances(x, s):
        if len(s) == 0:
            return 0
        elif s[0] == x:
            return 1+count_occurances(x, s[1:])
        else:
            return   count_occurances(x, s[1:])
        
    # if, for any element c in s1 or s2, the don't have the same number of those, there's trouble!
    for c in s1 + s2:
        if count_occurances(c, s1) != count_occurances(c, s2):
            return False
        
    # if we didn't return False above, then they must have the same set of elements
    return True
    
    
# confirm that "big" is the biggest element in "s"
def is_this_biggest(biggest_letter_we_hope: str, s: str) -> bool:
    """
    >>> is_this_biggest("m", "m")
    True
    >>> is_this_biggest("m", "me")
    True
    >>> is_this_biggest("m", "am")
    True
    >>> is_this_biggest("m", "mz")
    False
    >>> is_this_biggest("m", "zm")
    False
    >>> is_this_biggest("m", "")   # don't crash!
    False
    >>> try:
    ...    is_this_biggest("", "abc")
    ... except:
    ...    print("Aha, as expected, a problem!")
    Aha, as expected, a problem!
    """
    precondition(len(biggest_letter_we_hope) == 1)

    found_it = False
    for c in s:
        if c == biggest_letter_we_hope:
            found_it = True
        if c > biggest_letter_we_hope:
            return False
    return found_it


def is_this_smallest(smallest_letter_we_hope: str, s: str) -> bool:
    """
    >>> is_this_smallest("m", "m")
    True
    >>> is_this_smallest("m", "mz")
    True
    >>> is_this_smallest("m", "ym")
    True
    >>> is_this_smallest("m", "ma")
    False
    >>> is_this_smallest("m", "am")
    False
    >>> is_this_smallest("m", "")   # don't crash!
    False
    >>> from Logic import PreconditionException
    >>> try:
    ...    is_this_smallest("", "abc")
    ... except PreconditionException:   # note we import this, too
    ...    print("Aha, as expected, a precondition failed!")
    Aha, as expected, a precondition failed!
    """
    precondition(len(smallest_letter_we_hope) == 1)

    found_it = False
    for c in s:
        if c == smallest_letter_we_hope:
            found_it = True
        if c < smallest_letter_we_hope:
            return False
    return found_it
