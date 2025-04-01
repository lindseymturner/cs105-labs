from anagrams import anagrams, just_letters_as_lowercase
from anagrams import sort_letters
# importing sort_letters from anagrams rather than directly means this file and "anagrams" stay synchronized


# user interface for anagrams testing
def anagrams_ui():
    print("Enter sentence ")
    x: str = input()
    letters_of_x: str = just_letters_as_lowercase(x.lower())
    print("Sorted, that is: ", sort_letters(letters_of_x))
    print("Enter another sentence ")
    y: str = input()
    letters_of_y: str = just_letters_as_lowercase(y.lower())
    print("Sorted, that is: ", sort_letters(letters_of_y))

    if anagrams(letters_of_x, letters_of_y):
        print("They are anagrams")
    else:
        print("They are not anagrams")


anagrams_ui()
