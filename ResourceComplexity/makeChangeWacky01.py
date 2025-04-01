"""

# Answer key (draft) of the 0/1 wacky change problem

# Regular make-change should give two $6 and two $4 for this
#  but in the 0/1 version, we only have one of each bill other than $1, so...
>>> wacky_change_01(20, [6, 4, 1])
[1, 1, 10]

# A more interesting case of the 0/1 version, need to skip 11 and 10:
>>> wacky_change_01(14, [11, 10, 7, 6, 1])  # We want 7 and 6 and 1, not 11 and three 1's
[0, 0, 1, 1, 1]

"""
from Logic import precondition, postcondition
from typing import List, Tuple


def wacky_change_01(amount_of_change_to_give: int,
                    denominations: List[int]) -> List[int]:
    """
    The unconventional change problem, assuming
        (a) we have a "unit" bill, e.g. $1 or 1-lek,
        (b) that unit bill comes last in our list of denominations, and
        (c) that we have only one of each other bill (but unlimited 1's).

    :param amount_of_change_to_give: A _non_negative_ integer amount of money to be given.
                                        This means we must be able to make change with $1 bills.
    :param denominations: A list positive bill values, including 1 at the end.
    :return: A list of how many of each bill to give, e.g., 1st entry is how many of 1st denomination
    """
    precondition(amount_of_change_to_give >= 0)
    precondition(denominations[len(denominations)-1] == 1)  # must have a unit bill, e.g., $1 or 1-lek
    precondition(sorted(denominations)[0] == 1)  # all must be positive, since 1 is smallest

    if len(denominations)==1:   # only one bill, just use it, no choice!
        assert(amount_of_change_to_give%denominations[0] == 0) # must work, we end with $1
        result: List[int] = [amount_of_change_to_give // denominations[0]]
        # postcondition(amount_of_change_to_give == amount_given)
        return result
    else: # general case, must consider choices
        my_bill: int = denominations[0]
        other_bills: List[int] = denominations[1:]

        if my_bill <= amount_of_change_to_give:   # we could use my bill, or not
            # Using the help of two competent helpful friends,
            #  figure out what _would_ happen _if_ I use my bill in making change, or not
            change_use_my_bill: List[int] = [1] + wacky_change_01(amount_of_change_to_give - my_bill, other_bills)
            change_not_my_bill: List[int] = [0] + wacky_change_01(amount_of_change_to_give - 0, other_bills)

            # Now, pick the one that's better (i.e., produces fewer bills)
            #  Note that total _value_ should be amount_of_change_to_give, either way,
            #  but that "sum" counts the _number_ of bills, so we want the smaller sum.
            if sum(change_use_my_bill) > sum(change_not_my_bill):
                # postcondition(amount_of_change_to_give == amount_given)
                return change_not_my_bill
            else:
                # postcondition(amount_of_change_to_give == amount_given)
                return change_use_my_bill

        else:  # my bill is too big, no choice!
            change_not_my_bill: List[int] = [0] + wacky_change_01(amount_of_change_to_give - 0, other_bills)
            # postcondition(amount_of_change_to_give == amount_given)
            return change_not_my_bill


        
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
