"""

This file is designed to import logic.py file for Haverford CS projects,
 or allow work that use the core features, e.g.,  'precondition' and 'postcondition',
 even if the full logic.py is not available.

"""

# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print("*** Can't find logic.py in /home/courses/python, resorting to basic versions")
    print("*** If this happens in the CS teaching lab, tell your instructor.")
    print("*** (If it happens on your computer, that's ok; you can comment out these 3 lines.)")


    def precondition(value_of_precondition):
        if (value_of_precondition != True):
            raise "Precondition failed"

    def postcondition(value_of_postcondition):
        if (value_of_postcondition != True):
            raise "Postcondition failed"

    def assertion(value_of_assertion):
        if (value_of_assertion != True):
            raise "Assertion failed"

    def loopInvariant(value_of_loop_invariant):
        if value_of_loop_invariant != True:
            raise "Loop Invariant Failed"

    def is_integer(v): return isInteger(v)
    def isInteger(v):
        return isinstance(v, int)

    def is_number(v): return isNumber(v)
    def isNumber(v):
        return isInteger(v) or isinstance(v, float)

    def is_string(v): return isString(v)
    def isString(v):
        return isinstance(v, str)


    def is_boolean(v): return isBoolean(v)
    def isBoolean(v):
        return isinstance(v, bool)

