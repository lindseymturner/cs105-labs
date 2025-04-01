"""

>>> print(triangle_text(3, "LowerLeft"))
*
**
***

# If you like, you may remove the third (last) "newLine" in this test:
>>> print("here's a triangle between lines" + newLine + "===" + newLine + triangle_text(3, "LowerLeft") + newLine + "===")
here's a triangle between lines
===
*
**
***
===



"""

from Logic import *


newLine = "\n"   # the \n makes DocTest sad, so I'll use this variable in tests


# Corner should be "UpperLeft" or "LowerLeft" (or, if you like, also "UpperRight", "LowerRight")
def triangle_text(size: int, corner: str) -> bool:
    result = "*\n**\n***"  # the \n means 'new line goes here" ... newline is one character

    return result   # Well, sometimes it's right...


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
