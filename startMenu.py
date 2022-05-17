# Starting menu
def start_menu():
  # Imports list of valid accounts
  from main import validAccs
  acc = ""

  # Checks to see if 
  for acc in validAccs == False:
    acc = input("Please enter your access code: ")
  
  print("SELECT AN ACTION:")
  for i in range(1,4):
    if i == 1:
      act = "update the inventory (managers only)"
    elif i == 2:
      act = "recalibrate ()"
    elif i == 3:
      act = ""
    
    print(f"\nType '{i}' to {act}")
# Should return nothing