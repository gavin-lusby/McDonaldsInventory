"""
Written by: Gavin, Isaac, Katie, Nikolas
Date: May 12-June 10, 2022
Purpose: Create a comprehensive inventory software for McDonald's employees and managers to use

GENERAL PROGRAMMING NOTES
- subdivs.csv does not get modified by the program. It should only be edited manually when adding new products.
"""

"""
Creates a dict for the sake of converting and storing unit types. First item in
each line(names of items) of csv becomes the key, and the rest of the items become
a list that is stored as the value associated with that key. The number values get converted from string to int
"""


# Starting menu
# Runs for entire program; main piece of program

def start_menu():
    # Imports list of valid access accounts
    validAccs = ["manager123", "manager321" "employee1", "employee2", "employee3"]

    # Clear screen, ask for code
    reset_screen(False)
    print(menus["funclist"])
    acc = input("Please enter your access code correctly: ").lower()

    # Keep looping till code is invalid, or "exit"
    while acc not in validAccs:
        # Exits program if exit option chosen
        if acc == "exit":
            exit_menu()
        reset_screen(False)
        print(menus["funclist"])
        print("Invalid code, please try again.")
        acc = input("Please enter your access code correctly: ").lower()

        reset_screen(False)
        print(menus["funclist"])
        print("Invalid code, try again")

    # Clears the screen to prevent access codes from being seen by other users (privacy concern)
    reset_screen(False)
    print(menus["funclist"])

    # Calls on appropriate function for user's desired action

    while True:
        act = input("SELECT AN ACTION: ")
        act_valid = True
        if act == "1":
            new_shipment_up()
        elif act == "2":
            csvo.setInv(recalib_inventory(acc))
        elif act == "3":
            check_stock()
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
    import csv
    import sys
    import os

    # Imports functions used
    from newShipmentUp import new_shipment_up
    from recalibInventory import recalib_inventory
    from checkStock import check_stock
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
