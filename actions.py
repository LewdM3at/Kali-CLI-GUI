import subprocess
import curses
import sys
import os

def auto_audit_attack():
    curses.endwin()
    # Reset terminal state (important after curses)
    os.system("stty sane")
    # Clear the screen so ncurses UI is gone
    os.system("clear")
    subprocess.run(["sudo", "wifite", "--daemon"])

def pmkid_attack():
    curses.endwin()
    # Reset terminal state (important after curses)
    os.system("stty sane")
    # Clear the screen so ncurses UI is gone
    os.system("clear")
    subprocess.run(["sudo", "wifite", "--pmkid", "--daemon"])

def handshake_attack():
    curses.endwin()
    # Reset terminal state (important after curses)
    os.system("stty sane")
    # Clear the screen so ncurses UI is gone
    os.system("clear")
    subprocess.run(["sudo", "wifite", "--no-pmkid", "--no-wps", "--daemon"])

def pixiedust_attack():
    curses.endwin()
    # Reset terminal state (important after curses)
    os.system("stty sane")
    # Clear the screen so ncurses UI is gone
    os.system("clear")
    subprocess.run(["sudo", "wifite", "--pixie", "--no-pmkid", "--wps-only", "--daemon"])

def pin_attack():
    curses.endwin()
    # Reset terminal state (important after curses)
    os.system("stty sane")
    # Clear the screen so ncurses UI is gone
    os.system("clear")
    subprocess.run(["sudo", "wifite", "--no-pixie", "--no-pmkid", "--wps-only", "--daemon"])

def exit_menu():
    print("\033c", end="")  # full terminal reset
    sys.exit(0)

