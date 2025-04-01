"""

>>> is_palindrome("abcba")
True

>>> is_palindrome("abcxy")  
False

There's also a version that takes out spaces and punctuation:
>>> is_palindrome('aBc b a!')   # without the space and !, it would be
False

>>> is_palindrome_after_reducing_to_lowercase_letters('aBc b a!')
True

NOTE: You don't have to write that second one, it should work
as soon an your is_palindrome works. But, you can use either form
for your own tests. It just combines your function with the following:

>>> reduce_to_lower_case_letters('aBc b a!')
'abcba'

>>> is_palindrome("kayak")
True

A space inside of a palindrome doesn't matter.
>>> is_palindrome_after_reducing_to_lowercase_letters("le vel")
True

A captial inside of a palindrome doesn't matter.
>>> is_palindrome_after_reducing_to_lowercase_letters("rAdar")
True

An even number of lettters example.
>>> is_palindrome("hannah")
True


>>> is_palindrome("hanzah")
False

Dashes inside of a palindrome don't matter.
>>> is_palindrome_after_reducing_to_lowercase_letters("ro-tator")
True

"""

from Logic import precondition, postcondition

def precondition(value_of_precondition):
    if (value_of_precondition != True):
        raise "Precondition failed"


def postcondition(value_of_postcondition):
    if (value_of_postcondition != True):
        raise "Postcondition failed"


def is_palindrome(string):
#base case - if there is 1 letter or less in the string it will always be a palindrome
    if len(string) <= 1:

#base answer
        return True

#recursive case - if the first and last letters are the same it will return the string to the function without the first and last letters
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])

#if the first and last letters of the string are not the same, it cannot be a palindrome
    else:
        return False


# Students should not need to edit this function
# This is "top-down design" using two sub-functions:
#   * The is_palindrome function you'll write, and
#   * the lower_case_letters function, we provided below
def is_palindrome_after_reducing_to_lowercase_letters(any_string: str) -> bool:
    return is_palindrome(reduce_to_lower_case_letters(any_string))
    

# User interface for the palindrome function
def palindrome_UI():
    print("Type 1 to run your test-suite, press 2 to type in your own tests:")
    answer = input()
    if not (answer in ['2']):
        _test()
    else:
        print("Please input a possible palindrome: ")
        trial_text = input()
        letters_only = reduce_to_lower_case_letters(trial_text)
        if is_palindrome(letters_only):
            print("The text '" + letters_only + "' is a palindrome")
        else:
            print("The text '" + letters_only + "' is not a palindrome.")


# The following was done with basic-recursive design, as an example,
#  though there might be library functions we could have used
def reduce_to_lower_case_letters(text: str) -> str:
    """
        make something all lower case letters, e.g.

    >>> reduce_to_lower_case_letters('kayak')
    'kayak'

    >>> reduce_to_lower_case_letters('A man, a plan, a canal: Panama!')
    'amanaplanacanalpanama'
    """
    if text == '':
        return ''
    else:
        first = text[0]
        rest  = text[1:len(text)]  # or, equivalent, text[1:]
        if first in 'abcdefghijklmnopqrstuvwxyz':  # already lower case
            return first + reduce_to_lower_case_letters(rest)
        elif first in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # upper-case
            # first.lower() turns, for example, "D" into "d"
            return first.lower() + reduce_to_lower_case_letters(rest)
        else:   # otherwise skip first element, as it's not a letter
            return reduce_to_lower_case_letters(rest)


# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")


# tests may or may not be chosen by the user interface...
if __name__ == "__main__":
    palindrome_UI()

