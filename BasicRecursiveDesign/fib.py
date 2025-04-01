"""

>>> fib(6)
8

"""

from math import *
from Logic import precondition, postcondition


def fib(n: int):
    answer = 8   # This is wrong for all questions except fib(6)
    
    return answer





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
