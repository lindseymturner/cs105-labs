"""

Examples of make_change function,
 which should print the number of $100 bills, $20 bills, $10 bills, $5 bills, and $1 bills to give,
 based on the total value of the change we want to provide.

Do not list bills that are not involved, i.e., don't have any $10 in the list below,
 but we would have a $10 if giving change for $330.

>>> make_change(348)   # o.k. to change "bill" to "bills" on the $5 below, if you want to
Give 3 $100 bills
Give 2 $20 bills
Give 1 $5 bills
Give 3 $1 bills

>>> make_change(10)
Give 1 $10 bills

>>> make_change(330)
Give 3 $100 bills
Give 1 $20 bills
Give 1 $10 bills

>>> make_change(348)
Give 3 $100 bills
Give 2 $20 bills
Give 1 $5 bills
Give 3 $1 bills

>>> make_change(1000)
Give 10 $100 bills

>>> make_change(1531)
Give 15 $100 bills
Give 1 $20 bills
Give 1 $10 bills
Give 1 $1 bills

This example would give you nothing:
>>> make_change(0)

"""

# Logic tries to get the standard Haverford "logic" module, provides some parts if it fails
from Logic import *


def make_change(amount_of_change_to_give: int) -> None:

    """
    the function takes in the amount of money you want to get change for and lets the user know how many of each bill
    :param amount_of_change_to_give: quantity of money you want to receive change for
    :return: prints out the quantity of bills used for change
    """

# precondition function only accepts dollar amounts greater than or equal to $0
    precondition(amount_of_change_to_give >= 0)
# integer divide the total money by 100 first to get the number of $100 bills
    how_many_hundreds = amount_of_change_to_give // 100
# subtract the amount we have in hundreds from the total and integer divide the remainder by 20 to get the amount of twenties
    how_many_twenties = (amount_of_change_to_give - (how_many_hundreds * 100)) // 20
# subtract the total amount we have in change so far from the total and integer divide by 10 to get the amount of tens we need
    how_many_tens = (amount_of_change_to_give - (how_many_hundreds * 100) - (how_many_twenties * 20)) // 10
# subtract the total amount we have in change so far from the total and integer divide by 5 to get amount of fives we need
    how_many_fives = (amount_of_change_to_give - (how_many_hundreds * 100) - (how_many_twenties * 20) - (how_many_tens * 10)) // 5
# subtract the total amount we have in change so far from the total the amount of ones we need
    how_many_ones = (amount_of_change_to_give - (how_many_hundreds * 100) - (how_many_twenties * 20) - (how_many_tens * 10) - (how_many_fives * 5))

# the amount of each type of bill must be greater than 1 in order for it to be included. i.e. if no $20 bills are needed, it won't say "Give $0 $20 bills", it will just leave out the $20 bills
    if how_many_hundreds > 0:
        print("Give", how_many_hundreds, "$100 bills")
    if how_many_twenties > 0:
        print("Give", how_many_twenties, "$20 bills")
    if how_many_tens > 0:
        print("Give", how_many_tens, "$10 bills")
    if how_many_fives > 0:
        print("Give", how_many_fives, "$5 bills")
    if how_many_ones > 0:
        print("Give", how_many_ones, "$1 bills")


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
