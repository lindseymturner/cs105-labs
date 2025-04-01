"""

# Some examples, see the lab assignment for more information

>>> fib(1)
1
>>> fib(2)
1
>>> fib(3)
2
>>> fib(4)
3
>>> fib(5)  # easy to remember, fib(5) is 5
5
>>> fib(6)
8
>>> fib(7)
13
>>> fib(8)
21
>>> fib(9)
34
>>> fib(10)
55
>>> fib(11)
89
>>> fib(12) # Dave's favorite test, fib(12) happens to be 12*12
144

"""


from func_time import func_time

# direct recursive solution to Fibonacci sequence calculator
# meant to be timed by fib_time.py, so run that to see the timing
# To avoid throwing off the timing, there are no pre- or post-conditions checked

def fib(n):
    # precondition(n is a positive integer)
    # postcondition(fib(n) is the nth element of the Fibonacci sequence
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibwork(n):
    # precondition(n is a positive integer)
    # postcondition(fibwork(n) == fib(n) - 1)
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2) - 1

print(fibwork(50))



def fibtime():
    for n in [1, 2, 3, 4, 5, 6, 7, 15, 25]:
        time: float = func_time((lambda: fib(n)))
        print("# Time for Fib(n) is", time)
        print(n, time)
fibtime()

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

