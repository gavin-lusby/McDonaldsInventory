# Manager manual update inventory function (includes new shipments and recalibrating total product stock)

from resetScreen import reset_screen
import csvo


def print_inv(inv):
    reset_screen(True)
    for i in inv:
        print(i, inv[i])


def new_shipment_up():
    while True:
        inv = csvo.getInv()
        print_inv(inv)

    pass
# Returns nothing, edits inventory.csv
