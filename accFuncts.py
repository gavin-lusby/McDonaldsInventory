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


def acc_menu(manager_status):

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
          create_acc()
      elif act == "3" and manager_status:
          delete_acc()
      elif act == "exit":
          exit_menu()
      else:
          act_valid = False
        
      reset_screen(False)
      print_menu(manager_status)
      
      if not act_valid:
          print("Invalid action. Please try again.")


def write_users_csv(change):
    # Writes to users.csv
  f.write(change)


def change_pass():
   new_pass = input(str(""))


def create_acc():
    new_acc = []
    new_status = ""

    # Creates new user's username
    while True:
      new_status = str(input("Is this user a manager? (y/n): ")).lower().strip()

      if new_status == "y":
        new_status = True
        break
      elif new_status == "n":
        new_status = False
        break
      else:
        print("Invalid response.")
  
    # Allows user to enter manager/employee status
    while True:
      new_status = str(input("Is this user a manager? (y/n): ")).lower().strip()

      if new_status == "y":
        new_status = True
        break
      elif new_status == "n":
        new_status = False
        break
      else:
        print("Invalid response.")

      # Creates new user's password
      while True:
        new_status = str(input("Is this user a manager? (y/n): ")).lower().strip()
  
        if new_status == "y":
          new_status = True
          break
        elif new_status == "n":
          new_status = False
          break
        else:
          print("Invalid response.")
          
    new_name = str(input("FULL NAME: "))
    
    
    # Writes new user (name, status, and password to users.csv)
    write_users_csv([new_name,new_status,new_pass])
    print(f"User {user_name} saved.")



def delete_acc():
    print("Test delete_acc")