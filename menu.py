import curses
from menu_items import menu_items
from menu_structure import menu_structure


def draw_ascii_and_title(stdscr, art, title):
    """Draw ASCII art centered, with title below."""
    h, w = stdscr.getmaxyx()
    art_height = len(art)
    art_width = max(len(line) for line in art)

    # Center offsets
    y_offset = (h // 2) - (art_height // 2)
    x_offset = (w // 2) - (art_width // 2)

    # Draw art
    for i, line in enumerate(art):
        stdscr.addstr(y_offset + i, x_offset, line)

    # Draw title below art, centered
    stdscr.addstr(y_offset + art_height + 1,
                  (w // 2) - (len(title) // 2),
                  title)


def run_menu(stdscr, start_menu="main"):
    curses.curs_set(0)
    current_menu = start_menu
    selected_idx = 0

    while True:
        stdscr.clear()
        menu = menu_structure[current_menu]
        item_key = menu["items"][selected_idx]
        item = menu_items[item_key]

        # Draw art + title
        if "art" in item:
            draw_ascii_and_title(stdscr, item["art"], item["label"])
        else:
            draw_ascii_and_title(stdscr, ["(no art)"], item["label"])

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            selected_idx = (selected_idx - 1) % len(menu["items"])
        elif key == curses.KEY_RIGHT:
            selected_idx = (selected_idx + 1) % len(menu["items"])
        elif key in [curses.KEY_ENTER, 10, 13]:
            # Handle actions or submenu navigation
            if "action" in item:
                curses.endwin()  # restore terminal before running action
                item["action"]()
                # after action returns, reinitialize curses
                stdscr = curses.initscr()
                curses.curs_set(0)
            elif "submenu" in item:
                current_menu = item["submenu"]
                selected_idx = 0
            elif item_key == "back":
                # go back to parent menu if defined
                if "parent" in menu_structure[current_menu]:
                    current_menu = menu_structure[current_menu]["parent"]
                    selected_idx = 0
        elif key == 27:  # ESC key
            break


if __name__ == "__main__":
    curses.wrapper(run_menu)
