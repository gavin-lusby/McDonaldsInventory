# Please see readme.md file for notes! :)


# Starting menu
# Runs for entire program; main piece of program

def start_menu():
    # Imports list of valid access accounts
    valid_accs = ["manager123", "manager321" "employee1", "employee2", "employee3"]

    acc = None

    # Keep looping till code is invalid, or "exit"
    while acc not in valid_accs:
        # Exits program if exit option chosen
        if acc == "exit":
            exit_menu()
        reset_screen(False)
        if acc is not None:  # Makes sure this code doesn't run the first time, only subsequent times
            print("Invalid code, please try again.")
        acc = input("Please enter your access code correctly: ").lower()

        reset_screen(False)
        print("Invalid code, try again")

    # Clears the screen to prevent access codes from being seen by other users (privacy concern)
    reset_screen(False)
    print(menus["funclist"])

    # Calls on appropriate function for user's desired action

    while True:
        act = input("SELECT AN ACTION: ").strip()
        act_valid = True
        if act == "1":
            csvo.setInv(add_to_inventory(acc))
        elif act == "2":
            csvo.setInv(recalib_inventory(acc))
        elif act == "3":
            check_stock()
        elif act == "4":
            csvo.setInv(remove_from_inventory(acc))
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
