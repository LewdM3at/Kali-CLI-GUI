import subprocess
import curses
import sys

def pmkid_attack():
    curses.endwin()
    print("\033c", end="")  # full terminal reset
    subprocess.run(["sudo", "wifite", "--pmkid", "--daemon"])

def handshake_attack():
    curses.endwin()
    print("\033c", end="")  # full terminal reset
    subprocess.run(["sudo", "wifite", "--no-pmkid", "--no-wps", "--daemon"])

def pixiedust_attack():
    curses.endwin()
    print("\033c", end="")  # full terminal reset
    subprocess.run(["sudo", "wifite", "--pixie", "--no-pmkid", "--wps-only", "--daemon"])

def pin_attack():
    curses.endwin()
    print("\033c", end="")  # full terminal reset
    subprocess.run(["sudo", "wifite", "--no-pixie", "--no-pmkid", "--wps-only", "--daemon"])

def exit_menu():
    print("\033c", end="")  # full terminal reset
    sys.exit(0)

