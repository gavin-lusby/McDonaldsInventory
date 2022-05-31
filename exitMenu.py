from resetScreen import reset_screen


# Exit statements
def exit_menu():
    reset_screen(False)
    print("Exiting program. Some changes may not be saved.\n *Plays McDonald's jingle*\nGoodbye!")
    quit()
# Should return nothing, only exits program
