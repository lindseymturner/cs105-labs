"""

Name: Lindsey Turner
email: lturner@haverford.edu
Lab Partner Name:
Lab Partner email:

--- Part 1: sum_of_digits ---

None of these tests will pass yet, since there isn't a function written yet.

>>> sum_of_digits(123)
6

>>> sum_of_digits(321)
6

>>> sum_of_digits(777)
21

>>> sum_of_digits(65)
11

>>> sum_of_digits(123456789987654321)  # I think this should be 90...
90

>>> sum_of_digits(24)
6

>>> sum_of_digits(1001)
2

--- later solo part, for which the starter file has a correct version that you should change ---

Note that, when sum_of_digits produces an answer between 0 and 8,
this tells us the remainder "mod 9":

>>> mod9(321)
6

Of course, the remainder "mod 9" must be between 0 and 8, so when the answer is 9, we have to produce a 0:
>>> mod9(45)
0

And, when the sum is bigger than 9, we can sum the digits again (possibly more than once) to get n mod 9
>>> mod9(65)
2

Here we have a larger number that has to keep being passed through the sum of digits function until we have a single digit number as the output. Since the number does not equal 9, the remainder is the number
>>> mod9(57819)
3

Here we have a larger number that is passed through the sum of digits function until the output = 9, meaning that it has a remainder of 0.
>>> mod9(57879)
0

"""

from Logic import precondition, postcondition


def precondition(value_of_precondition):
    if (value_of_precondition != True):
        raise "Precondition failed"


def postcondition(value_of_postcondition):
    if (value_of_postcondition != True):
        raise "Postcondition failed"

# put your sum_of_digits function here

def sum_of_digits(number):
    number = abs(number)
    if number > 0:
        return number % 10 + sum_of_digits(number // 10)
    else:
        return 0


# Then, in the solo part, replace this with a function that does not have "//9" or "%9" or "-9" in it
#   (you can divide by, or subtract, 10, if you want to).
def mod9(n: int) -> int:
    return n%9   # easiest way to find "n mod 9": use the built-in part of Python :-)

def mod9(number):
#base case - if number is a single digit
#scenario 1 of base case - if number is less than 9, the remainder equals that number
    if number < 9:
        return number
#scenario 2 of base case - if the number is 9, the remainder equals zero
    elif number == 9:
        return 0
#recursive case - if number is greater than 9, the number will go through the sum of digits function and then the mod 9 function until the number is less than or equal to 9
    else:
        return mod9(sum_of_digits(number))


# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")


# tests may or may not be chosen by the user interface...
if __name__ == "__main__":
    _test()
