"""
Written by: Gavin, Isaac, Katie, Nikolas
Date: May 12-June 10, 2022
Purpose: Create a comprehensive inventory software for McDonald's employees and managers to use

GENERAL PROGRAMMING NOTES
- subdivs.csv does not get modified by the program. It should only be edited manually when adding new products.
"""
#cool comment


import csv
import sys
import os

# Imports functions used
from startMenu import start_menu
from checkStock import check_stock
from recalibInventory import recalib_inventory
from exitMenu import exit_menu

# Importing from inventory.csv to create list of inventory units_by_product
units_by_product = {}
with open(os.path.join(sys.path[0],"subdivs.csv"), 'r') as f:
    reader = csv.reader(f)
    for product in list(reader):
      units_by_product[product[0]] = [int(product[1]),int(product[2])]+product[3:]
"""
Creates a dict for the sake of converting and storing unit types. First item in
each line(names of items) of csv becomes the key, and the rest of the items become
a list that is stored as the value associated with that key. The number values get converted from string to int
"""