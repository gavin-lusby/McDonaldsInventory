# Manager or employees check stock (how much has been used, how much needs to be ordered)
from resetScreen import reset_screen


# Edited by Isaac (2022-5-23)
# Edited by Isaac (2022-5-31)

# used in checking
def check(DD, item):
  while True
    if item.isalpha():
      if item in DD:
        break
      else:
        item = 
    
  
  return item

def check_stock(stock, subdivs):
    reset_screen()

    item = check(stock, input("What item would you like to check: ").lower())

    # if user wants to see all
    if item == "all":
        for a in subdivs:
            subindex = 1
            sub1 = stock[subindex][1] // a[2]  # Number of boxes
            sub2 = stock[subindex][1] % a[2]  # Number of remaining uses
            print(f"There are {sub1} {a[3]} and {sub2} {a[4]} of {a[0]} ({stock[subindex][1]} uses).")

    # specific item
    else:
        for b in subdivs:
            if b == item:
                subindex = 1
                sub1 = stock[subindex][1] // b[2]  # Number of boxes
                sub2 = stock[subindex][1] % b[2]  # Number of remaining uses
                print(f"There are {sub1} {b[3]} and {sub2} {b[4]} of {b[0]} ({stock[subindex][1]} uses).")

    pass
# Should return nothing(prints current stock, may return current stock in later versions)
