import curses
from curses import textpad



def print_menu(stdscr, row, index):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(row)//2
    y = h//2
    stdscr.addstr(y, x, row)
    if(index is 0):
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(h-3, 0, "Quit")
        stdscr.attroff(curses.color_pair(1))
        stdscr.addstr(h-3, w-10, "Validate")
    else:
        stdscr.addstr(h-3, 0, "Quit")
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(h-3, w-10, "Validate")
        stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    index = 0
    h, w = stdscr.getmaxyx()
    txt = str()
    stdscr.addstr(h-3, 0, "Quit")
    stdscr.addstr(h-3, w-10, "Validate")
    stdscr.refresh()
    while 1:
        key = stdscr.getch()
        if(chr(key) is 'q'):
            break
        elif(key == curses.KEY_LEFT and index == 1):
            index = 0
        elif(key == curses.KEY_RIGHT and index == 0):
            index = 1
        elif(key == curses.KEY_ENTER or key in [10, 13]):
            break
        elif(key != curses.KEY_LEFT and key != curses.KEY_RIGHT):
            txt += chr(key)
        print_menu(stdscr, txt, index)



curses.wrapper(main)