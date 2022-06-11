# For all functions that modify the stock level in any way through user input

# Edited by Katie (2022-05-19)
# Edited by Katie, Gavin (2022-05-24)
# Edited by Katie (2022-05-30)
# Edited by Katie, Gavin (2022-05-31)

import fetchParams
from csvo import get_inv
from resetScreen import reset_screen


# For manager to recalibrate stock level values(in the case of employees negligence skewing stock numbers over time)
def recalib_inventory(user_name):
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {user_name}, setting current inventory.")

    curr_inv = get_inv()  # Fetches current inventory
    changes = fetchParams.fetch_item_grps("counted")
    for item in list(changes):
        curr_inv[item] = changes[item]

    return curr_inv


# If employee is removing product from shelves, they document it here
def remove_from_inventory(user_name):
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {user_name}, removing used items from current stock.")
    curr_inv = get_inv()  # Fetches current inventory
    changes = fetchParams.fetch_item_grps("removed/consumed")
    for item in list(changes):
        this_change = curr_inv[item] - changes[item]
        if this_change < 0:
            input(f"Warning: Negative item count detected for {item}. Recalibration required. Press enter to continue.")
        curr_inv[item] = this_change

    return curr_inv


# For manager to document incoming shipment to add to stock levels(without the need to recount existing product)
def add_to_inventory(user_name):
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {user_name}, adding shipment to current stock.")
    curr_inv = get_inv()  # Fetches current inventory
    changes = fetchParams.fetch_item_grps("received")
    for item in list(changes):
        this_change = curr_inv[item] + changes[item]
        if this_change < 0:
            input(f"Warning: Negative item count detected for {item}. Recalibration required. Press enter to continue.")
        curr_inv[item] = this_change

    return curr_inv
