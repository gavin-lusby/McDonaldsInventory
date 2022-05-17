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
  # Imports list of valid accounts
  validAccs = ["manager123", "employee1"]
  acc = ""

  # Checks to see if access code is valid
  while acc not in validAccs:
    acc = input("Please enter your access code, or type exit to end program: ")

    # Exits program if exit option chosen
    if acc == "exit":
      exit_menu()

    # Calls on appropriate function for user's desired action
    act = input("SELECT AN ACTION:")
    if act == 1:
      new_shipment_up()
    elif act == 2:
      recalib_inventory()
    elif act == 3:
      #check_stock()
      pass
# Should return nothing


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
  
  # Importing from inventory.csv to create list of inventory units_by_product
  units_by_product = {}
  with open(os.path.join(sys.path[0],"subdivs.csv"), 'r') as f:
      reader = csv.reader(f)
      for product in list(reader):
        units_by_product[product[0]] = [int(product[1]),int(product[2])]+product[3:]


  with open(os.path.join(sys.path[0],"menus.txt"), 'r') as f:
    raw_menus = []
    for menu in f.read().splitlines():
      menus.append(menu.replace('\\n','\n'))
  menus = {}
  menus["selfunc"] = raw_menus[0]
  # Run program
  start_menu()