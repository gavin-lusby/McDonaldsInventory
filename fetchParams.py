# This module is a modified version of recalibrateInventory after I noticed that a lot of the same functions
# could be applied to new shipment upload and remove product from stock. The functions in this module are a generalized
# version with the intent to fetch data regarding the amounts of each item from the user - Gavin

# {actioned} either means "received", "removed" or "counted", depending on what function is calling


import csvo


# Asks user the amount of containers and groups of given item {actioned}, and returns in list of length 2
# If the user indicated they want to exit the menu, returns ["exit",True/False] depending on whether they wanted to
# save or not
def ask_item_cons_grps(item_name, action_name):
    while True:
        item_con_amount = input(f"Enter the amount of {csvo.get_subdivs()[item_name][2]} of {item_name}"
                                f" {action_name}: ").strip()
        if item_con_amount == "exit":
            if csvo.check_if_save():
                return ["exit", True]
            else:
                return ["exit", False]
        if not item_con_amount.isdigit():
            print("Invalid integer amount. Please try again")
        else:
            item_con_amount = int(item_con_amount)
            break

    while True:
        item_grp_amount = input(f"Enter the amount of {csvo.get_subdivs()[item_name][3]} of {item_name}"
                                f" {action_name}: ").strip()
        if item_grp_amount == "exit":
            if csvo.check_if_save():
                return ["exit", True]
            else:
                return ["exit", False]
        if not item_grp_amount.isdigit():
            print("Invalid integer amount. Please try again")
        else:
            item_grp_amount = int(item_grp_amount)
            break

    return [item_con_amount, item_grp_amount]


# The point of this function is to ask a user for the amount of groups and containers {actioned} of any products
# In order to adjust stock level accordingly
def fetch_item_grps(action_name):
    changes = {}
    # This dict gets returned at the end in form {item_name: groups of product} for its outer
    # function to determine what to do with these values(either add to, remove from, or set as stock level

    while True:
        item_name = input(str(f"\nEnter \"all\" OR the plural name of one"
                              f" item {action_name} (ex. tomatoes): ")).lower().strip()
        if item_name == "all":
            if set(csvo.get_subdivs()) == set(changes):
                print("All items have already been accounted for. Exiting to menu.")
            else:
                for item in csvo.get_subdivs():
                    if item not in changes:  # Skips over items they already {actioned}
                        item_con_grp = ask_item_cons_grps(item, action_name)
                        if item_con_grp[0] == "exit":
                            if item_con_grp[1]:
                                input(f"Items {action_name}. Press enter to save changes.")
                                return changes
                            else:
                                input(f"Changes not saved. Press enter to continue.")
                                return {}

                        changes[item] = csvo.con_to_grp(item, item_con_grp[0]) + item_con_grp[1]

            if csvo.check_if_save():
                input(f"Items {action_name}. Press enter to save changes.")
                return changes
            else:
                input(f"Changes not saved. Press enter to continue.")
                return {}
        elif item_name == "exit":
            if csvo.check_if_save():
                input(f"Items {action_name}. Press enter to save changes.")
                return changes
            else:
                input(f"Changes not saved. Press enter to continue.")
                return {}
        # If the item mentioned is in the inventory, program asks user how much of the item they've {actioned}
        elif item_name in csvo.get_subdivs():
            if item_name in changes:
                print(f"(WARNING): Overwriting existing change for {item_name}")
            item_con_grp = ask_item_cons_grps(item_name, action_name)

            if item_con_grp[0] == "exit":
                if item_con_grp[1]:
                    input(f"Items {action_name}. Press enter to save changes.")
                    return changes
                else:
                    input(f"Changes not saved. Press enter to continue.")
                    return {}

            changes[item_name] = csvo.con_to_grp(item_name, item_con_grp[0]) + item_con_grp[1]

        else:  # If the user does not choose to exit entering items, and the item name isn't found in curr_inv (which
            # also doubles as a list of every valid item name), the following error message prints and the loop
            # restarts to ask for a valid item input again
            print("Invalid item name. Please try again.")
