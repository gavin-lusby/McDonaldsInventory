# Manager manual update inventory function (includes new shipments and recalibrating total product stock)

# Edited by Isaac 2022-06-07 Started work

from resetScreen import reset_screen
import csvo

def print_inv(inv):
    reset_screen(True)
    for i in inv:
        print(i, inv[i])

def validItem():
    i = input(str("Which item would you like to update: ")).lower()
    global curStock
    while not (i in curStock or i == 'exit'):
        i = input(str("\nNot in stock.\nWhich item would you like to update: ")).lower()

def validInt(querry):
    n = input(f"{querry}: ")
    if not n.isdigit():
        n = input(f"\nInvalid Integer\n{querry}:") 
    return n
      
curStock = csvo.getInv()
subDivs = csvo.UBP
def new_shipment_up():
    while True:
        print_inv(curStock)

        upItem = validItem()

        if upItem == 'exit':
            csvo.setInv(curStock)
            break

        else:
            group = validInt(f"Set number of {subDivs[upItem][3]}: ")
            count = validInt(f"Number of remaining {subDivs[upItem][4]}: ")            

            curStock[upItem] = csvo.grpToUse(upItem,group) + count
      
    pass

# Returns nothing, edits inventory.csv