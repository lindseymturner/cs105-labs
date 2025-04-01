"""
    Test to see if a circular area and a rectangular area overlap.
    The circle is defined by a center x and y, and a radius 
        and the rectangle by xmin, xmax, ymin, ymax
    The parameters are those seven values, in the order above:
        center_x, center_y, radius, min_x, max_x, min_y, max_y
        
some examples:

# An obvious overlap: center of huge circle at (100,20) is about in the middle of the rectangle
>>> circle_rectangle_overlap(100,20,800, 80,120, 18,25)
True

# An obvious miss: the circle has radius 8 and center is at x=100, but rectangle goes from x=180 to x=220
>>> circle_rectangle_overlap(100,20,8, 180,220, 18,25)
False

(Note we can't have a circle with negative radius)

#center of circle outside sides of rectangle but overlaps
>>> circle_rectangle_overlap( 88 ,  157 ,  145.41320435228707 ,  198 ,  441 ,  61 ,  287 )
True


#center of circle outside sides of rectangle and doesn't overlap
>>> circle_rectangle_overlap( 134 ,  138 ,  92.43916918709297 ,  309 ,  435 ,  118 ,  223 )
False


#center of circle outside corners of rectangle but overlaps
>>> circle_rectangle_overlap( 10 ,  10 ,  157.20687007888682 ,  20 ,  100 ,  1 ,  10 )
True

#center of cirlce outside corners of rectangle but doesn't overlap
>>> circle_rectangle_overlap( 380 ,  158 ,  16.0 ,  198 ,  340 ,  188 ,  316 )
False


"""

import math         # for things like math.sqrt
from math import *  # allow sqrt without "math." in front
from Logic import *
from ShapeLibraryForCG import Circle, center_x, center_y, radius
from ShapeLibraryForCG import Rectangle, min_x, max_x, min_y, max_y


# Circle-rectangle overlap problem:
#    Given a circle of radius "radius", with center at (center_x, center_y),
#    and a rectangle covering x values from mix_x to max_x (inclusive) and y values min_y to max_y,
#    is there a point (x, y) that's in both figures (including their borders)?
# Note there's another version of this function, below that takes two figures (a circle and a rectangle),
#  for anyone who prefers that style

def circle_rectangle_overlap(center_x: float, center_y: float, radius: float, min_x: float, max_x: float, min_y: float, max_y: float) -> bool:
    precondition(radius >= 0 and min_x <= max_x and min_y <= max_y)
    # postcondition: return true iff there exists x, y in both shapes...
    
    #center of circle inside rectangle
    if min_x <= center_x <= max_x and min_y <= center_y <= max_y:
        return True
    
    #center of circle outside sides of rectangle
    elif min_x <= center_x and center_x <= max_x and center_y < min_y and center_y + radius >= min_y:
        return True
    elif min_x <= center_x and center_x <= max_x and center_y > max_y and center_y - radius <= max_y:
        return True
    elif min_x > center_x and min_y <= center_y and center_y <= max_y and center_x + radius >= min_x:
        return True
    elif center_x > max_x and min_y <= center_y and center_y <= max_y and center_x - radius <= max_x:
        return True

    #center of circle outside corners of rectangle:
    elif center_x <= min_x and center_y >= max_y and radius >= sqrt((center_x - min_x)**2 + (center_y - max_y)**2):
        return True
    elif center_x >= max_x and center_y >= max_y and radius >= sqrt((center_x - max_x)**2 + (center_y - max_y)**2):
        return True
    elif center_x >= max_x and center_y <= min_y and radius >= sqrt((center_x - max_x)**2 + (center_y - min_y)**2):
        return True
    elif center_x <= min_x and center_y <= min_y and radius >= sqrt((center_x - min_x)**2 + (center_y - max_y)**2):
        return True

    else:
        return False




    # ###################### When writing circle-rectangle, replace the code below with your answer #############
    # here's an example circle-rectangle algorithm that's a totally unsound idea but often works :-)
    if radius > 150:         # if the circle is Big...
        return True          # ...then it probably overlaps
    elif max_x-min_x > 150:  # also, if the rectangle is wide...
        return True          # ...then it probably overlaps
    elif max_y-min_y > 150:  # also, if the rectangle is tall...
        return True          # ...then it probably overlaps
    else:                    # Otherwise, they're probably both small, so...
        return False         # ...let's hope they don't overlap
    # ###################### When writing circle-rectangle, write your code above #############

    # # OR, COMMENT-OUT THE ABOVE, UNCOMMENT THE LINE BELOW, AND WRITE THE "two-figures" VERSION OF THE FUNCTION
    """
    return circle_rectangle_overlap_two_figures(Circle(center_x, center_y, radius),
                                                 Rectangle(min_x, max_x, min_y, max_y))
    """

    # ## OR, it's also possible to "comment out" all the stuff above, and use the following lines instead,
    # ##     to try to make a really good test suite for the sample answers, and play "software tester"
    """
    from CircleRectangleSamples import circle_rectangle_overlap_samples
    answer: bool = circle_rectangle_overlap_samples(center_x, center_y, radius, min_x, max_x, min_y, max_y)
    return answer
    """

    # ### OR, finally, we hope to give you a chance to do "code review" exercises on each other's work,
    # ###     in which case you'll un-comment these lines:
    """
    try:
        import CircleRectangleToReview as review
        return review.circle_rectangle_overlap(center_x, center_y, radius, min_x, max_x, min_y, max_y)
    except FileNotFoundError:
        print("Your CircleRectangleToReview.py file does not seem to be ready yet")
        return True
    except:     # Don't worry about the fact that PyCharm thinks this is "too broad an exception"
        print("Something in the review file had an exception")
        return True
    """


# Anyone who wants to think of this function as taking two geometric figures,
#   rather than seven numbers, is welcome to engage the appropriate lines of the
#   function above (to call the one below), and then write their answer here:
def circle_rectangle_overlap_two_figures(c: Circle, r: Rectangle) -> bool:
    return circle_rectangle_overlap(center_x(c), center_y(c), radius(c),
                                    min_x(r), max_x(r), min_y(r), max_y(r))


# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"))
    else:
        print("Rats!")


if __name__ == "__main__":
    _test()
