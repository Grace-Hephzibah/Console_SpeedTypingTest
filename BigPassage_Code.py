import curses

import time
import random
import general_code as gc
import BigPassage as bp


def load_text():
    return random.choice(bp.BigPassage).strip()
    # strip() removes the '\0\ at the end of the string


def display_text(stdscr, target, current, penalty_rate, actual_wpm, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(25, 0, f"WPM : {wpm}", curses.color_pair(3))
    stdscr.addstr(26, 0, f"Penalty : {penalty_rate}", curses.color_pair(3))
    stdscr.addstr(27, 0, f"Actual WPM : {actual_wpm}", curses.color_pair(3))

    lines = 0
    pos = 0

    stdscr.move(0, 0)

    for i, char in enumerate(current):
        # stdscr.addstr(10, 0, f"target: {ord(check)} and current: {ord(char)}", curses.color_pair(3))
        # helps to figure out the context of characters being dealt with

        if ord(target[i]) == ord(char) and ord(char) == 10:
            lines += 1
            pos = 0
            stdscr.move(lines, pos)
            continue
            # Avoids unwanted space

        elif ord(target[i]) == ord(char) and ord(char) == 9:
            pos += 8 - pos%8
            stdscr.move(lines, pos)
            continue

        elif target[i] == current[i]:
            stdscr.addstr(lines, pos, char, curses.color_pair(1))
        else:  # ord(target[i]) != current[i]
            stdscr.addstr(lines, pos, char, curses.color_pair(2))

        pos += 1


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []

    wpm = 0
    start_time = time.time()

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()

    stdscr.nodelay(True)
    # This line does not wait for the getkey() and the wpm is updated dynamically

    while True:
        time_elapsed = max(time.time() - start_time, 1)  # max() avoids the division by error problem
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        # (characters by minute) / 5 = words per minute

        # Penalty calculation code
        penalty_rate, actual_wpm = gc.penalty_code(current_text, target_text, wpm)

        # Display is handled here
        stdscr.clear()
        display_text(stdscr, target_text, current_text, penalty_rate, actual_wpm, wpm)

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