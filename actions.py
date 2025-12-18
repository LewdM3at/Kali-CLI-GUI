import subprocess
import curses
import sys

def pmkid_attack():
    curses.endwin()
    subprocess.run(["sudo", "wifite", "--pmkid"])


def exit_menu():
    print("\033c", end="")  # full terminal reset
    sys.exit(0)

