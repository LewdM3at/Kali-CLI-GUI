import curses
from menu import start_menu

if __name__ == "__main__":
    curses.wrapper(start_menu)

