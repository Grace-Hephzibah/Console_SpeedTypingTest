import csv


def add_player():
    pass


def delete_player():
    pass


def clear_score_player():
    pass


def compare_score_player():
    pass


def check_Fulllist():
    pass

def settings_page():

    pass

def main (stdscr):
    with open("PlayerInventoryList.csv", 'r') as file:
        readObj = csv.reader(file)

        for i, row in enumerate(readObj):
            for j, col in enumerate(row):

                if (i==1) and (j>2):
                    col = 0
                    # Guest Portal should always be zero

                elif (i>1) and (j>2):
                    col = int(col)

        stdscr.addstr("Enter the Username : ")
        username = stdscr.getstring()
        stdscr.addstr("\nEnter the Password : ")
        password = stdscr.getstring()



main()
