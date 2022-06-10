# Please see readme.md file for notes! :)

import csv
from os import path as ospath
from sys import path as syspath


# Starting menu
# Runs for entire program; main piece of program

def start_menu():
    # Creates dictionary of valid access accounts from users.csv (key = user's full name, value #1 = manager or
    # employee, value #2 = user's password)
    valid_accs = {}

    with open(ospath.join(syspath[0], "users.csv"), 'r') as f:
        reader = csv.reader(f)

        for user_acc in list(reader):
            valid_accs[user_acc[0].upper()] = [user_acc[1], user_acc[2], user_acc[3]]

    # Hashes all passwords (note: hash_file is a one-time run function)
    #hash_file(valid_accs)

    user_name = None
    user_pass = ""

    # Keep looping until user's full name is valid, or "exit" is chosen user_name is stored in all uppercase as
    # case-sensitivity does not matter for full names and will make it easier for the user to correctly enter their
    # full name
    while user_name not in valid_accs:
        reset_screen(False)
        user_name = str(input("Please enter your full name correctly: ")).upper()

        # Exits program if exit option chosen
        if user_name == "EXIT":
            exit_menu()
        reset_screen(False)
        if user_name is not None:  # Makes sure this code doesn't run the first time, only subsequent times
            print("Invalid name. Please try again.")

        reset_screen(False)
        print("Invalid name. Please try again.")

    # Keep looping until user's password is valid, or "exit" is chosen
    while hashlib.sha512(user_pass.encode()).hexdigest() != valid_accs.get(user_name)[1]:
        # Exits program if exit option chosen
        if user_pass == "exit":
            exit_menu()
        reset_screen(False)
        if user_pass != "":  # Makes sure this code doesn't run the first time, only subsequent times
            print("Invalid password. Please try again.")
        user_pass = str(input("Please enter your password correctly (case-sensitive): "))

        reset_screen(False)
        print("Invalid password. Please try again.")

    # Clears the screen to prevent passwords from being seen by other users (privacy concern)
    reset_screen(False)
    print(menus["funclist"])
  
    manager_status = manager_check(user_name, valid_accs)

    # Calls on appropriate function for user's desired action

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
        
        if not act_valid:
            print("Invalid action. Please try again.")
          

# Only runs main if main is being run directly
if __name__ == "__main__":
    # Import libraries used
    import hashlib
    import os
    import sys
  
    # Import functions used
    from editInventoryCount import recalib_inventory, remove_from_inventory, add_to_inventory
    from checkStock import check_stock
    from accFuncts import manager_check, acc_menu
    from exitMenu import exit_menu
    from passHash import hash_file
    from resetScreen import reset_screen
    from itemHelp import item_help
    import csvo
    from createNewItem import create_new_item, remove_item

    # Importing from inventory.csv to create list of inventory units_by_product

    with open(os.path.join(sys.path[0], "menus.txt"), 'r') as f:
        raw_menus = []

        """Python automatically assumes we don't want chars like \n
        to actually be a newline character, so it automatically adds
        an extra backslash. This removes that since when we have "\n"
        in menus we actually want a new line but we cant just press
        enter because each "menu" should only take up one line"""
        for menu in f.read().splitlines():
            raw_menus.append(menu.replace('\\n', '\n'))
    menus = {"header": raw_menus[0], "funclist": raw_menus[1]}
    # Run program
    start_menu()
