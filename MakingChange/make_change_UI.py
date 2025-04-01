from makeChange import make_change


def make_change_UI() -> None:
    """
    This function takes an inputted amount of money and passes it through the make_change function to let the user know how many of each bill they get.
    :return: it returns the output of the make_change function, which prints the amount of each bill
    """
    while True:
        user_input = int(input("Give an integer amount you want change for"))
        if user_input > 0:
            make_change(user_input)
        elif user_input == 0:
            break
make_change_UI()
