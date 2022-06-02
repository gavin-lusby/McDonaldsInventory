# Short for CSV Operations
import csv
from os import path as ospath
from sys import path as syspath

# UBP = units by product
"""
Creates a dict for the sake of converting and storing unit types. First item in
each line(names of items) of csv becomes the key, and the rest of the items become
a list that is stored as the value associated with that key. The number values get converted from string to int
"""

UBP = {}
with open(ospath.join(syspath[0], "subdivs.csv"), 'r') as f:
    reader = csv.reader(f)
    for product in list(reader):
        UBP[product[0]] = [int(product[1]), int(product[2])] + product[3:]

# Fetches current inventory data and stores as dict in form of <product name> : <num of uses>
def getInv():
    products = {}
    with open(ospath.join(syspath[0], "inventory.csv"), 'r') as f:
        reader = csv.reader(f)
        for item in list(reader):
            products[item[0]] = int(item[1])

    return products


# Updates inventory stored in CSV to match the inventory stored in memory (since changes will be made to the
# memory-stored one by the users) Format of inventory.csv: "buns,300"
def setInv(updated_inv):
    # Checks if changes would be redundant before making them
    if updated_inv != getInv():
        with open(ospath.join(syspath[0], "inventory.csv"), 'w', newline="") as f:
            writer = csv.writer(f)
            temp_inv_as_list = []
            # Converts dictionary called inv into list of all of its keys
            # since writerows only takes 2d lists as arguments(not dictionaries)
            for item in list(updated_inv):
                temp_inv_as_list.append([item, updated_inv[item]])
            writer.writerows(temp_inv_as_list)


"""
Anything involving 'uses' is no longer necesarry as we don't have time to make the inventory auto-update
based on till orders (making a till system at this point is out of the cards)

# returns num of groups of product, and what a group is called(two decimal places)
def useToGrp(product_name, uses):
    return [(int(100 * uses / UBP[product_name][1])) / 100, UBP[product_name][3]]


# returns num of containers of product, and what a container is called(two decimal places)
def useToCon(product_name, uses):
    return [(int(100 * (uses / UBP[product_name][1]) / UBP[product_name][0])) / 100, UBP[product_name][2]]



# returns num of uses of product
def conToUse(product_name, cons):
    return cons * UBP[product_name][0] * UBP[product_name][1]
"""


# returns num of containers and groups of product
# Example input: ("nuggets", 105), example output : [10,5]
def grpToConGrp(product_name, groups):
    return [groups // UBP[product_name][0], groups % UBP[product_name][0]]


# returns num of groups of product
# Example input: ("nuggets", 10), example output : 100
def conToGrp(product_name, cons):
    return cons * UBP[product_name][0]


# returns num of uses of product
def grpToUse(product_name, groups):
    return groups * UBP[product_name][1]
