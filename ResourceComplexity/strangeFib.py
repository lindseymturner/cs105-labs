"""

>>> fib(5)
5
>>> strangeFib(5)
5

>>> fib(12)
144
>>> strangeFib(12)
144

hmm... looks like these do the same thing ... do they?

"""

from math import *
from Logic import *

# strangeFib: compute fib(n) in a strange way
#  This may be faster than the obvious recursive approach,
#  though as we'll see later, there are several ways that are much faster
def strangeFib_idiomatic(n: int) -> int:
    # precondition: same as fib(n) precondition
    # postcondition: returns the same thing as fib(n)
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        # The following line deserves a better comment than this:
        return 2*strangeFib_idiomatic(n-1) - strangeFib_idiomatic(n-3)

# this version will fit better with our verificiation rules:
def strangeFib(n: int) -> int:
    # precondition: same as fib(n) precondition
    # postcondition: returns the same thing as fib(n)
    return (1
            if n<=2 else
            (2
             if n==3 else
             2*strangeFib(n-1)-strangeFib(n-3)))

def fib(n: int) -> int:
    # precondition: n>0
    # postcondition: result is the nth element in the sequence
    return 1 if n<=2 else fib(n-1)+fib(n-2)

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
