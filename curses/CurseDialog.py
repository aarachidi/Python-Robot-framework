import curses
from curses import textpad

class CurseDialog():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        
        self.index_vert = 0
        self.inputs = []
        self.results = []
        self.key = []
    
    def show(self):
        curses.wrapper(self.do)

    def do(self, stdscr):
        curses.curs_set(1)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.print_center(stdscr, self.inputs, self.index_vert)
        self.getInput(stdscr)
    
        
    def createInput(self, text="", name=""):
        self.inputs.append(text+" : ")
        self.results.append(str())
        self.key.append(name)


    def getResult(self):
        dic = {}
        i = 0
        for element in self.key:
            dic[element] = self.results[i]
            i += 1
        return dic

    def getInput(self, stdscr):
        while 1:
            key = stdscr.getch()
            if(chr(key) is 'q'):
                break
            elif((key == curses.KEY_ENTER or key in [10, 13]) and self.index_vert == len(self.inputs)):
                break
            elif(key == curses.KEY_UP and self.index_vert != 0):
                self.index_vert -= 1
            elif(key == curses.KEY_DOWN and self.index_vert != len(self.inputs)):
                self.index_vert += 1
            elif(key == 8):
                self.inputs[self.index_vert] = self.inputs[self.index_vert][:-1]
                self.results[self.index_vert] = self.results[self.index_vert][:-1]
            elif(key >= 32 and key <= 126):
                self.inputs[self.index_vert] += chr(key)
                self.results[self.index_vert] += chr(key)
            self.print_center(stdscr, self.inputs, self.index_vert)
            

    def print_center(self, stdscr, row, index_vert):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        i = 0
        for element in row:
            x = w//2 - len(element)//2
            y = h//2
            if(index_vert == i):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y + i, x, element)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y + i, x, element)
            i += 1
        if(index_vert == i):
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(h//2 + i + 4, w//2 - 2, "Validate")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(h//2 + i + 4, w//2 - 2, "Validate")
        stdscr.refresh()