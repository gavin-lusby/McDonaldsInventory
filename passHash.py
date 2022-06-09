import os
import sys
import csv
import hashlib


def accFileUpdate(valid_accs):
    # Updates users.csv with the hashed passwords so they are not stored in plain text
    
    with open(os.path.join(sys.path[0], "users.csv"), 'w', newline="") as r:
        writer = csv.writer(r)
        writer.writerows(valid_accs)


def hash_file(valid_accs):
  # Hashes each user's password
    for user in valid_accs.keys():
        newHash = hashlib.sha512((valid_accs[user][1]).encode()).hexdigest()
        valid_accs[user][1] = newHash

    accFileUpdate(valid_accs)