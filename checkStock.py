# Manager or employees check stock (how much has been used, how much needs to be ordered)
from resetScreen import reset_screen
import csvo


# Edited by Isaac (2022-05-23)
# Edited by Isaac (2022-05-31) Officially works with dictionary and clean up

def check(Dict):  # Checks if input is valid
    check = input("What item would you like to check: ").lower()
    while True:  # loops through until valid input
        item_name = input(str("Enter the plural name of one item taken (ex. tomatoes): ")).lower()
        if check in Dict or check == 'all' or check == 'exit':
            break
        else:
            item = input("\nItem not in inventory, please try again: ").lower()
    return item


"""    while True:
        item_name = input(str("Enter the plural name of one item taken (ex. tomatoes): ")).lower()

        if item_name == "exit":
            if checkIfSave:
                return new_inv
            else:
                return curr_inv
        # If the item mentioned is in the inventory, program asks user how much of the item they've taken off the
        # inventory shelves"""


def printout(item, curr_inv):
    cons, grps = csvo.grpToConGrp(curr_inv[item])
    print(f"There are {cons} {csvo.UBP[item][2]} and {grps} {csvo.UBP[item][3]} of {item} \
    ({csvo.grpToUse(curr_inv[item])} uses).")


def check_stock():
    curr_inv = csvo.getInv()
    reset_screen(True)

    while True:  # loops through until valid input
        item_name = input(str("Enter the plural name of one item taken (ex. tomatoes): ")).lower()

        if item_name == "all":  # if user wants to see all
            for item_name in curr_inv:
                printout(item_name, curr_inv)

        elif item_name == 'exit':
            reset_screen(True)
            pass

        else:  # specific item
            printout(curr_inv, search)

    pass
# Should return nothing (prints current curr_inv, may return current curr_inv in later versions)
