# Created by Gavin (2022-05-24)

import os


# Clears output and reprint header every time(T/F depending on if you want it to
# say return to menu or end process)
def reset_screen(return_to_menu):
    os.system('cls' if os.name == 'nt' else 'clear')  # Note this must be run in a terminal otherwise it will not clear
    print(
        f'--------------------------------\n--- McD Inventory Management ---\n--------------------------------\nType '
        f'exit at any time to {"return to menu" if return_to_menu else "end process"}\n\n')
