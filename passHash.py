import os
import sys
import csv
import hashlib

# Note: Need to pass as valid_accs.sort() to retain alphabetical organization in the CSV
def accFileUpdate(valid_accs):
  # Updates users.csv with the hashed passwords so they are not stored in plain text
    
  # Sorts valid_accs's keys alphabetically so CSV is alphabetically organized
    acc_temp = []
    for pair in valid_accs:
      acc_temp.append(list[pair])

    acc_temp.sort()
    print(acc_temp)
  
    #acc_names = (valid_accs.keys()).sort()
    #acc_passes = (valid_accs.)
    
  
    with open(os.path.join(sys.path[0], "users.csv"), 'w', newline="") as r:
        writer = csv.writer(r)
        writer.writerows(valid_accs)


def hash_file(valid_accs):
  # Hashes each user's password
    for user in valid_accs.keys():
      newHash = hashlib.sha512((valid_accs[user][1]).encode()).hexdigest()
      valid_accs[user][1] = newHash

    accFileUpdate(valid_accs)