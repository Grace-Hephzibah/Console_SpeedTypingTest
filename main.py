import curses
from curses import wrapper  # Takes control over the terminal to do the styling
import random

# Self created modules
import Sentences_Code as sc
import Word_Code as wc
import Paragraph_Code as pc
import BigPassage_Code as bpc
import Fun as f


def start_screen(stdscr):
    stdscr.clear()  # Clears the screen
    stdscr.addstr("Welcome to the Interactive Console Speed Typing Test  \n")
    # Simply prints the statement (Overwriting can happen)
    # Syntax: (row, col, text, color_pair()  )
    stdscr.addstr("Press \n"
                  "1 for easy mode \n"
                  "2 for medium mode\n"
                  "3 for hard mode\n"
                  "4 for ultimate mode\n"
                  "...   ")
    stdscr.refresh()  # Refreshes the screen
    return stdscr.getkey()


def main(stdscr):
    # color fiddling
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    key_mode = start_screen(stdscr)  # Initiates the game
    mode = 0

    while True:

        # Easy # Score 5
        if ord(key_mode) == 49 or mode == 1:  # ord(1) == 49
            wc.cpm_test(stdscr)  # initializes the gaming process
            y = 6
            x = 0

        # Medium # Score 10
        elif ord(key_mode) == 50 or mode == 2:  # ord(2) == 50
            sc.wpm_test(stdscr)  # initializes the gaming process
            y = 5
            x = 0

        # Hard # Score 15
        elif ord(key_mode) == 51 or mode == 3:  # ord(3) == 51
            pc.wpm_test(stdscr)
            y = 10
            x = 0

        # Ultimate Hard # Score 30
        elif ord(key_mode) == 52 or mode == 4:
            bpc.wpm_test(stdscr)
            y = 20
            x = 0

        stdscr.addstr(y, x, f"{random.choice(f.words)}! {random.choice(f.phrases)}. \n\n") #advancement here using fun
        # Common terms for next round
        stdscr.addstr("E/e to Easy Level \n"
                      "M/m to Medium Level \n"
                      "H/h to Hard Level  \n"
                      "U/u to Ultimate Level\n"
                      "Or press any key to continue in the same level")

        key = stdscr.getkey()

        if ord(key) == 69 or ord(key) == 101:  # Easy
            mode = 1
            key_mode = 'A'

        elif ord(key) == 77 or ord(key) == 109:  # Medium
            mode = 2
            key_mode = 'A'

        elif ord(key) == 72 or ord(key) == 104:  # Hard
            mode = 3
            key_mode = 'A'

        elif ord(key) == 85 or ord(key) == 117:  # Hard
            mode = 4
            key_mode = 'A'

        elif ord(key) == 27:
            break

        # resetting key_mode to avoid the repetition of same level

# E - 69  e - 101
# M - 77  m - 109
# H - 72  h - 104

wrapper(main)