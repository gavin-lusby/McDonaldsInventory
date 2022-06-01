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
    cons, grps = csvo.grpToConGrp(item, curr_inv[item])
    print(f"There are {cons} {csvo.UBP[item][2]} worth of {item} and {grps} {csvo.UBP[item][3]} worth of {item}"
          f"  ({csvo.grpToUse(item, curr_inv[item])} uses).")


def check_stock():
    curr_inv = csvo.getInv()
    list_of_items = []
    reset_screen(True)
    item_name = input(str("Enter \"all\" or the plural name of a specific item to view stock level: ")).lower()
    while True:  # loops through until valid input
        reset_screen(True)

        if item_name == 'exit':
            return
        elif item_name == "all":  # if user wants to see all
            for item in curr_inv:
                printout(item, curr_inv)
            # This shows if they requested to view all items as they will not need to use check_stock again after
            # viewing all items
            input("Press enter to return to main menu.")
            return

        elif item_name in curr_inv:  # specific item
            if item_name not in list_of_items:
                list_of_items.append(item_name)
                list_of_items.sort()
            for item in list_of_items:
                printout(item, curr_inv)
        else:
            for item in list_of_items:
                printout(item, curr_inv)
            print("Invalid item name.")
        if len(list_of_items) == len(curr_inv):  # If user manually selects every item, treat as if they typed "all"
            item_name = "all"
        else:
            item_name = input(str("Enter \"all\" or the plural name of a specific item to view stock level: ")).lower()

# Should return nothing (prints current curr_inv, may return current curr_inv in later versions)
