"""
In this case we have a different letter, other than u or q, after.
>>> u_less_qs("qintar")
I found a q followed by i.

In this case we have a quotation mark after.
>>> u_less_qs("q'doba")
I found a q followed by '.

In this case we have two spaces after the q.
>>> u_less_qs("put q ")
I found a q followed by  .

In this case we have another q after.
>>> u_less_qs("qqq")
I found a q followed by q.
I found a q followed by q.

"""


def u_less_qs(text: str) -> None:
    """
    This function finds situations where a q is followed by something other than a q in a string.
    :param text: The string that is inputted into the function.
    :return: Prints out any characters following q other than u.
    """
# we start by looking at the first character in the string (index = 0)
    index = 0

# the position of the last character must be less than the length of the text because the index starts at 0
    while index < len(text):

# if the function finds a q in the string and it is not the last letter in the string
        if text[index] == "q" and index + 1 < len(text):

# if the letter following q is not u, then print what directly follows q.
            if text[index + 1] != "u":
                print("I found a q followed by", text[index + 1] + ".")
# when we run the function again, we will look at the next index position and run it through the function. this will repeat until we are at the end of the string.
        index = index + 1


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
