import sys
from robot import run
from multiprocessing import Process
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from robot.libraries.BuiltIn import BuiltIn
class run3:
    def f(self):
        run("bot2.robot")
    

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.r = run3()
        self.p = None
        self.p2 = None
        grid = QtWidgets.QGridLayout()
        #Load Button
        self.pybutton3 = QtWidgets.QPushButton('Load', self)
        self.pybutton3.resize(100, 60)
        self.pybutton3.clicked.connect(self.clickMethodLoad)
        grid.addWidget(self.pybutton3, 1, 1)

        #Abord Test Button
        self.pybutton5 = QtWidgets.QPushButton('Abord', self)
        self.pybutton5.resize(100, 60)
        self.pybutton5.clicked.connect(self.abordTest)
        grid.addWidget(self.pybutton5, 1, 3)
        self.a = 0

        self.setLayout(grid)
    
    def clickMethodLoad(self):
        self.p = Process(target=self.r.f)
        self.p.start()
        
    
    def abordTest(self):
        self.p.terminate()
        print("can be done")


if __name__ == "__main__":
    #p = Process(target=f)
    #p.start()
    #p.join()

    application = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setWindowTitle('Robot Launcher')
    window.resize(800, 800)
    window.show()
    window.activateWindow()
    sys.exit(application.exec_())


dict1 = {
    "name" : "exemple",
    "test" : "test Function"
}

#run("bot.robot", **dict)