# should turn a 2 item list containing the containers and groups of an item, with input of item and count
# "returns num of containers and groups of product"
# input (str, num) return [num, num]

# python -m unittest discover test/

# Edited by Isaac 2022-06-08


import unittest
from csvo import grp_to_con_grp()

import random

class TestGTCG(unittest.TestCase):
    def test_gtcg_predef(self):
        # test general
        expected = [9,8]
        actual = csvo.grp_to_con_grp("fries", 458)
        self.assertEqual(actual, expected)

        # test negative
        expected = [0,-93]
        actual = csvo.grp_to_con_grp("lettuce", -93)
        self.assertEqual(actual, expected)

        # test if no remainder
        expected = [2,0]
        actual = csvo.grp_to_con_grp("nuggets", 48)
        self.assertEqual(actual, expected)

        self.assertEqual(csvo.grp_to_con_grp("fries", -56), [-1, -6])

    def test_gtcg_rand(self):
        r = random.randint(0,600)
        self.assertEqual(csvo.grp_to_con_grp("fries", r), [r // 50, r % 50])