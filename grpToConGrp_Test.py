# should turn a 2 item list containing the containers and groups of an item, with input of item and count
# "returns num of containers and groups of product"
# input (str, num) return [num, num]

# Edited by Isaac 2022-06-08


import unittest
import csvo

import random


class TestGTCG(unittest.TestCase):
    def test_gtcg_predef(self):
        expected = [9,8]
        actual = csvo.grpToConGrp("fries", 458)
        self.assertEqual(actual, expected)

        expected = [0,93]
        actual = csvo.grpToConGrp("lettuce", 93)
        self.assertEqual(actual, expected)

        expected = [2,0]
        actual = csvo.grpToConGrp("nuggets", 48)
        self.assertEqual(actual, expected)

        #self.assertEqual(csvo.grpToConGrp("fries",-56),[-1,-6])

    def test_gtcg_rand(self):
        r = random.randint(0,600)
        self.assertEqual(csvo.grpToConGrp("fries",r),[r//50, r % 50])