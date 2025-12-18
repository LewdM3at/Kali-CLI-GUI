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
        try:
            stdscr.addstr(y_offset + i, x_offset, line)
        except curses.error:
            pass  # ignore if drawing goes out of bounds

    # Draw title below art, centered
    try:
        stdscr.addstr(y_offset + art_height + 1,
                      (w // 2) - (len(title) // 2),
                      title)
    except curses.error:
        pass


def run_menu(stdscr, start_menu="main"):
    curses.curs_set(0)
    current_menu = start_menu
    selected_idx = 0
    menu_stack = [current_menu]

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
                curses.endwin()
                item["action"]()
                # If action returns, reinitialize curses
                stdscr = curses.initscr()
                curses.curs_set(0)
            elif "submenu" in item:
                menu_stack.append(item["submenu"])
                current_menu = item["submenu"]
                selected_idx = 0
            elif item_key == "back":
                if len(menu_stack) > 1:
                    menu_stack.pop()
                    current_menu = menu_stack[-1]
                    selected_idx = 0
        elif key == 27:  # ESC key
            break
