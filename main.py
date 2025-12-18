#!/usr/bin/env python3
import curses
from menu import run_menu

def main():
    curses.wrapper(run_menu)

if __name__ == "__main__":
    main()
