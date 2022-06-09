# Please see readme.md file for notes! :)

import csv
from os import path as ospath
from sys import path as syspath


# Starting menu
# Runs for entire program; main piece of program

def start_menu():
    # Imports dictionary of valid access accounts from users.csv (key = user's full name, value #1 = manager or employee, value #2 = user's password)
    valid_accs = {}
  
    with open(ospath.join(syspath[0], "users.csv"), 'r') as f:
      reader = csv.reader(f)

      for userAcc in list(reader):
          valid_accs[userAcc[0].upper()] = [userAcc[1],userAcc[2]]

    userName = None
    userPass = None

    # Keep looping until user's full name is valid, or "exit" is chosen
    # userName is stored in all uppercase as case-sensitivity does not matter for full names and will make it easier for the user to correctly enter their full name
    while userName not in valid_accs:
        reset_screen(False)
        userName = str(input("Please enter your full name correctly: ")).upper()
      
      # Exits program if exit option chosen
        if userName == "EXIT":
            exit_menu()
        reset_screen(False)
        if userName is not None:  # Makes sure this code doesn't run the first time, only subsequent times
            print("Invalid name, please try again.")
        
        reset_screen(False)
        print("Invalid name, please try again.")

    # Keep looping until user's password is valid, or "exit" is chosen
    while userPass != valid_accs.get(userName)[1]:
        # Exits program if exit option chosen
        if userPass == "exit":
            exit_menu()
        reset_screen(False)
        if userPass is not None:  # Makes sure this code doesn't run the first time, only subsequent times
            print("Invalid password, please try again.")
        userPass = str(input("Please enter your password correctly (case-sensitive): "))

        reset_screen(False)
        print("Invalid password, please try again.")
      
    # Clears the screen to prevent passwords from being seen by other users (privacy concern)
    reset_screen(False)
    print(menus["funclist"])

    # Calls on appropriate function for user's desired action

    while True:
        act = input("SELECT AN ACTION: ").strip()
        act_valid = True


        # Ensures only managers can access manager-only functions
        if act == "1" and manager_check(userName,valid_accs) == True:
            csvo.setInv(add_to_inventory(userName))
        elif act == "2" and manager_check(userName,valid_accs) == True:
            csvo.setInv(recalib_inventory(userName))
        elif act == "3":
            check_stock()
        elif act == "4":
            csvo.setInv(remove_from_inventory(userName))
        elif act == "5":
            pass
        elif act == "exit":
            exit_menu()
        else:
            act_valid = False
        reset_screen(False)
        print(menus["funclist"])
        if not act_valid:
            print("Invalid action, try again")


# Only runs main if main is being run directly
if __name__ == "__main__":
    import sys
    import os
    # Import functions used
    from editInventoryCount import recalib_inventory, remove_from_inventory, add_to_inventory
    from checkStock import check_stock
    from createAccs import manager_check
    from exitMenu import exit_menu
    from resetScreen import reset_screen
    import csvo  

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
