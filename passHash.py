import os
import sys
import csv
import hashlib

# Note: Need to pass as valid_accs.sort() to retain alphabetical organization in the CSV
def accFileUpdate(valid_accs):
  # Updates users.csv with the hashed passwords
    with open(os.path.join(sys.path[0], "users.csv"), 'w', newline="") as r:
        writer = csv.writer(r)
        writer.writerows(valid_accs)


def hash_file(valid_accs):
    for user in range(len(valid_accs)-1):
      newHash = hashlib.sha512( (valid_accs[user].value[1]).encode() ).hexdigest()
      valid_accs[user].value[1][user] = newHash

    accFileUpdate(valid_accs.sort())