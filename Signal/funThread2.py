import time, sys
from PyQt5.QtCore  import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from robot import run
from robot.libraries.BuiltIn import BuiltIn
import os
import signal
import logging



class listener:
    ROBOT_LISTENER_API_VERSION = 2
    def __init__(self, filename='listen.txt', obj=None):
        self.obj = obj
        pass

    def start_suite(self, name, attrs):
        self.suite = name

    def start_test(self, name, attrs):
        pass

    def kill(self):
        os.kill(os.getpid(), signal.SIGINT)

    def end_test(self, name, attrs):
        pass

    def end_suite(self, name, attrs):
        a = 4

class Worker(QObject):
    'Object managing the simulation'

    stepIncreased = pyqtSignal(int)

    def __init__(self):
        super(Worker, self).__init__()
        self.listener = listener(obj=self)
        self._step = 0
        self._isRunning = True
        self._maxSteps = 20

    def task(self):
        
        run("bot.robot", listener=self.listener)

        print("finished...")

    def stop(self):
        self.listener.kill()
        #os.kill(signal.CTRL_C_EVENT, 0)
        #os.kill(os.getpid(), signal.SIGINT)


class SimulationUi(QtWidgets.QDialog):
    def __init__(self):
        super(SimulationUi, self).__init__()

        self.btnStart = QtWidgets.QPushButton('Start')
        self.btnStop = QtWidgets.QPushButton('Stop')
        self.currentStep = QtWidgets.QSpinBox()

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.btnStart)
        self.layout.addWidget(self.btnStop)
        self.layout.addWidget(self.currentStep)
        self.setLayout(self.layout)

        self.thread = QThread()
        self.thread.start()

        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.worker.stepIncreased.connect(self.currentStep.setValue)

        self.btnStop.clicked.connect(self.stop_thread)
        self.btnStart.clicked.connect(self.worker.task)

        #self.finished.connect(self.stop_thread)

    def stop_thread(self):
        # args = sys.argv[:]  # get shallow copy of running script args
        # args.insert(0, sys.executable)  # give it the executable
        # os.execv(sys.executable, args)
        self.worker.stop()
        #os.kill(os.getpid(), signal.SIGINT)
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    simul = SimulationUi()
    simul.show()
    sys.exit(app.exec_())