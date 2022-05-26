# Manager or employees check stock (how much has been used, how much needs to be ordered)
from resetScreen import reset_screen


# Edited by Isaac (2022-5-23)

# Function for finding index of 2d array, checks for item in first item of list
def DD_find(DD, item):
    for l in range(0, len(DD)):
        if DD[l][0] == item:
            return l
    return -1  # used in checking


def check_stock(stock, subdivs):
    reset_screen()

    item = input("What item would you like to check: ")
    while DD_find(item) <= 0 and not item.isalnum():  # makes sure item is in stock
        item = input("That item is not in inventory.\n\nWhat item would you like to check: ")

    # if user wants to see all
    if item == "all":
        for a in subdivs:
            subindex = DD_find(stock, a[0])
            sub1 = stock[subindex][1] // a[2]  # Number of boxes
            sub2 = stock[subindex][1] % a[2]  # Number of remaining uses
            print(f"There are {sub1} {a[3]} and {sub2} {a[4]} of {a[0]} ({stock[subindex][1]} uses).")

    # specific item
    else:
        for b in subdivs:
            if b[0] == item:
                subindex = DD_find(stock, b[0])
                sub1 = stock[subindex][1] // b[2]  # Number of boxes
                sub2 = stock[subindex][1] % b[2]  # Number of remaining uses
                print(f"There are {sub1} {b[3]} and {sub2} {b[4]} of {b[0]} ({stock[subindex][1]} uses).")

    pass
# Should return nothing(prints current stock, may return current stock in later versions)
