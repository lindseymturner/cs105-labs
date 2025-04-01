"""
This file provides a library of shape types for doing more idiomatic computational geometry problems.

For example, circle_overlap can take two _circle_ objects instead of just six numbers.
Both message-send notation like c.radius() and function-call notation like radius(c) are allowed.

Some trivial examples:

>>> c1:Circle = Circle(100,120, 20)   # radius-20  circle at (100, 120)
>>> c2:Circle = Circle(150,140, 300)  # radius-300 circle at (150, 140)
>>> rect:Rectangle = Rectangle(100,150, 120,140)  # rectangle with corners at the circle's centers

>>> radius(c1)
20
>>> c1.radius()
20
>>> center_x(c1)
100
>>> center_y(c1)
120

>>> c2.radius()
300
>>> c2.center_x()
150
>>> c2.center_y()
140

>>> rect.min_x()
100
>>> rect.max_x()
150
>>> rect.min_y()
120
>>> rect.max_y()
140


"""

class CGShape:
    pass   # we might want to put something here, but, for now, this class is just for type-checking


# Huh, whinge about PyCharm or Python or something:
#      "Circle" can't be used as a type in the definition of "self"
#      without getting a compliant about it not being defined yet
class Circle(CGShape):
    def __init__(self, _center_x: float, _center_y: float, _radius: float):
        self.cx: float = _center_x
        self.cy: float = _center_y
        self.r:  float = _radius

    def center_x(self) -> float:
        return self.cx

    def center_y(self) -> float:
        return self.cy

    def radius(self) -> float:
        return self.r


# allow function-call notation instead, if we want to
def center_x(c: Circle) -> float: return c.center_x()
def center_y(c: Circle) -> float: return c.center_y()
def radius(c: Circle) -> float: return c.radius()


class Rectangle(CGShape):
    def __init__(self, _min_x: float, _max_x: float, _min_y: float, _max_y: float):
        self.min_x_: float = _min_x
        self.max_x_: float = _max_x
        self.min_y_: float = _min_y
        self.max_y_: float = _max_y

    def min_x(self) -> float:
        return self.min_x_

    def max_x(self) -> float:
        return self.max_x_

    def min_y(self) -> float:
        return self.min_y_

    def max_y(self) -> float:
        return self.max_y_


# allow function-call notation instead, if we want to
def min_x(rect: Rectangle) -> float: return rect.min_x()
def max_x(rect: Rectangle) -> float: return rect.max_x()
def min_y(rect: Rectangle) -> float: return rect.min_y()
def max_y(rect: Rectangle) -> float: return rect.max_y()


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
