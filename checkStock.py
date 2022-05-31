# Manager or employees check stock (how much has been used, how much needs to be ordered)
from resetScreen import reset_screen
import csvo


# Edited by Isaac (2022-05-23)
# Edited by Isaac (2022-05-31) Officially works with dictionary and clean up

def check(Dict):  # Checks if input is valid
    check = input("What item would you like to check: ").lower()
    while True:  # loops through until valid input
        if check in Dict or check == 'all' or check == 'exit':
            break
        else:
            item = input("\nItem not in inventory, please try again: ").lower()
    return item


def printout(curr_inv, subdivs, item):
    sub1 = curr_inv[item][1] // subdivs[item][2]  # Number of boxes
    sub2 = curr_inv[item][1] % subdivs[item][2]  # Number of remaining uses
    print(
        f"There are {sub1} {subdivs[item][3]} and {sub2} {subdivs[item][4]} of {subdivs[item][0]} ({curr_inv[item][1]} uses).")


def check_stock():
    curr_inv = csvo.getInv()
    subdivs = csvo.UBP  # Fetches subdivision table to convert units with
    reset_screen(True)

    search = check(subdivs)

    if search == "all":  # if user wants to see all
        for a in subdivs:
            printout(curr_inv, subdivs, a)

    elif search == 'exit':
        reset_screen(True)
        pass

    else:  # specific item
        printout(curr_inv, subdivs, search)

    pass
# Should return nothing (prints current curr_inv, may return current curr_inv in later versions)
