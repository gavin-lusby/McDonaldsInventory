# For all functions that modify the stock level in any way through user input

# Edited by Katie (2022-05-19)
# Edited by Katie, Gavin (2022-05-24)
# Edited by Katie (2022-05-30)
# Edited by Katie, Gavin (2022-05-31)
import fetchparams
from resetScreen import reset_screen
from csvo import getInv


# For manager to recalibrate stock level values(in the case of employees neglegence skewing stock numbers over time)
def recalib_inventory(acc):
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {acc}")

    curr_inv = getInv()  # Fetches current inventory
    changes = fetchparams.fetch_item_cons_grps("counted")
    for item in list(changes):
        curr_inv[item] = changes[item]

    return curr_inv


# If employee is removing product from shelves, they document it here
def remove_from_inventory(acc):
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {acc}")
    curr_inv = getInv()  # Fetches current inventory
    changes = fetchparams.fetch_item_cons_grps("removed/consumed")
    for item in list(changes):
        this_change = curr_inv[item] - changes[item]
        if this_change < 0:
            input(f"Warning: Negative item count detected for {item}. Recalibration required. Press enter to continue.")
        curr_inv[item] = this_change

    return curr_inv


# For manager to document incoming shipment to add to stock levels(without the need to recount existing product)
def add_to_inventory(acc):
    reset_screen(True)  # resets screen with return to menu suggestion
    print(f"Welcome, {acc}")
    curr_inv = getInv()  # Fetches current inventory
    changes = fetchparams.fetch_item_cons_grps("received")
    for item in list(changes):
        this_change = curr_inv[item] + changes[item]
        if this_change < 0:
            input(f"Warning: Negative item count detected for {item}. Recalibration required. Press enter to continue.")
        curr_inv[item] = this_change

    return curr_inv
