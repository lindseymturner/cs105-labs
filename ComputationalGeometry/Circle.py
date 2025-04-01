"""
Here are some examples of the circle-overlap problem,
in which we give the "x", "y", and radius for one circle and then the other,
and need to know if there are any points that line in/on both circles.
(Note that we don't allow a circle with negative radius.)


# An obvious overlap (Sample answer #3 got this wrong):
# Note that the second circle's center is directly to the right of the first one's,
#  only 25 away, and they each have radius 30, so each one encloses the other's center.
>>> circle_overlap(100,100,30, 125,100,30)
True

# An obvious non-overlap (Sample answer #1 gets this one wrong):
# Note that the second center is 125 to the right of the first one's center,
#  but they are each 30 wide, so that's a lot of empty space between them!
>>> circle_overlap(100,100,30, 225,100,30)
False

# An example copied from the "Console" window during a run of overlap-test-graphics,
# The second one's center is a bit to the right, not quite at the same height,
#  but they're both big enough to enclose part of the other
# When we draw circles with the mouse, the radius isn't always an integer,
#  but that's not a problem.
>>> circle_overlap( 160 ,  152 ,  82.8070045346 ,  198 ,  167 ,  93.813645063 )
True


# A final example: for those who want to think of this problem as involving
#  two CIRCLES, rather than six NUMBERS, we can use circle_overlap_concise:
>>> circle_overlap_two_figures(Circle(100,100,30), Circle(125,100,30))
True



##############################################################################
#

>>> circle_overlap( 104 ,  98 ,  191.02355875650522 ,  382 ,  170 ,  223.36517185989405 )
True


#

>>> circle_overlap( 152 ,  152 ,  43.41658669218482 ,  269 ,  201 ,  33.54101966249684 )
False

##############################################################################
"""

import math         # for things like math.sqrt
from math import *  # allow sqrt without "math." in front
from ShapeLibraryForCG import Circle, center_x, center_y, radius
from Logic import *


def circle_overlap(xcenter1: float, ycenter1: float, radius1: float, xcenter2: float, ycenter2: float, radius2: float) -> bool:
    precondition(radius1 >= 0 and radius2 >= 0)

    distance = sqrt((xcenter1 - xcenter2) ** 2 + (ycenter1 - ycenter2) ** 2)
    r = radius1 + radius2
    if distance <= r:
        return True
    else:
        return False

    # OR, DELETE THE ABOVE, UNCOMMENT THE LINE BELOW AND WRITE THE FUNCTION BELOW
    # return circle_overlap_two_figures(Circle(xcenter1, ycenter1, radius1),  Circle(xcenter2, ycenter2, radius2))

    # OR, it's also possible to "comment out" the stuff above, and use the following lines instead
    # the line below only works in the QuaCS lab computers
    # from sample_answers.cs105.Intersect.CircleSamples import circleOverlapSamples
    # answer: bool = circleOverlapSamples(xcenter1, ycenter1, radius1, xcenter2, ycenter2, radius2)
    # return answer


def circle_overlap_two_figures(c1: Circle, c2: Circle):
    return circle_overlap(center_x(c1), center_y(c1), radius(c1),
                          center_x(c2), center_y(c2), radius(c2))


# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")


if __name__ == "__main__":
    _test()
