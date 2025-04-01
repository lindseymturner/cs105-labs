"""

This file should define the value_of_change, can_i_buy_this, and how_many_can_i_buy functions.
Examples of each are given below, with descriptions.

Name:Lindsey Turner
email: lturner@haverford.edu
Lab Partner's Name: Matt Dahl and Logan Brown
Lab Partner's email: mdahl@haverford.edu and lrbrown@haverford.edu

===================================================================================================
The value_of_change function gives the total value (in dollars)
of a given quantity of quarters, dimes, nickels, and pennies.

For example, if we have three quarters, that's worth 0.75 dollars
>>> value_of_change(3, 0, 0, 0)
0.75

Sometimes, these tests will reveal the imperfection of the computer's
representation of whole numbers, so we may want to round these off
to two decimal places, using Python's "round" function, like so:
>>> round(value_of_change(3, 0, 0, 0), 2)
0.75

If we have three quarters, eight dimes, four nickels, and six pennies, that's worth $1.81
>>> round(value_of_change(3, 8, 4, 6), 2)
1.81

Of course, if I have $12 in bills, along with that change, I should have $13.81
>>> round(value_of_change(3, 8, 4, 6) + 12.00, 2)
13.81

If we have no coins as all, that's worth $0.00
>>> round(value_of_change(0, 0, 0, 0), 2)
0.0


===================================================================================================
The can_i_buy_this function returns true if the given quantities
of quarters, dimes, nickels, and pennies, can buy at least one item of a given price.
(Otherwise, it returns false.)

If we have three quarters, eight dimes, four nickels, and six pennies, and want to buy
something that costs $1.99, the answer should be false (meaning no, we can't buy it)
>>> can_i_buy_this(3, 8, 4, 6, 1.99)
False

If we want to buy something costing $1.19 with those coins, the answer should be true (we can)
>>> can_i_buy_this(3, 8, 4, 6, 1.19)
True

If the thing cost 17 cents, we still just get true as the answer, even though we could buy several.
>>> can_i_buy_this(3, 8, 4, 6, 0.17)
True


===================================================================================================
The how_many_can_i_buy function is similar to the can_i_buy_this,
but it tells us how many (or, of course, zero if I can't buy any).
We'll only count the integer part of the purchase, e.g., if we can
afford to buy 2.37 smartphones, we'll just want to get two, not
two plus a bunch of pieces (this reduces issues of rounding, too).

If we have three quarters, eight dimes, four nickels, and six pennies, and want to buy
something that costs $1.99, the answer should be zero, since we can't buy it
>>> int(how_many_can_i_buy (3, 8, 4, 6, 1.99))
0

If we want to buy something costing $1.19 with those coins, we can get one
>>> int(how_many_can_i_buy(3, 8, 4, 6, 1.19))
1

If the thing cost 17 cents, we can get ten of them
>>> int(how_many_can_i_buy(3, 8, 4, 6, 0.17))
10

"""


def value_of_change(howManyQuarters: int, howManyDimes: int, howManyNickels: int, howManyPennies: int) -> float:
    return (0.25 * howManyQuarters) + (.1 * howManyDimes) + (.05 * howManyNickels) + (.01 * howManyPennies)  # We'll need to do better than this! (though, it is an interesting case...)


def can_i_buy_this(howManyQuarters: int, howManyDimes: int, howManyNickels: int, howManyPennies: int, price: float) -> bool:
    x = value_of_change(howManyQuarters, howManyDimes, howManyNickels, howManyPennies)# We'll need to do better than this!
    if x>= price:
        return True
    else:
        return False










# Work on the function below without looking at anyone else's Python code,
#  and without having other students look at yours.
# (It's fine to talk to teaching assistants and instructors, though.)

# Note: it's fine to make this return float or int, whichever you like.
def how_many_can_i_buy(howManyQuarters: int, howManyDimes: int, howManyNickels: int, howManyPennies: int, price: float) -> float:
    money = value_of_change(howManyQuarters , howManyDimes , howManyNickels, howManyPennies)
    n = money / price
    return n


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
