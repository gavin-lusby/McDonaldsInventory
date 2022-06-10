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


def acc_menu(manager_status, user_name, valid_accs):

    # Initial menu print
    reset_screen(False)
    print_menu(manager_status)
    
    # Allows user to enter menu items allowed based on their status as a manager or employee
    while True:
      act = input("SELECT AN ACTION: ").strip()
      act_valid = True
  
      # Ensures only managers can access manager-only functions
      if act == "1":
          change_pass(valid_accs, user_name)
      elif act == "2" and manager_status:
          create_acc(valid_accs)
      elif act == "3" and manager_status:
          delete_acc(valid_accs)
      elif act == "exit":
          reset_screen(True)
          break
      else:
          act_valid = False
        
      reset_screen(False)
      print_menu(manager_status)
      
      if not act_valid:
          print("Invalid action. Please try again.")


def change_pass(valid_accs, user_name):
    # Allows users to change their account password if they know their current password
        # Saves all hashed current passwords in list passes
    passes = []
    for user in valid_accs:
        passes.append(valid_accs[user][1])

  
    current_pass = str(input("Enter current password: "))
    if current_pass.lower().strip() == "exit":
        input("Password change cancelled. Press enter to continue.")
        reset_screen(True)
        return

    # Can only change correct current passwords
    while hash_pass(current_pass) not in passes:
        print("Incorrect current password.")
        current_pass = str(input("Correctly enter current password: "))

        if current_pass.lower().strip() == "exit":
            input("Password change cancelled. Press enter to continue.")
            reset_screen(True)
            return
    
    changed_pass = str(input("Enter new password (case-sensitive): "))
    
    # Changes user's password if changes have been saved
    if check_if_save():
        input("Password change has been saved. Press enter to continue.")
        valid_accs[user_name][1] = hash_pass(changed_pass)
        acc_file_update(valid_accs)
      
        reset_screen(True)
        return
    else:
        input("Password change cancelled. Press enter to continue.")
        reset_screen(True)
        return


def create_acc(valid_accs):
    new_acc = []
  
    # Creates new user's username
    while True:
        new_name = str(input("Enter full name: ")).upper().strip()
        if new_name == "EXIT":
            input("Create new account cancelled. Press enter to continue.")
            reset_screen(True)
            break
  
        # Prevents multiple accounts under the same name
        while new_name in valid_accs:
            new_name = str(input("This user already exists. Enter new user's full name or type \"exit\": ")).upper().strip()

            if new_name == "EXIT":
                input("Create new account cancelled. Press enter to continue.")
                reset_screen(True)
                break

          
        # User can choose to re-enter username as many times as they would like
        if check_if_save():
            input("Username changes saved. Press enter to continue.")
            new_acc.append(new_name)
  
            # Asks user to choose manager status
            create_status = create_acc_status(valid_accs, new_acc)
            if create_status != None:
                create_pass = create_acc_pass(valid_accs, new_acc)
              
                if create_pass != None:
                    # Writes new user (name, status, and password to users.csv)
                    valid_accs[new_name] = [create_status, create_pass]
                    acc_file_update(valid_accs)
                  
                    print(f"{create_status} {new_name} saved.")
                    reset_screen(True)
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
        elif new_status == "exit":
            return None
        else:
          print("Invalid response.")


        # Checks if user would like to save changes
        if check_if_save():
            input("Status changes saved. Press enter to continue.")
            new_acc.append(new_status)
            return new_status
          
        else:
            return None


def create_acc_pass(valid_accs, new_acc):
    # Creates new user's password
    while True:
        new_pass = str(input("Enter password (case-sensitive): "))

        if new_pass.lower().strip() == "exit":
            return None
        
        if check_if_save():
            input("Password changes saved. Press enter to continue.")
            new_pass = hash_pass(new_pass)
            new_acc.append(new_pass)
            return new_pass
      
        else:
            return None


def delete_acc(valid_accs):
    # Removes a key:value pair from the dictionary valid_accs
    remove_acc = str(input("Enter the full name of the user whose account you would like to remove: ")).upper().strip()

    if remove_acc == "EXIT":
        input("Delete account cancelled. Press enter to continue.")
        reset_screen(True)
        return

    # Can only remove existing users
    while remove_acc not in valid_accs:
        remove_acc = str(input("This user does not exist. Please enter the correct full name of the existing user whose account you would like to remove or type \"exit\": ")).upper().strip()
  
        if remove_acc == "EXIT":
            input("Delete account cancelled. Press enter to continue.")
            reset_screen(True)
            return

    # Deletes the user if changes have been saved
    if check_if_save():
        input(f"{remove_acc} has been deleted. Press enter to continue.")
        del valid_accs[remove_acc]
        acc_file_update(valid_accs)
      
        reset_screen(True)
        return
    
    else:
        input("Delete account cancelled. Press enter to continue.")
        reset_screen(True)
        return