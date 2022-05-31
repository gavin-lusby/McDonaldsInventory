# Manager or employees check stock (how much has been used, how much needs to be ordered)
from resetScreen import reset_screen


# Edited by Isaac (2022-5-23)
# Edited by Isaac (2022-5-31)

# used in checking
def check(Dict):
    item = input("What item would you like to check: ").lower()
    while True: #loops through until valid input
        if item in Dict or item == 'all':
            break
        else:
            item = input("\nItem not in inventory, please try again: ").lower()
    return item

def find (DD, item):
    for i in DD:
      if item == i[0]:
        return DD.index(i)
    
def check_stock(stock, subdivs):
    reset_screen()

    item = check(subdivs)

    # if user wants to see all
    if item == "all":
        for a in subdivs:
            index = find(stock, item)
            sub1 = stock[index][1] // subdivs[a][2]
            sub2 = stock[index][1] % subdivs[a][2]
            print(f"There are {sub1} {a[3]} and {sub2} {a[4]} of {a[0]} ({stock[index][1]} uses).")

    # specific item
    else:
        index = find(stock, item)
        sub1 = stock[index][1] // subdivs[item][2]  # Number of boxes
        sub2 = stock[index][1] // subdivs[item][2]  # Number of remaining uses
        print(f"There are {sub1} {subdivs[item][3]} and {sub2} {subdivs[item][4]} of {subdivs[item][0]} ({stock[index][1]} uses).")

    pass
# Should return nothing(prints current stock, may return current stock in later versions)
