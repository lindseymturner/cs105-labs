"""
    func_time(function, repeats):
      Run the function _function_ for _repeats_ iterations,
      then return the average elapsed processing time.

      Note that this does not consistently count time taken for the computer's memory,
      or time taken for other programs running on the computer (for that, we would need
      to switch "perf_counter" to "process_time" in two places below).


Note that "function" to be timed must take zero parameters,
e.g. we can't use func_time(fib(12), 1000) because
     fib(12) would be called before func_time starts;
     we could create sample_fib (see below) to compute
     fib(12), and then use func_time(sample_fib, 1000).

# Note two notations for defining a function, below:
>>> from fib import fib
>>> def sample_fib(): return fib(12)
>>> sample_fib()
144
>>> sample_fib2: Callable[[], int] = (lambda : fib(12))
>>> sample_fib2()
144

Something too fast to measure easily, will need to be run repeatedly.
If you run it only once, as in the example below, you may get 0.0,
and occasionally get the minimum measurable amount of time (0.001s?).
>>> func_time(sample_fib, 1)   # doctest: +ELLIPSIS

Running a 100 microsecond function 10000 times should take about 0.1 second,
and 0.1s is short enough to not be tedious, but long enough to measure.
>>> func_time(sample_fib, 1000)   # doctest: +ELLIPSIS


If repeats is 0 or missing,
automatically try to run for at least 250ms (can be replaced with optional 3rd parameter).
>>> func_time(sample_fib)   # doctest: +ELLIPSIS


If you want to be able to time a function that needs parameter(s),
create a zero-parameter function that calls it with whatever parameter(s) you want.
(The most concise way being to use lambda, e.g. to time fib(14), we do the following):

>>> func_time((lambda : fib(12)), 1000)

Somewhat less concise is to define a function with a name, i.e. sample_fib above.

You can make it more flexible by giving sample_fib a parameter:

>>> def fib_time(n, repeats=0):
...     def fib_n(): return fib(n)
...     return func_time(fib_n, repeats)  # func_time( (lambda: fib(n)), repeats )

>>> fib_time(12)


"""

import time
from typing import Callable
from typing import Any


def func_time(function: Callable[[], Any],
              repeats: int=0,
              min_time: float=0.250):
    """
        Run FUNCTION for REPEATS repetitions,
         and return the average time taken.
        If REPEATS is 0 or missing,
         run for MIN_TIME (default 1/4sec) consecutive calls
    """
    r = repeats if repeats != 0 else 1
    done = False
    while not done:
        start = time.perf_counter()  # counts of computation time (contrast process_time)
        for i in range(0,r):
            function()
        end = time.perf_counter()
        if repeats>0 or end-start>min_time:   # @ToDo: Dave should check whether this is right.
            done=True
        else:
            r = r*2
#    print("     R was "+str(r))
    return (end-start)/(r*1.0)




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
    print("Note: calling nothing seems to take about " + str(func_time(nothing, 1000000)) + " seconds on this computer")

