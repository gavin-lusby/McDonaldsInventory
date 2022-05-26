import csv
from os import path as ospath
from sys import path as syspath

UBP = {}
with open(ospath.join(syspath[0], "subdivs.csv"), 'r') as f:
    reader = csv.reader(f)
    for product in list(reader):
        UBP[product[0]] = [int(product[1]), int(product[2])] + product[3:]


def getInv():
    products = {}
    with open(ospath.join(syspath[0], "inventory.csv"), 'r') as f:
        reader = csv.reader(f)
        for item in list(reader):
            products[item[0]] = item[1]

    return products


