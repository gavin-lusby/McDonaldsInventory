import os
import sys
import csv
import hashlib
import random

def hash_file(valid_accs):
  # Hashes each user's password
  # Only run once to properly hash passwords already in users.csv from program development (see hidden.txt), not including newly-added accounts by user
    for user in valid_accs.keys():
        newHash = hashlib.sha512((valid_accs[user][1]).encode()).hexdigest()
        valid_accs[user][1] = newHash

    acc_file_update(valid_accs)


def hash_pass(user_pass,user_salt):
    # Hashes a single password (used to create new passwords or change existing passwords)
    unencrypted=user_salt+user_pass
    newHash = hashlib.sha512(unencrypted.encode()).hexdigest()
    return newHash

  
def acc_file_update(valid_accs):
    # Re-writes all of users.csv with most recent list stored in valid_accs_csv
    valid_accs_csv = []
  
    for user in valid_accs:
        valid_accs_csv.append([user, valid_accs[user][0], valid_accs[user][1]])

    valid_accs_csv.sort()
      
    # Updates users.csv with the hashed passwords so they are not stored in plain text
    with open(os.path.join(sys.path[0], "users.csv"), 'w', newline="") as r:
        writer = csv.writer(r)
        writer.writerows(valid_accs_csv)


def generate_salt():
   return ''.join(random.sample('./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',16))
    
    