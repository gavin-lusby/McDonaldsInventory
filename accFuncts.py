# accFuncts is short for Account Functions
from exitMenu import exit_menu
from os import path as ospath
from resetScreen import reset_screen
from sys import path as syspath


# This function creates user accounts ("accs") of two types: manager accounts and employee accounts (which both have different levels of access to certain functionalities within the program)


# Saves account settings menus from accMenus.txt to a list
acc_menus_lst = []

with open(ospath.join(syspath[0], "accMenus.txt"), 'r') as f:
    reader = f.read().splitlines()

for menuLine in list(reader):
    acc_menus_lst.append(menuLine)


def manager_check(userName, valid_accs):
    # Checks if user is a manager or an employee)
    if valid_accs[userName][0] == "manager":
        return True
    else:
        return False


def acc_menu(manager_status):
    # Saves menu items according to manager or employee status (ex. employees can only access employee actions, not manager-only actions)
  if manager_status == True:
      acc_menu = acc_menus_lst[0]
  else:
      acc_menu = acc_menus_lst[1]


  # Allows user to enter menu items allowed based on their status as a manager or employee
  while True:
    act = input("SELECT AN ACTION: ").strip()
    act_valid = True

    # Ensures only managers can access manager-only functions
    if act == "1" == True:
        change_pass()
    elif act == "2" and manager_status:
        create_acc()
    elif act == "3" and manager_status:
        delete_acc()
    elif act == "exit":
        exit_menu()
    else:
        act_valid = False
    reset_screen(False)
    print(str(acc_menu))
    if not act_valid:
        print("Invalid action. Please try again.")


def change_pass():
    pass

def create_acc():
    pass
  
def delete_acc():
    pass