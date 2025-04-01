"""
This is a simple example python file, including some doctest examples and a trivial function.

Use this project for any work that isn't a lab to hand in, e.g., work during lecture

>>> 6*7
42

>>> times(6, 7)
42

"""

# Logic tries to get the standard Haverford "logic" module, provides some parts if it fails
from Logic import *


def times(x: float, y: float) -> float:
    precondition(x>0 or x<=0)
    result = (x-1)*y + y
    postcondition(result == x*y)  # check our answer
    return result


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
