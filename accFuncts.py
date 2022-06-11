# accFuncts is short for Account Functions
# There are two types of user accounts ("accs"): manager accounts and employee accounts. Both have different levels of access to certain functionalities within the program


# Imports functions used
from csvo import check_if_save
from exitMenu import exit_menu
from os import path as ospath
from passHash import acc_file_update, generate_salt, hash_pass
from resetScreen import reset_screen
from sys import path as syspath


# (Lines 14-21) Saves account settings menus from accMenus.txt to a list
acc_menus_lst = []

with open(ospath.join(syspath[0], "accMenus.txt"), 'r') as f:
    reader = f.read().splitlines()
  
for menu_line in list(reader):
    acc_menus_lst.append(menu_line.replace('\\n', '\n'))


def manager_check(user_name, valid_accs):
    # Checks if user is a manager or an employee
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
    # This function prints and allows users to choose from the account settings menu according to their status as manager or employee

    # Initial menu print
    reset_screen(False)
    print_menu(manager_status)
    
    # Allows user to enter menu items allowed based on their status as a manager or employee
    while True:
      act = input("SELECT AN ACTION: ").strip()
      act_valid = True
  
      # Ensures only managers can access manager-only functions
      if act == "1":
          change_pass(manager_status, user_name, valid_accs)
      elif act == "2" and manager_status:
          create_acc(valid_accs)
      elif act == "3" and manager_status:
          delete_acc(user_name, valid_accs)
      elif act == "exit":
          reset_screen(True)
          break
      else:
          act_valid = False
        
      reset_screen(False)
      print_menu(manager_status)

      # Prints error message if user inputs something other than 1-3 or exit
      if not act_valid:
          print("\nInvalid action. Please try again.")


def change_pass(manager_status, user_name, valid_accs):
    # This function allows account passwords to be changed
    # Sidenote: We, the developers, unanimously agree that it's annoying when you forget your current password, then attempt to change your password and get hit with an error message telling you that your new password cannot be your current password (we're all a little forgetful sometimes 😔). Thus, we did not include this annoying feature. We hope you can understand our decision on this very important matter.

  
    # Allows users to change their account (or another account's, in the case of managers making the password changes) password if they know their account's current password
    current_pass = str(input("Enter your account's current password: "))
    if current_pass.lower().strip() == "exit":
        input("\nPassword change cancelled. Press enter to continue.")
        reset_screen(True)
        return
        
    user_salt = valid_accs[user_name][2]

  
    # Users can only change an account's password if they know their own account's password (extra security measure in case an employee has accidentally left their account logged in after initially entering their password at the start of the program)
    while hash_pass(current_pass, user_salt) != valid_accs[user_name][1]:
        print("\nIncorrect current password.")
        current_pass = str(input("Correctly enter current password: "))

        if current_pass.lower().strip() == "exit":
            input("\nPassword change cancelled. Press enter to continue.")
            reset_screen(True)
            return

  
    # Managers can change their account password or the passwords of anyone else's account
    if manager_status:
        user_name = str(input("Enter the full name of the user who's password you would like to change: ")).upper()

    if user_name == "EXIT":
        input("\nChange password cancelled. Press enter to continue.")
        reset_screen(True)
        return

    # Can only remove existing users
    while user_name not in valid_accs:
        user_name = str(input("\nThis user does not exist. Please enter the correct full name of the existing user whose account you would like to remove or type \"exit\": ")).upper()
  
        if user_name == "EXIT":
            input("\nChange password cancelled. Press enter to continue.")
            reset_screen(True)
            return
    
    changed_pass = str(input("Enter new password for the password change (case-sensitive): "))
  
    while changed_pass.strip() == "":
        print("\nPassword cannot just be whitespace; must contain other characters.")
        changed_pass = str(input("Enter new password for the password change (case-sensitive): "))
    
    # Changes user's password if changes have been saved
    if check_if_save():
        input("\nPassword change has been saved. Press enter to continue.")
        new_salt = generate_salt()
        valid_accs[user_name][1] = hash_pass(changed_pass, new_salt)
        valid_accs[user_name][2] = new_salt
        acc_file_update(valid_accs)
      
        reset_screen(True)
        return
    else:
        input("\nPassword change cancelled. Press enter to continue.")
        reset_screen(True)
        return


def create_acc(valid_accs):
    new_acc = []
  
    # Creates new user's username
    #while True:
        
    new_name = input('Enter full name of new account holder. Should contain letters and a space between first, middle and/or last names.').upper()

    # Prevents multiple accounts under the same name, and name being white space
    while new_name.strip() == "" or (new_name in valid_accs):
        if new_name.strip() == "":
            new_name = str(input("\nName cannot be just whitespace. Enter full name: ")).upper()
        elif new_name in valid_accs:
            new_name = str(input("\nThis user already exists. Enter new user's full name or type \"exit\": ")).upper()
      
    if new_name == "EXIT":
        input("\nCreate new account cancelled. Press enter to continue.")
        reset_screen(True)
        pass
          
    # User can choose to re-enter username as many times as they would like
    if check_if_save():
        input("\nUsername changes saved. Press enter to continue.")
        new_acc.append(new_name)
  
        # Asks user to choose manager status
        create_status = create_acc_status(valid_accs, new_acc)
        if create_status != None:
            create_pass = create_acc_pass(valid_accs, new_acc)
              
            if create_pass != None:
                # Writes new user (name, status, and password to users.csv)
                valid_accs[new_name] = [create_status, create_pass, generate_salt()]
                acc_file_update(valid_accs)
                  
                print(f"{create_status} {new_name} saved.")
                reset_screen(True)
            else:
                input("\nCreate new account cancelled. Press enter to continue.")
                reset_screen(True)
                pass
        else:
            input("\nCreate new account cancelled. Press enter to continue.")
            reset_screen(True)
            pass
                  
    else:
        input("\nCreate new account cancelled. Press enter to continue.")
        reset_screen(True)
        pass
      
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
          print("\nInvalid response.")


        # Checks if user would like to save changes
        if check_if_save():
            input("\nStatus changes saved. Press enter to continue.")
            new_acc.append(new_status)
            return new_status
          
        else:
            return None


def create_acc_pass(valid_accs, new_acc):
    # Note: Appended to new_acc so changes can be made to users.csv, in addition to returning values from new_acc or None (this allows us to check if the user has saved changes or not at every step)
  
    # Creates new user's password
    while True:
        new_pass = str(input("Enter password (case-sensitive): "))
      
        while new_pass.strip() == "":
            print("\nPassword cannot just be whitespace; must contain other characters.")
            new_pass = str(input("Enter password (case-sensitive): "))

        if new_pass.lower().strip() == "exit":
            return None
        
        if check_if_save():
            input("\nPassword changes saved. Press enter to continue.")
            new_salt = generate_salt()
            new_pass = hash_pass(new_pass, new_salt)
            
            new_acc.append(new_pass)
            return new_pass
      
        else:
            return None


def delete_acc(user_name, valid_accs):
    # Removes a key:value pair from the dictionary valid_accs
    remove_acc = str(input("Enter the full name of the user whose account you would like to remove: ")).upper()

    if remove_acc == "EXIT":
        input("\nDelete account cancelled. Press enter to continue.")
        reset_screen(True)
        return

    # Can only remove existing users and cannot remove self
    while remove_acc not in valid_accs or remove_acc == user_name:
        if remove_acc == user_name:
            print("\nCannot delete your own account. Please have another manager delete your account instead.")
            remove_acc = str(input("\nPlease enter the correct full name of another existing user whose account you would like to remove or type \"exit\": ")).upper()
        elif remove_acc == "EXIT":
            input("\nDelete account cancelled. Press enter to continue.")
            reset_screen(True)
            return
        elif remove_acc not in valid_accs:
            remove_acc = str(input("\nThis user does not exist. Please enter the correct full name of the existing user whose account you would like to remove or type \"exit\": ")).upper()

          
    # Deletes the user if changes have been saved
    if check_if_save():
        input(f"{remove_acc} has been deleted. Press enter to continue.")
        del valid_accs[remove_acc]
        acc_file_update(valid_accs)
      
        reset_screen(True)
        return
    
    else:
        input("\nDelete account cancelled. Press enter to continue.")
        reset_screen(True)
        return