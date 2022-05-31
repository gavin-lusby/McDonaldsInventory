# Manager update for resetting values of items in inventory This is used in case employees forget to log a removed
# item or the updated inventory is otherwise incorrect/out-of-date and requires a manual recount and reset

# Edited by Katie (2022-05-19)
# Edited by Katie, Gavin (2022-05-24)
# Edited by Katie (2022-05-30)
# Edited by Katie, Gavin (2022-05-31)

from resetScreen import reset_screen
import csvo


# Check if the user has chosen to save (returns True) or not (returns False)
def checkIfSave():
    save_bool = input("Do you want to save changes? (y/n): ").lower()
    if save_bool == "n":
        return False
    else:
        # If user indicates anything but 'n', assume 
        # they want to save changes as to ensure if they accidently
        # type something that is neither n, nor y, the program is saving                    
        # the changes 
        return True


def recalib_inventory(acc):
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {acc}")

    curr_inv = csvo.getInv()  # Fetches current inventory
    new_inv = dict(curr_inv)  # Creates copy of curr_inv to be edited as each
    # product is recalibrated
    # Update curr_inv = new_inv if user saves changes

    while True:
        item_name = input(str("Enter the plural name of one item taken (ex. tomatoes): ")).lower()

        if item_name == "exit":
            if checkIfSave:
                return new_inv
            else:
                return curr_inv
        # If the item mentioned is in the inventory, program asks user how much of the item they've taken off the
        # inventory shelves
        if item_name in curr_inv:
            item_con_amount = int(input(f"Enter the amount of {csvo.UBP[item_name][2]} taken for this item: "))
            if item_con_amount == "exit":
                if checkIfSave:
                    return new_inv
                else:
                    return curr_inv
            # For now, we are assuming that the user will only enter a valid integer, since in real life they would
            # have a keypad and only be able to enter integers
            item_grp_amount = int(input(f"Enter the amount of {csvo.UBP[item_name][3]} taken for this item: "))
            if item_grp_amount == "exit":
                if checkIfSave:
                    return new_inv
                else:
                    return curr_inv

            new_inv[item_name] = csvo.conToGrp(item_name, item_con_amount) + item_grp_amount

        else:  # If the user does not choose to exit entering items, and the item name isn't found in curr_inv (which
            # also doubles as a list of every valid item name), the following error message prints and the loop
            # restarts to ask for a valid item input again
            print("Invalid item name.")
