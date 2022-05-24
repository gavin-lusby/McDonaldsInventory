# Created by Gavin (2022-05-24)

from os import system


# Clears output and reprint header every time(T/F depending on if you want it to
# say return to menu or end process)
def reset_screen(return_to_menu):
  system('clear')
  print(f'--------------------------------\n--- McD Inventory Management ---\n--------------------------------\nType exit at any time to {"return to menu" if return_to_menu else "end process"}\n\n')