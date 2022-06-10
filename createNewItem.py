import csvo
import resetScreen


# Function to reduce redundant code
def return_to_menu(checksave, a, b, c, d):
    if checksave:
        input(f"Items recorded. Press enter to save changes.")
        return [a, b]
    else:
        input(f"Changes not saved. Press enter to continue.")
        return [c, d]


# Modified version of ask_item_cons_grps from fetchParams.py
def ask_item_cons_grps(item_name, cons, grps):
    while True:
        uses_per_grp = input(f"How many uses of {item_name} are in each {grps}?: ").strip()
        if uses_per_grp == "exit":
            if csvo.check_if_save():
                return ["exit", True]
            else:
                return ["exit", False]
        if (not uses_per_grp.isdigit()):
            print("Invalid integer amount. Please try again.")
        elif int(uses_per_grp) == 0:
            print("Invalid integer amount. Please try again.")
        else:
            uses_per_grp = int(uses_per_grp)
            break

    while True:
        grps_per_con = input(f"How many {grps} of {item_name} are in each {cons}?: ").strip()
        if grps_per_con == "exit":
            if csvo.check_if_save():
                return ["exit", True]
            else:
                return ["exit", False]
        if not grps_per_con.isdigit():
            print("Invalid integer amount. Please try again.")
        elif int(grps_per_con) == 0:
            print("Invalid integer amount. Please try again.")
        else:
            grps_per_con = int(grps_per_con)
            break

    return [grps_per_con, uses_per_grp]


def create_new_item(user_name):
    resetScreen.reset_screen(True)  # resets screen with return to menu suggestion
    curr_inv = csvo.get_inv()
    new_inv = dict(curr_inv)  # copy of curr_inv
    subdivs = csvo.get_subdivs()
    new_subdivs = dict(subdivs)  # copy of subdivs
    print(f"Welcome, {user_name}")
    print("Please ensure you have read and understand help menu prompt before continuing here. If not navigate too \"HELP\" (input \"exit\" and then \"n\", then press enter, then input \"8\")")

    while True:

        new_item = input("\nPlease enter the name of the new item you would like to add to inventory (plural): ").lower().strip()

        if new_item == "exit":
            return return_to_menu(csvo.check_if_save(), new_inv, new_subdivs, curr_inv, subdivs)

        elif new_item == "all" or new_item == "":
            print("Invalid name. Please try again.")

        elif new_item in new_subdivs:
            print("Item already exists / was already defined.")

        elif not new_item.replace(' ', '').isalnum():  # Checks if item without any spaces is alphanumeric
            print("Item name must only contain letters, numbers, or space")

        else:
            while True:
                con_name = input("What is the name of one container of this item with singular(plural), ie. \"box(es)\": ").lower().strip()
                if len(con_name) < 4:
                    print("Name is too short.")
                elif con_name.replace(' ', '').isnumeric():
                    print("Name must contain letters.")
                else:
                    break

            if con_name == "exit":
                return return_to_menu(csvo.check_if_save(), new_inv, new_subdivs, curr_inv, subdivs)

            while True:
                grp_name = input("What is the name of one group of this item with singular(plural), ie. \"box(es)\": ").lower().strip()
                if len(grp_name) < 4:
                    print("Name is too short.")
                elif grp_name.replace(' ', '').isnumeric():
                    print("Name must contain letters.")
                else:
                    break

            if grp_name == "exit":
                return return_to_menu(csvo.check_if_save(), new_inv, new_subdivs, curr_inv, subdivs)
            uses_grps_cons = ask_item_cons_grps(new_item, con_name, grp_name)

            if uses_grps_cons[0] == "exit":
                return return_to_menu(uses_grps_cons[1], new_inv, new_subdivs, curr_inv, subdivs)

            new_subdivs[new_item] = [uses_grps_cons[0], uses_grps_cons[1], con_name, grp_name]
            new_inv[new_item] = 0
            print(f"{new_item} has been recorded with 0 {con_name} and 0 {grp_name}. Exit, save, and recalibrate"
                  f" to adjust values.")

def remove_item(user_name) :
    resetScreen.reset_screen(True)  # resets screen with return to menu suggestion
    curr_inv = csvo.get_inv()
    new_inv = dict(curr_inv)  # copy of curr_inv
    subdivs = csvo.get_subdivs()
    new_subdivs = dict(subdivs)  # copy of subdivs
    print(f"Welcome, {user_name}")
    while True:
        removing_item = input("Please enter the name of the new item you would like to add to inventory"
                         "(plural): ").lower().strip()

        if removing_item == "exit":
            return return_to_menu(csvo.check_if_save(), new_inv, new_subdivs, curr_inv, subdivs)

        elif removing_item in new_subdivs:
            print(f"Removal of  {removing_item} recorded.")
            del new_subdivs[removing_item]
            del new_inv[removing_item]
        else:
            print("Invalid name. Please try again.")
            