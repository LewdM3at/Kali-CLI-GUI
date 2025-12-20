import subprocess
import curses
import sys
import os
import time

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

def is_wifi_up():
    try:
        result = subprocess.run(["ip", "link", "show", "wlan0"], capture_output=True, text=True)
        return "state UP" in result.stdout
    except Exception:
        return False

def toggle_wifi():
    if is_wifi_up():
        subprocess.run(["sudo", "ip", "link", "set", "wlan0", "down"])
    else:
        subprocess.run(["sudo", "ip", "link", "set", "wlan0", "up"])
        time.sleep(1.5)  # wait for interface to come up

def exit_menu():
    print("\033c", end="")  # full terminal reset
    sys.exit(0)

