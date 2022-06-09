import csv
from os import path as ospath
from sys import path as syspath


# This function creates user accounts ("accs") of two types: manager accounts and employee accounts (which both have different levels of access to certain functionalities within the program)


# Saves account settings menus from accMenus.txt to a list
acc_menus_lst = []

with open(ospath.join(syspath[0], "accMenus.txt"), 'r') as f:
    reader = f.read

for menuLine in list(reader):
    acc_menus_lst.append(menuLine)


def manager_check(userName,valid_accs):
    # Checks if user is a manager or not (user is an employee) and provides access to the accordingly appropriate functions
    if valid_accs[userName][1] == "manager":
      manager_access = True
      print(acc_menus_lst[0]) # Prints manager-access actions
      
    else:
      manager_access = False
      print(acc_menus_lst[1]) # Prints employee-access actions
  
  
def manager_menu():
    pass


def employee_menu():
    pass