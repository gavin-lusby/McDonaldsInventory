# Manager or employees check stock (how much has been used, how much needs to be ordered)
import csvo
from resetScreen import reset_screen


# Edited by Isaac (2022-05-23)
# Edited by Isaac (2022-05-31) Officially works with dictionary and clean up


def printout(item, curr_inv):
    cons, grps = csvo.grp_to_con_grp(item, curr_inv[item])
    print(
        f"There are {cons} {csvo.get_subdivs()[item][2]} worth of {item} and {grps} {csvo.get_subdivs()[item][3]} worth "
        f"of {item}  ({csvo.grp_to_use(item, curr_inv[item])} uses).")


def check_stock(user_name):
    curr_inv = csvo.get_inv()
    list_of_items = []
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {user_name}")
    item_name = input(
        str("Enter \"all\" or the plural name of a specific item (ex. tomatoes) to view stock level: ")).lower()
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
            print("Invalid name. Please try again.")
        if len(list_of_items) == len(curr_inv):  # If user manually selects every item, treat as if they typed "all"
            item_name = "all"
        else:
            item_name = input(str("Enter \"all\" or the plural name of a specific item to view stock level: ")).lower()

# Should return nothing (prints current curr_inv, may return current curr_inv in later versions)
