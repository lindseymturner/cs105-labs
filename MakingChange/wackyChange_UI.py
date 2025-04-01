from wackyChange import wacky

def wacky_UI() -> None:
    """
    This function takes an inputted amount of money and goes through all the possible combinations in change to find the one with the lowest sum.
    :return: returns the combination of change with the lowest sum.
    """

    user_input = int(input("What is the total amount you want to make change for?"))
    bills_number = int(input("How many types of bill options do you want?"))
    user_list = []
    for bills in range(bills_number):
        bill = int(input("What is the value of bill " + str(bills + 1) + "?"))
        user_list.append(bill)
    print(wacky(user_input, user_list))


wacky_UI()