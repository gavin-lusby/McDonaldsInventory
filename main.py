# Please see readme.md file for notes! :)

# Imports necessary libraries
import csv
from os import path as ospath
from sys import path as syspath


def start_menu():
    # This function prints and creates the start_menu that runs for the entire program (this is the main piece of the
    # program)

    # Creates dictionary of valid access accounts from users.csv (key = user's full name, value #1 = manager or
    # employee, value #2 = user's password)
    valid_accs = {}

    with open(ospath.join(syspath[0], "users.csv"), 'r') as f:
        reader = csv.reader(f)

        for user_acc in list(reader):
            valid_accs[user_acc[0].upper()] = [user_acc[1], user_acc[2], user_acc[3]]

    # Hashes all passwords (note: hash_file is a one-time run function; it's commented out below because we've
    # already used it to hash the passwords) hash_file(valid_accs)

    user_name = None
    user_pass = ""

    # Keep looping until user's full name is valid, or "exit" is chosen Note: user_name is stored in all uppercase as
    # case-sensitivity does not matter for full names and will make it easier for the user to correctly enter their
    # full name
    reset_screen(False)
    user_name = str(input("Please enter your full name correctly: ")).upper()

    while user_name not in valid_accs:
        reset_screen(False)
        print("Invalid name. Please try again.")
        user_name = str(input("Please enter your full name correctly: ")).upper()

        # Exits program if exit option chosen
        if user_name == "EXIT":
            exit_menu()

    # Keeps looping until user's password is valid (valid if equivalent to the stored hashed password) or "exit" is
    # chosen
    while hash_pass(user_pass, valid_accs.get(user_name)[2]) != valid_accs.get(user_name)[1]:
        # Exits program if exit option chosen
        if user_pass == "exit":
            exit_menu()
        reset_screen(False)

        # Prints error message if user's password is empty
        if user_pass != "":  # Makes sure this code doesn't run the first time, only subsequent times
            print("Invalid password. Please try again.")
        user_pass = str(input("Please enter your password correctly (case-sensitive): "))

        reset_screen(False)
        print("Invalid password. Please try again.")

    # Clears the screen to prevent passwords from being seen by other users (privacy concern)
    reset_screen(False)
    print(menus["funclist"])

    # Checks if the user is a manager or employee
    manager_status = manager_check(user_name, valid_accs)

    # Calls on appropriate function for user's desired action according to the menu
    while True:
        act = input("SELECT AN ACTION: ").strip()
        act_valid = True

        # Ensures only managers can access manager-only functions
        if act == "1" and manager_status:
            csvo.set_inv(add_to_inventory(user_name))
        elif act == "2" and manager_status:
            csvo.set_inv(recalib_inventory(user_name))
        elif act == "3" and manager_status:
            this_inv, this_subdiv = create_new_item(user_name)
            csvo.set_inv(this_inv)
            csvo.set_subdivs(this_subdiv)
        elif act == "4" and manager_status:
            this_inv, this_subdiv = remove_item(user_name)
            csvo.set_inv(this_inv)
            csvo.set_subdivs(this_subdiv)
        elif act == "5":
            check_stock(user_name)
        elif act == "6":
            csvo.set_inv(remove_from_inventory(user_name))
        elif act == "7":
            acc_menu(manager_status, user_name, valid_accs)
        elif act == "8":
            item_help()
        elif act == "exit":
            exit_menu()
        else:
            act_valid = False

        reset_screen(False)
        print(menus["funclist"])

        # Prints error message if the user enters anything other than 1-8 or exit
        if not act_valid:
            print("Invalid action. Please try again.")


# Only runs main if main is being run directly
if __name__ == "__main__":
    # Imports libraries used
    import os
    import sys

    # Imports functions used
    from editInventoryCount import recalib_inventory, remove_from_inventory, add_to_inventory
    from checkStock import check_stock
    from accFuncts import manager_check, acc_menu
    from exitMenu import exit_menu
    from passHash import hash_pass
    from resetScreen import reset_screen
    from itemHelp import item_help
    import csvo
    from createNewItem import create_new_item, remove_item

    # Imports from inventory.csv to create units_by_product, a list of the inventory
    with open(os.path.join(sys.path[0], "menus.txt"), 'r') as f:
        raw_menus = []

        """Python automatically assumes we don't want chars like \n
        to actually be a newline character, so it automatically adds
        an extra backslash. This removes that since when we have "\n"
        in menus we actually want a new line but we cant just press
        enter because each "menu" should only take up one line"""
        for menu in f.read().splitlines():
            raw_menus.append(menu.replace('\\n', '\n'))
    menus = {"header": raw_menus[0], "funclist": raw_menus[1], "accmenus": raw_menus[2]}

    # Run program
    start_menu()
