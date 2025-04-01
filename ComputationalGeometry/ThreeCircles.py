"""

Name:
email:
Lab Partner's Name:
Lab Partner's email:

===========================================================================================

In this variant of the circle overlap problem, we'll have three circles.
We want to know if each of them overlaps both of the others.

In other words, if the first one overlaps the second and third, and
the second overlaps the first and third, and the third overlaps the first and second,
then the function returns True. But, if any pair don't overlap, it returns False.

We'll provide a reasonably complete test suite for this one,
so don't fret too much about strange cases.

Suppose we have three circles in a row, with centers (0, 0), (100, 0), and (200, 0).
If they're bigger than size 50, each one just touches the neighbors.
If they're bigger than size 100, the two end ones touch each other.
Let's try some examples of that:

Three in a row, as described above, with sizes 120
>>> three_circles_all_overlap_pairwise(0,0,120,  100,0,120,   200,0,120)
True

Now, with sizes 20, nothing overlaps:
>>> three_circles_all_overlap_pairwise(0,0,20,  100,0,20,   200,0,20)
False

And, the interesting case, if the're all size 65
>>> three_circles_all_overlap_pairwise(0,0,65,  100,0,65,   200,0,65)
False


Of course, they don't have to be in a line,
e.g., we could have centers at (100,100) and (150,100) --- note their centers are 50 apart ---
and also a center at (130,140), which is also 50 away from (100, 100), but just under 45 from (150,100)

In this set of examples, if they each have radius bigger than 1/2 way to the more distant neighbor,
they should touch ... the since half the longest distance just over 22, let's try making them all size 30
>>> three_circles_all_overlap_pairwise(100,100,30,  150,100,30,  130,140,30)
True

Or, try making them all tiny, say size 5, and nothing overlaps:
>>> three_circles_all_overlap_pairwise(100,100,5,  150,100,5,  130,140,5)
False

Or, if the circles are all size 23, the ones with centers about 45 apart will overlap,
but neither of those will overlap the one whose center is 50 away from each of them
>>> three_circles_all_overlap_pairwise(100,100,23,  150,100,23,  130,140,23)
False



Now, we could ask about all those same scenarious, but ask do _any_ two circles overlap:

Three in a row, distances between centers 50, 50, 100, with sizes 120
>>> three_circles_any_overlap(0,0,120,  100,0,120,   200,0,120)
True

Now, with sizes 20, nothing overlaps:
>>> three_circles_any_overlap(0,0,20,  100,0,20,   200,0,20)
False

And, the interesting case, if the're all size 65, since we want to know if _any_ pair overlaps:
>>> three_circles_any_overlap(0,0,65,  100,0,65,   200,0,65)
True


Now, with centers (100,100) and (150,100) and (130,140)

All touching:
>>> three_circles_any_overlap(100,100,30,  150,100,30,  130,140,30)
True

None touching:
>>> three_circles_any_overlap(100,100,5,  150,100,5,  130,140,5)
False

With the circles are all size 23, the ones with centers ~45 apart will overlap,
but neither of those will overlap the one whose center is 50 away from each of them
>>> three_circles_any_overlap(100,100,23,  150,100,23,  130,140,23)
True

"""

import math         # for things like math.sqrt
from math import *  # allow sqrt without "math." in front
from ShapeLibraryForCG import Circle, center_x, center_y, radius
from Circle import circle_overlap, circle_overlap_two_figures
from Logic import *

def circle_overlap(xcenter1: float, ycenter1: float, radius1: float, xcenter2: float, ycenter2: float, radius2: float) -> bool:
    precondition(radius1 >= 0 and radius2 >= 0)

    distance = sqrt((xcenter1 - xcenter2) ** 2 + (ycenter1 - ycenter2) ** 2)
    r = radius1 + radius2
    if distance <= r:
        return True
    else:
        return False


def three_circles_all_overlap_pairwise(center_x1: float, center_y1: float, radius1: float, center_x2: float, center_y2: float, radius2: float, center_x3: float, center_y3: float, radius3: float, ) -> bool:
    precondition(radius1 >= 0 and radius2 >= 0 and radius3 >= 0)
    distance1 = circle_overlap(center_x1, center_y1, radius1, center_x2, center_y2, radius2)
    distance2 = circle_overlap(center_x1, center_y1, radius1, center_x3, center_y3, radius3)
    distance3 = circle_overlap(center_x2, center_y2, radius2, center_x3, center_y3, radius3)
    if distance1 and distance2 and distance3:
        return True
    else:
        return False

    # REPLACE THE NEXT LINE WITH YOUR ALGORITHM, OR SEE BELOW
    return True
    # OR, DELETE THE ABOVE, UNCOMMENT THE LINE BELOW AND WRITE THE FUNCTION BELOW
    """
    return three_circles_all_overlap_three_figures(Circle(center_x1, center_y1, radius1),
                                                   Circle(center_x2, center_y2, radius2),
                                                   Circle(center_x3, center_y3, radius3))
    """

def three_circles_all_overlap_three_figures(c1: Circle, c2: Circle, c3: Circle) -> bool:
    precondition(radius(c1) >= 0 and radius(c2) >= 0 and radius(c3) >= 0)

    return three_circles_all_overlap_pairwise(center_x(c1), center_y(c1), radius(c1),
                                              center_x(c2), center_y(c2), radius(c2),
                                              center_x(c3), center_y(c3), radius(c3))


def three_circles_any_overlap(center_x1: float, center_y1: float, radius1: float,
                              center_x2: float, center_y2: float, radius2: float,
                              center_x3: float, center_y3: float, radius3: float,) -> bool:
    precondition(radius1 >= 0 and radius2 >= 0 and radius3 >= 0)

    # REPLACE THE NEXT LINE WITH YOUR ALGORITHM, OR SEE BELOW
    return True
    # OR, DELETE THE ABOVE, UNCOMMENT THE LINE BELOW AND WRITE THE FUNCTION BELOW
    """
    return three_circles_any_overlap_three_figures(Circle(center_x1, center_y1, radius1),
                                                   Circle(center_x2, center_y2, radius2),
                                                   Circle(center_x3, center_y3, radius3))
    """

def three_circles_any_overlap_three_figures(c1: Circle, c2: Circle, c3: Circle) -> bool:
    precondition(radius(c1) >= 0 and radius(c2) >= 0 and radius(c3) >= 0)

    return three_circles_any_overlap(center_x(c1), center_y(c1), radius(c1),
                                     center_x(c2), center_y(c2), radius(c2),
                                     center_x(c3), center_y(c3), radius(c3))



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
