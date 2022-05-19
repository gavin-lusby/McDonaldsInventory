# Employee update for taking items from shelf
def recalib_inventory():
  # Imports variables from main.py
  global acc, units_by_product

  print(f"Welcome, {acc}")

  request = ""
  updates = []

  # Takes requests from employee user
  while request.lower() != "exit":
    request = input("Enter item taken, or type exit to finish updating: ")
    updates.append(request)

  units_by_product

# Should return nothing (takes inputs only)