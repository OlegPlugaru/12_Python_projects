import curses
import time

def main(stdscr):
    # Set up curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)  # Don't wait for user input

    # Define the heart shape
    heart = [
"                                    ",
"                                    ",        
"     8888888888                     ",
"    888888888888888                 ",
"   888888822222228888               ",
" 88888822222222288888               ",
"888888222222222228888822228888      ",
"888882222222222222288222222222888   ",
"8888822222222222222222222222222288  ",
" 8888822222222222222222222222222_88 ",
" 88888222222222222222222222222__888 ",
"  888822222222222222222222222___888 ",
"   8888222222222222222222222____888 ",
"    8888222222222222222222_____888  ",
"     8882222222222222222_____8888   ",
"      888822222222222______888888   ",
"       8888882222______88888888     ",
"        888888_____888888888        ",
"         88888888888888             ",
"          8888888888                ",
"           8888888                  ",
"            88888                   ",
"             888                    ",
"              8                     ",

    ]
    max_y, max_x = stdscr.getmaxyx()

    # Position the heart in the middle of the screen
    y = max_y // 2 - len(heart) // 2
    x = max_x // 2 - len(heart[0]) // 2

    # Draw the heart
    def draw_heart():
        for i, row in enumerate(heart):
            try:
                stdscr.addstr(y + i, x, row)
            except curses.error:
                pass

    # Animate the heart beating
    while True:
        # Increase the size of the heart
        for i in range(1, 4):
            height = len(heart) + i * 2
            width = len(heart[0]) + i * 2
            y = max_y // 2 - height // 2
            x = max_x // 2 - width // 2
            stdscr.clear()
            draw_heart()
            stdscr.refresh()
            time.sleep(0.1)

        # Decrease the size of the heart
        for i in range(3, 0, -1):
            height = len(heart) + i * 2
            width = len(heart[0]) + i * 2
            y = max_y // 2 - height // 2
            x = max_x // 2 - width // 2
            stdscr.clear()
            draw_heart()
            stdscr.refresh()
            time.sleep(0.1)

curses.wrapper(main)
