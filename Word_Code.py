import curses

import words # Has a random set of English Words

import time
import random
import general_code as gc


def load_text():
    return random.choice(words.words).strip()
    # strip() removes the '\0\ at the end of the string

def display_text(stdscr, target, current, penalty_rate, actual_cpm, cpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"CPM : {cpm}", curses.color_pair(3))
    stdscr.addstr(2, 0, f"Penalty : {penalty_rate}", curses.color_pair(3))
    stdscr.addstr(3, 0, f"Actual CPM : {actual_cpm}", curses.color_pair(3))
    stdscr.move(0, 0)

    for i, char in enumerate(current):
        if target[i] == current[i]:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:  # target[i] != current[i]
            stdscr.addstr(0, i, char, curses.color_pair(2))


def cpm_test(stdscr):
    target_text = load_text()
    # target_text = tt.load_text() ## Dummy text for testing purposes
    current_text = []

    cpm = 0
    start_time = time.time()

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()

    stdscr.nodelay(True)
    # This line does not wait for the getkey() and the wpm is updated dynamically

    while True:
        time_elapsed = max(time.time() - start_time, 1)  # max() avoids the division by error problem
        cpm = round(len(current_text) / (time_elapsed / 60))
        # (characters by minute) / 5 = words per minute

        # Penalty calculation code
        penalty_rate, actual_cpm = gc.penalty_code(current_text, target_text, cpm)

        # Display is handled here
        stdscr.clear()
        display_text(stdscr, target_text, current_text, penalty_rate, actual_cpm, cpm)

        # Ending the game code
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # Code ends with penalty
        if len(current_text) == len(target_text):
            stdscr.nodelay(False)
            break

        # Removing this block as it throws an exception
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # Checking if the key entered in escape key
            break

        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            # Different ways of representation of backspace on different OS
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text += [key]

