import curses
from curses import textpad



def print_center(stdscr, row, index_hori):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for i in [0, 1, 2]:
        x = w//2 - len(row[i])//2
        y = h//2
        stdscr.addstr(y + i, x, row[i])
    if(index_hori is 0):
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
    curses.curs_set(1)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    index_hori = 0
    index_vert = 0
    h, w = stdscr.getmaxyx()
    txt = []
    txt.append(str('Entrez text1 : '))
    txt.append(str('Entrez text2 : '))
    txt.append(str('Entrez text3 : '))
    print_center(stdscr, txt, index_hori)
    while 1:
        key = stdscr.getch()
        if(chr(key) is 'q'):
            break
        elif(key == curses.KEY_LEFT and index_hori == 1):
            index_hori = 0
        elif(key == curses.KEY_RIGHT and index_hori == 0):
            index_hori = 1
        elif(key == curses.KEY_ENTER or key in [10, 13]):
            break
        elif(key == curses.KEY_UP and index_vert != 0):
            index_vert -= 1
        elif(key == curses.KEY_DOWN and index_vert != 2):
            index_vert += 1
        elif(key != curses.KEY_LEFT and key != curses.KEY_RIGHT and key != curses.KEY_UP and key != curses.KEY_DOWN):
            txt[index_vert] += chr(key)
        print_center(stdscr, txt, index_hori)



curses.wrapper(main)