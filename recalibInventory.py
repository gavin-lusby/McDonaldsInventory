# Employee update for taking items from shelf

# Edited by Katie (2022-05-19)
# Edited by Katie, Gavin (2022-05-24)
# Edited by Katie (2022-05-30)

from resetScreen import reset_screen

def recalib_inventory(acc, curr_inv):
    reset_screen(True) # reset's screen with return to menu suggestion
    print(f"Welcome, {acc}")


  
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
