from typing import List


# def sort_letters(l: str) -> str:
#    """
#    >>> sort_letters('abc')
#    'abc'
#    >>> sort_letters('cab')
#    'abc'
#    >>> sort_letters('aba')
#    'aab'
#    """
#    letters: List[str] = list(l)
#    inorder: List[str] = sorted(letters)  # use Python's built-in sort. This is usually the best thing to do.
#    result: str = "".join(inorder)  # join appends the "" and all the letters in inorder
#    return result

def sort_letters(unsorted: str) -> str:
    """
>>> sort_letters('OpenAI')
'aeinop'
>>> sort_letters('bca')
'abc'
>>> sort_letters('new york times')
'eeikmnorstwy'

    """
    unsorted = unsorted.lower()
    # Convert the string to a list of characters for in-place sorting
    char_list = list(unsorted)
    n = len(char_list)

    # Selection sort
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if char_list[j] < char_list[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        char_list[i], char_list[min_index] = char_list[min_index], char_list[i]

    # Convert the sorted list of characters back to a string
    sorted_str = ''.join(char_list)
    sorted_str = sorted_str.strip()

    return sorted_str


def sort_letters2(unsorted: str) -> str:
    """
>>> sort_letters2('OpenAI')
'aeinop'

>>> sort_letters2('bca')
'abc'

>>> sort_letters2('new york times')
'eeikmnorstwy'

    """
    unsorted = unsorted.lower()
    # Convert the string to a list of characters for in-place sorting
    #assert unsorted.isalpha()
    char_list = list(unsorted)
    n = len(char_list)

    # Insertion sort
    for i in range(1, n):
        key = char_list[i]
        j = i - 1

        while j >= 0 and key < char_list[j]:
            char_list[j + 1] = char_list[j]
            j -= 1

        char_list[j + 1] = key

    # Convert the sorted list of characters back to a string
    sorted_str = ''.join(char_list)
    sorted_str = sorted_str.strip()

    return sorted_str
