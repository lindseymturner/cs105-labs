"""

There are two whole sets of doctest examples here.

The first one is for the basic "excited" function, in this triple-quoted section,
and then a second set of tests for a later lab.
In the first lab that works with this file, you can ignore the second set.

>>> excited(["Recursion", "and", "lists!"])
['Recursion!', 'and!', 'lists!!']

Note, also, that your function should not _change_ the list it is given, so:

>>> myTest = ["Recursion", "and", "lists!"]
>>> excited(myTest)
['Recursion!', 'and!', 'lists!!']
>>> myTest
["Recursion", "and", "lists!"]

############# You should replace this line with some more examples #########


"""

"""

When it's time to use this second set of examples, just remove the two sets of
triple-quotes on the lines just above this, and you'll have one big set of tests


To make this more concrete, note that you should be able to pass tests like this one:
>>> excited2(["wow", ["a list", "with", "a list"], "cool"])
['wow!', ['a list!', 'with!', 'a list!'], 'cool!']

>>> excited2(["wow", "cool"]) # does what excited would have done
['wow!', 'cool!']

>>> myTest2 = ["wow", ["a list", "with", "a list"], "cool"]
>>> excited2(myTest2)
['wow!', ['a list!', 'with!', 'a list!'], 'cool!']
>>> myTest2
["wow", ["a list", "with", "a list"], "cool"]


To make this more concrete, note that you should be able to pass tests like this one:
>>> def veryExcited(s: str)-> str: return s+"!!!"
>>> excitable(["wow", "extra excitement", "cool"], veryExcited)
['wow!!!', 'extra excitement!!!', 'cool!!!']

>>> excited3(["wow", "cool"]) # does what excited would have done
['wow!', 'cool!']

>>> excited3(myTest)
['Recursion!', 'and!', 'lists!!']
>>> myTest
["Recursion", "and", "lists!"]



>>> def veryExcited(s: str)-> str: return s+"!!!"
>>> excitable4(["wow", ["extra", "sublist", "excitement"], "cool"], veryExcited)
['wow!!!', ['extra!!!', 'sublist!!!', 'excitement!!!'], 'cool!!!']
>>> excited4(["wow", "cool"]) # does what excited would have done
['wow!', 'cool!']


>>> excited4(myTest)
['Recursion!', 'and!', 'lists!!']
>>> myTest
["Recursion", "and", "lists!"]

"""


from Logic import precondition, postcondition



#############################################################################################
# The following gets the DocTest system to check test cases in the documentation comments.  #
# In most Haverford CS course, you won't need to modify the stuff below.                    #
#############################################################################################

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all "+str(result[1])+" tests"))
    else:
        print("Rats!")
