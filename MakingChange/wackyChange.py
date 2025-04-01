"""


This an example that shows how choosing the highest bill first results in a higher sum of the resulting list. The best option here is to choose 2 fours.
>>> wacky(8,[5,4,1])
[0, 2, 0]

This is a pretty simple example.
>>> wacky(5,[5,1])
[1, 0]

>>> wacky(13,[10,5,1])
[1, 0, 3]

This example shows how any integer amount can work.
>>> wacky(13,[13,12,1])
[1, 0, 0]

>>> wacky(15,[10,3,1])
[1, 1, 2]

>>> wacky(10,[7,5,2,1])
[0, 2, 0, 0]

>>> wacky(10, [10])
[1]



"""


def wacky(change: int, denom: list) -> list:
    """
    This function takes a total amount of money and a list of bills and returns a list containing the lowest combination of bills in change.
    :param change: the value of money that the function will make change for.
    :param denom: contains all the bills available to make change with. these must be listed in descending order.
    :return: returns the best combination of bills (with the lowest sum)
    """

# this is my precondition
    # precondition(change > 0)
    # The total amount of money must be greater than.
    # The list of bills must be given in descending order.

    # base case
    # when there is only one bill option left, and there is no remainder when dividing change by the bill, then the function will return a list containing the number of bills that go into this amount.
    if len(denom) == 1:
        if change % denom[0] == 0:
            return [change // denom[0]]
    # if there is a remainder, this will raise an error because we do not have any coins, we can only make whole numbers for our change.
        else:
            raise ValueError
    # recursive step
    else:
        # x is a variable representing the number of times the first bill in the denom list is used.
        x = 0
        # I put a really high number in best list because it is unlikely that the sum of the numbers in optionList will be greater than the sum of bestList.
        bestList = [100000000000]
        # this a while loop that will keep running until the lens of denom is 1.
        # the program begins by selecting zero of the first bill in denom multiplied by the first bill value.
        while x * denom[0] <= change:
            # creates a new list
            # creates a new list for each possible combination of bills that create change for the total amount
            optionList = [x] + wacky(change - denom[0] * x, denom[1:])
            # the first time going through this loop, the sum of option list will definitely be less than the crazy high number in best list. However, as the program goes through all the possible
            # combinations, the combination with the lowest sum will end up in the final bestList.
            if sum(optionList) < sum(bestList):
                bestList = optionList
            x += 1
        return bestList





