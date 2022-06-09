# should turn a 2 item list containing the containers and groups of an item, with input of item and count
# "returns num of containers and groups of product"
# input (str, num) return [num, num]

# Edited by Isaac 2022-06-08


import unittest
import csvo

import random


# ---------- reading csv for testing ---------- #
import os
import sys
import csv
UBP = {}
with open(ospath.join(syspath[0], "subdivs.csv"), 'r') as f:
    reader = csv.reader(f)
    for product in list(reader):
        UBP[product[0]] = [int(product[1]), int(product[2])] + product[3:]
 # hear we get subdivs group to compare to function

# fries,8,50,box(es),bag(s)
class TestGTG(unittest.testCase):
    def test_conv_predef(self):
        expected = []
        actual = csvo.grpToConGrp
        self.assertEqual(actual, expected)

        expected =
        actual = 
        self.assertEqual(actual, expected)

        expected =
        actual = 
        self.assertEqual(actual, expected)