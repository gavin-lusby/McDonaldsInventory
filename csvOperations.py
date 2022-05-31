import csv
from os import path as ospath
from sys import path as syspath

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
            products[item[0]] = item[1]

    return products


# returns num of groups of product, and what a group is called(two decimal places)
def useToGrp(product_name, uses):
    return [(int(100 * uses / UBP[product_name][1])) / 100, UBP[product_name][3]]


# returns num of containers of product, and what a container is called(two decimal places)
def useToCon(product_name, uses):
    return [(int(100 * (uses / UBP[product_name][1]) / UBP[product_name][0])) / 100, UBP[product_name][2]]


# returns num of uses of product
def grpToUse(product_name, groups):
    return groups * UBP[product_name][1]


# returns num of uses of product
def grpToCon(product_name, groups):
    return [(int(100 * (groups / UBP[product_name][0])))/100, UBP[product_name][2]]


# returns num of uses of product
def conToUse(product_name, cons):
    return cons * UBP[product_name][0] * UBP[product_name][1]


# returns num of groups of product, and what a group is called
# Example input: ("nuggets", 10), example output : [100, "bag(s)"]
def conToGrp(product_name, cons):
    return [cons * UBP[product_name][0], UBP[product_name][3]]
