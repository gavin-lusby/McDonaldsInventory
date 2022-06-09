# csvo is short for CSV Operations
import csv
from os import path as ospath
from sys import path as syspath

# UBP = units by product
"""
Creates a dict for the sake of converting and storing unit types. First item in
each line(names of items) of csv becomes the key, and the rest of the items become
a list that is stored as the value associated with that key. The number values get converted from string to int
"""


def fetchUBP():
    unit_by_product = {}
    with open(ospath.join(syspath[0], "subdivs.csv"), 'r') as f:
        reader = csv.reader(f)
        for product in list(reader):
            unit_by_product[product[0]] = [int(product[1]), int(product[2])] + product[3:]
    return unit_by_product


# Overwrites subdivs.csv and updated UBP
def overwriteSubdivs(new_UBP):
    global UBP
    # Checks if changes would be redundant before making them
    if new_UBP != fetchUBP():
        with open(ospath.join(syspath[0], "subdivs.csv"), 'w', newline="") as f:
            writer = csv.writer(f)
            temp_subdivs_as_list = []
            name_list = list(new_UBP)
            name_list.sort()
            # Sorting names so that the printed order in the csv is alphabetical

            # Converts dictionary called inv into list of all of its keys
            # since writerows only takes 2d lists as arguments(not dictionaries)
            print(new_UBP)
            for item in name_list:
                temp_subdivs_as_list.append([item, new_UBP[item][0], new_UBP[item][1], new_UBP[item][2],
                                             new_UBP[item][3]])
            writer.writerows(temp_subdivs_as_list)


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
            name_list = list(updated_inv)
            name_list.sort()
            # Sorting names so that the printed order in the csv is alphabetical

            # Converts dictionary called inv into list of all of its keys
            # since writerows only takes 2d lists as arguments(not dictionaries)
            for item in name_list:
                temp_inv_as_list.append([item, updated_inv[item]])
            writer.writerows(temp_inv_as_list)


"""
Anything involving 'uses' is no longer necessary as we don't have time to make the inventory auto-update
based on till orders (making a till system at this point is out of the cards). The only use we have for uses now
is to include how many total uses you have of each product when checking stock. We still record amount of uses though
so that the program is future proof for if we wanted to/had time to add a till system further on(in a realistic scenario
it would be wise to ensure that our product will be compatible with its own updates as there would be no reason to 
presume we won't eventually make said updates as a real company)

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
    ubp = fetchUBP()
    return [groups // ubp[product_name][0], groups % ubp[product_name][0]]


# returns num of groups of product
# Example input: ("nuggets", 10), example output : 100
def conToGrp(product_name, cons):
    return cons * fetchUBP()[product_name][0]


# returns num of uses of product
def grpToUse(product_name, groups):
    return groups * fetchUBP()[product_name][1]


# Check if the user has chosen to save (returns True) or not (returns False)
# This is used to determine whether changes to csv's will be made
def checkIfSave():
    while True:
        save_bool = input("Do you want to save changes? (y/n): ").lower().strip()
        if save_bool == "n":
            return False
        elif save_bool == "y":
            return True
        else:
            print("Invalid response.")
