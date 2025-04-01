"""
Find out whether two rectangular computer "windows" overlap,
In other words, find out whether there is any point on the screen that
is used by both.

Examples (courtesy of Andrew Wonnacott):

>>> windowOverlap(50,300,50,350, 100,500,100,500)
True

>>> windowOverlap(100,399.99,100,401, 400,600,100,400)
False

>>> windowOverlap(100,400.001,100,401, 400.0001,600,100,400)
True

>>> windowOverlap( 62 ,  179 ,  96 ,  192 ,  226 ,  346 ,  98 ,  208 )
False

>>> windowOverlap( 31 ,  173 ,  45 ,  227 ,  142 ,  292 ,  39 ,  240 )
True

>>> windowOverlap( 228 ,  390 ,  102 ,  222 ,  32 ,  150 ,  77 ,  215 )
False

>>> windowOverlap( 130 ,  221 ,  90 ,  181 ,  121 ,  278 ,  199 ,  364 )
False

>>> windowOverlap( 75 ,  424 ,  216 ,  488 ,  225 ,  240 ,  168 ,  179 )
False

>>> windowOverlap( 182 ,  389 ,  165 ,  277 ,  105 ,  197 ,  180 ,  232 )
True

>>> windowOverlap( 80 ,  244 ,  88 ,  198 ,  127 ,  159 ,  169 ,  237 )
True

>>> windowOverlap( 126 ,  262 ,  268 ,  409 ,  156 ,  186 ,  213 ,  302 )
True

Here, #2 is touching but to the right of, #1 --- this should count as overlap!
>>> windowOverlap( 100, 600, 10, 500,   600, 800, 200, 300)
True

Note that this sort of thing, with minx2 > maxx2, is not allowed!
### >>> windowOverlap( 100, 600, 10, 500,   600, 500, 200, 300)
"""

from Logic import *
from Range import *

# The following comes from Dave Wonnacott's Wednesday lecture.
# See also windowOverlapFromCourseNotes below for another approach
    
def windowOverlap(minx1: float, maxx1: float, miny1: float, maxy1: float, minx2: float, maxx2: float, miny2: float,maxy2: float) -> bool:
    if minx2 > maxx1:    # 2 to the right of 1
        return False
    elif maxy1 < miny2:  # 2 above 1
        return False
    elif maxx2 < minx1:
        return False
    elif maxy2 < miny1:
        return False
    else:
        return True


def windowOverlapFromCourseNotes(minx1: float, maxx1: float, miny1: float, maxy1: float, minx2: float, maxx2: float, miny2: float, maxy2: float) -> bool:
    precondition(minx1 <= maxx1 and minx2 <= maxx2 and miny1 <= maxy1 and miny2 <= maxy2)
    """postcondition: return true iff there exists x,y in both windows, i.e. minx1 <= x <= maxx1 and miny1 <= y <= maxy1 etc """
    return rangeOverlap(minx1, maxx1, minx2, maxx2) and rangeOverlap(miny1, maxy1, miny2, maxy2)



# copied from  http://docs.python.org/lib/module-doctest.html
# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
