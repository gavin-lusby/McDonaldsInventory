# accFuncts is short for Account Functions
from csvo import check_if_save
from exitMenu import exit_menu
from os import path as ospath
from passHash import acc_file_update, hash_pass
from resetScreen import reset_screen
from sys import path as syspath


# This function creates user accounts ("accs") of two types: manager accounts and employee accounts (which both have different levels of access to certain functionalities within the program)


# Saves account settings menus from accMenus.txt to a list
acc_menus_lst = []

with open(ospath.join(syspath[0], "accMenus.txt"), 'r') as f:
    reader = f.read().splitlines()
  
for menuLine in list(reader):
    acc_menus_lst.append(menuLine.replace('\\n', '\n'))

def manager_check(user_name, valid_accs):
    # Checks if user is a manager or an employee)
    if valid_accs[user_name][0] == "manager":
        return True
    else:
        return False


def print_menu(manager_status):
      # Saves menu items according to manager or employee status (ex. employees can only access employee actions, not manager-only actions)
    
    if manager_status == True:
        for line in range(len(acc_menus_lst)):
          print(acc_menus_lst[line])
    else:
        print(acc_menus_lst[0])


def acc_menu(manager_status, valid_accs):

    # Initial menu print
    reset_screen(False)
    print_menu(manager_status)
    
    # Allows user to enter menu items allowed based on their status as a manager or employee
    while True:
      act = input("SELECT AN ACTION: ").strip()
      act_valid = True
  
      # Ensures only managers can access manager-only functions
      if act == "1":
          change_pass()
      elif act == "2" and manager_status:
          create_acc(valid_accs)
      elif act == "3" and manager_status:
          delete_acc()
      elif act == "exit":
          reset_screen(True)
          break
      else:
          act_valid = False
        
      reset_screen(False)
      print_menu(manager_status)
      
      if not act_valid:
          print("Invalid action. Please try again.")


def change_pass():
    #change_pass = input(str(""))

    #acc_file_update
    pass


def create_acc(valid_accs):
    new_acc = []
  
    # Creates new user's username
    while True:
        new_name = str(input("Enter full name: ")).upper().strip()
  
        # Prevents multiple accounts under the same name
        while new_name in valid_accs:
            print ("This user already exists. Please try again or type \"exit\".")
            new_name = str(input("Enter full name: ")).upper().strip()
  
        # User can choose to re-enter username as many times as they would like
        if check_if_save():
            input("Username changes saved. Press enter to continue.")
            new_acc.append(new_name)
  
            # Asks user to choose manager status
            if create_acc_status(valid_accs, new_acc) != None:
                if create_acc_pass(valid_accs, new_acc) != None:
                    # Writes new user (name, status, and password to users.csv)
                    valid_accs[new_name] = [create_acc_status(valid_accs, new_acc), create_acc_pass(valid_accs, new_acc)]
                    acc_file_update(valid_accs)
                  
                    print(f"{create_acc_status(valid_accs, new_acc)} {new_name} saved.")
                else:
                  input("Create new account cancelled. Press enter to continue.")
                  reset_screen(True)
                  break
            else:
                input("Create new account cancelled. Press enter to continue.")
                reset_screen(True)
                break
                  
        else:
            input("Create new account cancelled. Press enter to continue.")
            reset_screen(True)
            break

      
def create_acc_status(valid_accs, new_acc):
    # Allows user to enter manager/employee status
    while True:
        new_status = str(input("Is this user a manager? (y/n): ")).lower().strip()
  
        if new_status == "y":
            new_status = "manager"
        elif new_status == "n":
            new_status = "employee"

        else:
          print("Invalid response.")


        # Checks if user would like to save changes
        if check_if_save():
            input("Status changes saved. Press enter to continue.")
            new_acc.append(new_status)
            return [new_status]
            break
          
        else:
            return None


def create_acc_pass(valid_accs, new_acc):
    # Creates new user's password
    while True:
        new_pass = str(input("Enter password (case-sensitive): "))
        
        if check_if_save():
            input("Password changes saved. Press enter to continue.")
            new_pass = hash_pass(new_pass)
            new_acc.append(new_pass)
            return[]
            break
      
        else:
            return None


def delete_acc():
    print("Test delete_acc")