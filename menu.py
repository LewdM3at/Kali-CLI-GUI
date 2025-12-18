#!/usr/bin/env python3
import curses
import sys
from menu_items import menu_items
from menu_structure import menu_structure


def draw_ascii(stdscr, art, y_offset=5, x_offset=2):
    """Draw ASCII art at given offset."""
    for i, line in enumerate(art):
        stdscr.addstr(y_offset + i, x_offset, line)


def draw_menu(stdscr, menu_name, selected_idx):
    """Render a menu with highlighting and ASCII art."""
    stdscr.clear()
    menu = menu_structure[menu_name]

    # Title
    stdscr.addstr(0, 2, f"== {menu['title']} ==")

    # Items
    for idx, key in enumerate(menu["items"]):
        item = menu_items[key]
        label = item["label"]

        if idx == selected_idx:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(2 + idx, 2, label)
            stdscr.attroff(curses.A_REVERSE)

            # Show ASCII art for selected item
            if "art" in item:
                draw_ascii(stdscr, item["art"])
        else:
            stdscr.addstr(2 + idx, 2, label)

    stdscr.refresh()


def run_menu(stdscr, start_menu="main"):
    curses.curs_set(0)
    current_menu = start_menu
    selected_idx = 0

    while True:
        draw_menu(stdscr, current_menu, selected_idx)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected_idx > 0:
            selected_idx -= 1
        elif key == curses.KEY_DOWN and selected_idx < len(menu_structure[current_menu]["items"]) - 1:
            selected_idx += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            # handle selection here
            pass

if __name__ == "__main__":
    curses.wrapper(run_menu)