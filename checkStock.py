# Manager or employees check stock (how much has been used, how much needs to be ordered)
from resetScreen import reset_screen
import csvOperations

# Edited by Isaac (2022-5-23)
# Edited by Isaac (2022-5-31) Officially works with dictionary and clean up

def check(Dict): # Checks if input is valid
    check = input("What item would you like to check: ").lower()
    while True: #loops through until valid input
        if check in Dict or check == 'all' or check == 'exit':
            break
        else:
            item = input("\nItem not in inventory, please try again: ").lower()
    return item

def printout(stock, subdivs, item):
    sub1 = stock[item][1] // subdivs[item][2] # Number of boxes
    sub2 = stock[item][1] % subdivs[item][2] # Number of remaining uses
    print(f"There are {sub1} {subdivs[item][3]} and {sub2} {subdivs[item][4]} of {subdivs[item][0]} ({stock[item][1]} uses).")
    
def check_stock():
    stock = csvOperations.getInv()  
    subdivs = csvOperations.UBP
    reset_screen(True)

    search = check(subdivs)

    if search == "all": # if user wants to see all
        for a in subdivs:
            printout(stock, subdivs, a)

    elif search == 'exit':
        reset_screen(True)
        pass

    else: # specific item
        printout(stock, subdivs, search)

    pass
# Should return nothing (prints current stock, may return current stock in later versions)