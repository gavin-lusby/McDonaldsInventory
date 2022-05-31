# Employee update for taking items from shelf

# Edited by Katie (2022-05-19)
# Edited by Katie, Gavin (2022-05-24)
# Edited by Katie (2022-05-30)
# Edited by Katie, Gavin (2022-05-31)

from resetScreen import reset_screen
import csvOperations

def checkIfSave(a, b):
    save_bool = input("Do you want to save changes? (y/n): ").lower()
    if save_bool == "n":
        return a
    else: 
        # If user indicates anything but 'n', assume 
        # they want to save changes as to ensure if they accidently
        # type something that is neither n, nor y, the program is saving                    
        # the changes 
        return b

def recalib_inventory(acc):
    reset_screen(True) # resets screen with return to menu suggestion
    print(f"Welcome, {acc}")
  
    curr_inv = csvOperations.getInv() # Fetches current inventory
    new_inv = dict(curr_inv) # Creates copy of curr_inv to be edited as each
    # product is recalibrated
  # Update curr_inv = new_inv if user saves changes

    while True:
        item_name = input(str("Enter the name of one item taken: ")).lower()
        
        if item_name == "exit":
             checkIfSave(curr_inv, new_inv)

        # If the item mentioned is in the inventory, program asks user how much of the item they've taken off the inventory shelves
        if item_name in curr_inv:
            item_amount = input(int(f"Enter the amount of {csvOperations.UBP[item_name][3]} taken for this item: "))
            if item_amount == "exit":
                 checkIfSave(curr_inv, new_inv)
            # For now, we are assuming that the user will only enter a valid integer, since in real life they would have a keypad and only be able to enter integers
            new_inv[item_name] = item_amount
          
        else: # If the user does not choose to exit entering items, and the item name isn't found in curr_inv (which also doubles as a list of every valid item name), the following error message prints and the loop restarts to ask for a valid item input again
          print("Invalid item name.")
      
"""    # Check if necessary?
    reset_screen(True)

    print(f"Welcome, {acc}")

    set_of_items = set(curr_inv)
    requests = {"pickle": 2}
    updates = []

    # curr_inv and new_inv are mutable since they are both dicts; makes a copy of curr_inv so changes to new_inv dont
    # affect curr_inv
    new_inv = dict(curr_inv)

    # Takes requests from employee user
    while True:
        item_name = input("Enter one item taken: ").lower()

        if item_name == "exit":
            # Add later: or item_container_value.lower() == "exit"
            save_bool = input("Do you want to save changes? (y/n): ").lower()
            if save_bool == "n":
                return curr_inv
            else:
                return new_inv
        elif item_name in set_of_items:
            # In the real world, input would be done via keypad so possible input is limited to exit or an integer.
            # We are not accounting for if the user types something like "hello", which is possible in-console but
            # not in a real-world scenario
            item_container_value = input(f"Enter the amount of {item_name[2]} {item_name} taken as a number: ")
            if item_container_value == "exit":
                save_bool = input(
                    "Do you want to save changes? (this particular item will not be changed regardless since you have "
                    "not entered a value yet) (y/n): ").lower()
                if save_bool == "n":
                    return curr_inv
                else:
                    return new_inv
            else:
                item_container_value = int(item_container_value)

            item_uses_value = input(f"Enter the amount of {item_name[3]} of {item_name} taken as a number: ")
            if item_uses_value == "exit":
                save_bool = input(
                    "Do you want to save changes? (this particular item will not be changed regardless since you have "
                    "not entered a value yet) (y/n): ").lower()
                if save_bool == "n":
                    return curr_inv
                else:
                    return new_inv
            else:
                item_uses_value = int(item_uses_value)

        else:
            print("Invalid item name. Please try again.")
        # updates.append(requests)

# TO FIGURE OUT:
# - Make save_bool usage more efficient (just use it once, change if statements' conditions)"""
