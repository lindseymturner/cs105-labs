"""

Some functions to compute b to the e power, for positive integer e.
Useful to explore program speed.

# First, we pick a power function from the list below
>>> power: Callable[[float, int], float] = power1
>>> power(10.0, 5)
100000.0

>>> power(2.0, 3)
8.0

>>> power(2.0, 10)
1024.0

>>> power(3.0, 5)
243.0

>>> power(5.0, 3)
125.0

>>> power(0.5, 3)  # one eighth
0.125

>>> power(1.0, 500)
1.0


# Check the power1a example of the "count the work" approach;
#  we think the work is one less than the exponent, based on
#  the following, so we add that as a postcondition
>>> power1a(3.0, 5)
(243.0, 4)

>>> power1a(5.0, 3)
(125.0, 2)

>>> power1a(1.0, 500)
(1.0, 499)


# Now, some tests of the speed of "power", using func_time
# These always error in doctest, since we get varying times
>>> func_time((lambda : power(1.0, 500)), 1000)
some amount of time to compute 1.0 to the 500th power, e.g., on sammet,
12e-5 for power1, or
?e-5 for power2, or
?e-5 for power3


# Now, some timing tests!  Do b and e both matter?
# >>> for b in [2.0, 50.0, 1000.0, 6.024e23]:
# ...    print("# Time for power(", b, ", 500) is", func_time((lambda : power(b, 500))))

>>> for e in [2, 8, 32, 125, 250, 500]:
...    time: float = func_time((lambda : power(10.0, e)))
...    print("# Time for power(10.0, ", e, ") is", time)
...    print(e, time)
*****************************************************
***  Note: times vary a lot, so there's no point  ***
***        in having an expected answer here.     ***
***  This test will always "fail", that's fine.   ***
*****************************************************


"""
from func_time import func_time
from Logic import precondition, postcondition
from typing import Callable
from typing import Tuple


# basic recursive design
def power1(base: float, exp: int) -> float:
    precondition(exp > 0)
    if exp == 1:
        return base
    else:
        return base*power1(base, exp-1)


# How much work is done by the B.R.D. function?
#
# Here's a version that returs both the answer (as a float)
#  and the number of multiplications needed to get it (an integer),
#  as a Python Tuple.
# We include the code above, with a few more variables to emphasize B.R.D.,
#  and also define my_work in terms of the work for the "smaller question",
#  having done that, we then try to figure out the best postcondition
#  decription of my_work directly in terms of the parameters (in this case,
#  we care about "exp", though some functions might care about both)
#
def power1a(base: float, exp: int) -> Tuple[float, int]: # (work, result)
    precondition(exp > 0)
    if exp == 1:
        my_result: float = base
        my_work: int = 0  # no multiplications done for the base case :-)
        return (my_result, my_work)
    else:
        smaller_result_and_work: Tuple[float, int] = power1a(base, exp-1)
        smaller_result: float = smaller_result_and_work[0]
        smaller_work: int = smaller_result_and_work[1]

        my_result: float = base*smaller_result
        # recurrence - refers to the work calculation of the simpler case in the recursive case
        my_work: int = smaller_work+1
# closed form - expresses the value of my_work directly in terms of the function's parameters, specifically as exp-1
        postcondition(my_work == exp-1)
        return (my_result, my_work)


# Basic approach to power, with a loop
# Start with result=base, keep multiplying until you have enough
def power2(base: float, exp: int) -> float:
    precondition(exp > 0)
    result: float = base
    n_bases: int = 1
    while n_bases < exp:	# could also use a Python "for" loop
        result = result * base
        n_bases = n_bases+1
    return result


# Recursive, but try to be clever for even exponents
# Specifically, for, e.g., 3 to the 100th,
#  we don't need to multiply out 100 3's;
#  we can find 3 to the 50th and then square that!
def power3(base: float, exp: int) -> float:
    precondition(exp > 0)
    if exp == 1:
        return base
    elif exp%2==0:   # if exp is _even_
        half_exp: int = exp//2
        base_to_half_exp: float = power3(base, half_exp)
        return base_to_half_exp * base_to_half_exp
        # ToDo: Discuss what happens if we inline that variable definition
    else:
        return base * power3(base, exp-1)  # this is still true, use it!


# copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    # print "Result of doctest is:", result
    if result[0] == 0:
        print("Wahoo! Passed all " +str(result[1])+ " tests!")
    else:
        print("Rats!")

if __name__ == "__main__":
    _test()
    def nothing(): return
    print("Note: calling a function that does nothing seems to take about " + str(func_time(nothing, 10000000)) + " seconds on this computer")

