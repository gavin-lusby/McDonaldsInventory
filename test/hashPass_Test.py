# should turn a 2 item list containing the containers and groups of an item, with input of item and count
# "returns num of containers and groups of product"
# input (str, num) return [num, num]

# python -m unittest discover test/

# Edited by Isaac 2022-06-08


import hashlib
import unittest

from passHash import hash_pass, generate_salt


class TestHashPass(unittest.TestCase):
    def test_hash_pass_predef(self):
        # test general
        expected = 'dab4918b97a45655d7a75f1e944d5f88c50ae907b63841b161d3aa9a3d5cb72267ecb3252f10bd032b6962ecf67a025aabe9645bb5706d45fb5cfed9d85f16bc'
        actual = hash_pass('password123', 'gzm89Uy6GFV3SqKr')
        self.assertEqual(actual, expected)

        # test negative
        expected = 'ff32a7d0af83510a1a01ed726175535b6e5fece7172b8128a0cbc3a9a92fd8fc7303907a311bb0f003533159d540c83ecfabdd31f86b7850e7530a25de120328'
        expected = ['', '3AdHR6bTLio/m5fc']
        actual = hash_pass('', '3AdHR6bTLio/m5fc')
        self.assertEqual(actual, expected)

        # test if no remainder
        expected = 'c83aadb0e1d5b2376a47e0e950bf364f856cf0d6c5d538e1111ba932b7704e2e9739cf6d0819bd502e11d7b92d69dffc8bc9c206427483d75d8e8911e5759886'
        actual = hash_pass("gavin", 'lusby')
        self.assertEqual(actual, expected)

    def test_gtcg_rand(self):
        salt = generate_salt()
        password = generate_salt()  # Generate salt just returns 16 characters ["a-z"+"A-Z"+"0-9"+".""+"/] so it can also be used to make a password
        salted_password = salt + password
        self.assertEqual(hash_pass(password, salt), hashlib.sha512(salted_password.encode()).hexdigest())
