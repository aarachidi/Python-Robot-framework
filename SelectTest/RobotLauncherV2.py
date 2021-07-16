import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from robot.running import TestSuiteBuilder
from robot.model import SuiteVisitor
import glob
from robot import run
import xml.etree.ElementTree as ET
from os import rename, remove, path, getcwd, chdir
import ntpath
import os
from robot.api import SuiteVisitor
import signal
from robot.running.signalhandler import STOP_SIGNAL_MONITOR
import signal


class OrderTest(SuiteVisitor):

    def __init__(self, obj):
        self.obj = obj
        

    def start_suite(self, suite):
        """Remove tests that match the given pattern."""
        arr_suite = []
        if(len(suite.suites) > 0):
            list_Item = self.obj.getCheckedItem()
            keys = list_Item.keys()
            for key in keys:
                for el in suite.suites:
                    if(el.name.lower() == key.lower()):
                        arr_suite.append(el)
            suite.suites = arr_suite
        arr = []
        for element in self.obj.option['test']:
            for el in suite.tests:
                if(el.name == element):
                    arr.append(el)
        suite.tests = arr




class listener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, filename='listen.txt', obj=None):
        self.obj = obj
        self.prog = obj.getCheckedItemCount()
        self.suite = ""
        self.clicked = False
        try:
            self.prog = 100//self.prog
        except:
            self.prog = 0

    def start_suite(self, name, attrs):
        self.suite = name

    def start_test(self, name, attrs):
        self.obj.text.setText("Actual Suite Test : "+ self.suite+",   actual test : " + name)
        self.obj.colorActuelTest(name, "actuel")

    def end_test(self, name, attrs):
        if self.obj.checkBox.isChecked() :
            if attrs['status'] == "FAIL" and self.clicked == False:
                self.clicked = True
                self.obj.abordTest()
        self.obj.updateProgress(self.obj.pbar.value() + self.prog)
        self.obj.colorActuelTest(name, attrs['status'])


    def end_suite(self, name, attrs):
        a = 4

class TestCasesFinder(SuiteVisitor):
    def __init__(self):
        self.tests = []

    def visit_test(self, test):
        self.tests.append(test)

class myTree(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        QtWidgets.QTreeWidget.__init__(self, parent)
        self.setDragDropMode(self.InternalMove)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
    
    def dragEnterEvent(self, event):
        item = self.itemAt(event.pos())
        QtWidgets.QTreeWidget.dragEnterEvent(self, event)

    def dragMoveEvent(self, event):
        item = self.itemAt(event.pos())
        QtWidgets.QTreeWidget.dragMoveEvent(self, event)
    
    def dropEvent(self, event):
        item = self.itemAt(event.pos())
        return super().dropEvent(event)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        grid = QtWidgets.QGridLayout()

        
        # List of tests
        self.path, self.option, self.data = self.listOfTest()

        

        self.tree = myTree(self)
        self.tree.setHeaderLabel("")
        self.createTreeItems()
        shorcut = QtWidgets.QShortcut(32, 
            self.tree, 
            context=QtCore.Qt.WidgetShortcut,
            activated=self.checkSelectedItem)

        

        # Tree position
        self.tree.resize(500, 400)
        grid.addWidget(self.tree, 2, 1, 4, 5)
        self.tree.setColumnWidth(0, 400)
        

        # Launch Button
        self.pybutton = QtWidgets.QPushButton('Launch', self)
        self.pybutton.resize(100, 60)
        self.pybutton.clicked.connect(self.clickMethodLaunch)
        self.pybutton.setEnabled(False)
        grid.addWidget(self.pybutton, 10, 3)


        #Save Button
        self.pybutton2 = QtWidgets.QPushButton('Save', self)
        self.pybutton2.resize(100, 60)
        self.pybutton2.setEnabled(False)
        self.pybutton2.clicked.connect(self.clickMethodSave)
        grid.addWidget(self.pybutton2, 10, 5)

        #Load Button
        self.pybutton3 = QtWidgets.QPushButton('Load configuration', self)
        self.pybutton3.resize(100, 60)
        self.pybutton3.clicked.connect(self.clickMethodLoad)
        grid.addWidget(self.pybutton3, 10, 1)

        #Select Suite Button
        self.pybutton4 = QtWidgets.QPushButton('Select Suite', self)
        self.pybutton4.resize(100, 60)
        self.pybutton4.clicked.connect(self.clickMethodSuite)
        grid.addWidget(self.pybutton4, 0, 1)

        #Abord Test Button
        self.pybutton5 = QtWidgets.QPushButton('Abord', self)
        self.pybutton5.resize(100, 60)
        self.pybutton5.clicked.connect(self.abordTest)
        grid.addWidget(self.pybutton5, 9, 3)
        self.pybutton5.setEnabled(False)

        #Open Report
        self.pybutton6 = QtWidgets.QPushButton('Open report', self)
        self.pybutton6.resize(100, 60)
        self.pybutton6.clicked.connect(self.openReport)
        grid.addWidget(self.pybutton6, 9, 5)

        grid.setSpacing(50)

        #Progress bar
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.resize(300, 30)
        grid.addWidget(self.pbar, 7, 1, 1, 5)

        #Text of current test
        self.text = QtWidgets.QLabel(text="")
        self.text.setFont(QtGui.QFont('Helvetica font', 20))
        grid.addWidget(self.text, 8, 1, 1, 5)

        #Text of current config file
        self.config = QtWidgets.QLabel(text="")
        self.config.setFont(QtGui.QFont('Helvetica font', 13))
        grid.addWidget(self.config, 0, 2, 1, 5)
        self.setLayout(grid)

        #Text of Suite path
        self.testPath = QtWidgets.QLabel(text="Suite Path : " + self.path)
        self.testPath.setFont(QtGui.QFont('Helvetica font', 13))
        grid.addWidget(self.testPath , 1, 1, 1, 4)
        self.setLayout(grid)

        #CheckBox for exit if test fail
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setText("Exit on first fail")
        grid.addWidget(self.checkBox, 6, 5, 1, 1)


        self.testsuite_running = False
        self.loadBackUp()


    def loadBackUp(self):
        pa = QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.AppDataLocation)[0] + "/backup.xml"
        print("Loading backup configuration from : " + pa)
        if os.path.exists(pa):
            dic = self.readFromXmlFile(pa)
            if(len(dic.keys()) > 0):
                self.unckeckAll()
            for key in dic.keys():
                if(len(dic[key]) > 0):
                    for subElement in dic[key]:
                        self.searchForItem(key, subElement)
            self.disableButton()

    def disableButton(self):
        if(self.getCheckedItemCount() == 0):
            self.pybutton.setEnabled(False)
            self.pybutton2.setEnabled(False)
        else:
            self.pybutton.setEnabled(True)
            self.pybutton2.setEnabled(True)

    def createTreeItems(self):
        keys = self.data.keys()
        if len(keys) > 0:
            self.tree.clear()
        for key in keys:
            parent = QtWidgets.QTreeWidgetItem(self.tree)
            key_temp = ntpath.basename(key)
            title = key_temp.replace(".robot", "")
            parent.setText(0, title)
            parent.setFlags(parent.flags() | Qt.ItemIsTristate |
                            Qt.ItemIsUserCheckable)
            for element in self.data[key]:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags((child.flags() | Qt.ItemIsUserCheckable) & ~Qt.ItemIsDropEnabled)
                child.setText(0, element)
                child.setCheckState(0, Qt.Unchecked)
        self.tree.expandAll()
        self.tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tree.itemClicked.connect(self.disableButton)
        self.tree.itemSelectionChanged.connect(self.disableButton)

    def checkSelectedItem(self):
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    if child.isSelected() == True:
                        if child.checkState(0) == Qt.Checked:
                            child.setCheckState(0, Qt.Unchecked)
                        else:
                            child.setCheckState(0, Qt.Checked)
                    else:
                        recurse(child)

                else:
                    if child.isSelected() == True:
                        if child.checkState(0) == Qt.Checked:
                            child.setCheckState(0, Qt.Unchecked)
                        else:
                            child.setCheckState(0, Qt.Checked)
        recurse(self.tree.invisibleRootItem())
        self.disableButton()
            
    def setWidgetDisabled(self):
        self.pybutton.setEnabled(False)
        self.pybutton2.setEnabled(False)
        self.pybutton3.setEnabled(False)
        self.pybutton4.setEnabled(False)
        self.pybutton5.setEnabled(True)

    def setWidgetEnabled(self):
        self.pybutton.setEnabled(True)
        self.pybutton2.setEnabled(True)
        self.pybutton3.setEnabled(True)
        self.pybutton4.setEnabled(True)
        self.pybutton5.setEnabled(False)

    def clickMethodLaunch(self, event):
        dic = self.getCheckedItem()
        keys = dic.keys()
        self.setWidgetDisabled()

        current_path = getcwd()
        self.option['test'] = []
        self.pbar.setValue(0)

        for key in keys:
            if len(dic[key]) != 0:
                self.option['test'] += dic[key]
        dic = self.getCheckedItem()
        pa = QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.AppDataLocation)[0] + "/backup.xml"
        self.createXMLFile(dic, pa)
        chdir(self.path)

        STOP_SIGNAL_MONITOR.__init__()
        self.testsuite_running = True
        run("./", **self.option, listener=listener(obj=self), prerunmodifier=OrderTest(self))
        self.testsuite_running = False
        chdir(current_path)
        self.updateProgress(100)
        self.text.setText("")
        self.setInitialColor()
        self.setWidgetEnabled()

    def abordTest(self):
        try:
            STOP_SIGNAL_MONITOR(signal.SIGINT, None)
        except:
            pass

    def clickMethodSuite(self):
        dic = self.getCheckedItem()
        pa = QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.AppDataLocation)[0] + "/backup.xml"
        self.createXMLFile(dic, pa)
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.createTree(file)
        print(self.path)

    def createTree(self, file):
        path, dict_Option = self.listOfOption()
        path = file
        files = glob.glob(path+"/*.robot")
        dict = {}
        for file in files:
            dict[file] = []
            builder = TestSuiteBuilder()
            testsuite = builder.build(file)
            finder = TestCasesFinder()
            testsuite.visit(finder)
            for element in finder.tests:
                dict[file].append(element.name)
        self.path, self.option, self.data = path, dict_Option, dict
        self.testPath.setText("Suite Path : " + self.path)
        self.createTreeItems()

    def getCheckedItem(self):
        checked_items = []
        dic = {}

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    dic[child.text(0)] = []
                    recurse(child)

                if child.checkState(0) == Qt.Checked and grand_children == 0:
                    dic[parent_item.text(0)].append(child.text(0))
                    checked_items.append(child.text(0))

        recurse(self.tree.invisibleRootItem())
        return dic

    def getCheckedItemCount(self):
        dic = {}
        dic['count'] = 0

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)

                if child.checkState(0) == Qt.Checked and grand_children == 0:
                    dic['count'] += 1
        recurse(self.tree.invisibleRootItem())
        return dic['count']
    
    def clickMethodSave(self, event):
        self.saveFileDialog()

    def clickMethodLoad(self, event):
        self.openFileNameDialog()
    
    def openReport(self):
        os.system("start " + "report.html")

    def keyPressEvent(self, event):
        if event.key() == 16777220 and not self.testsuite_running :
            self.clickMethodLaunch(event)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Document XML (*.xml)", options=options)
        if fileName:
            dic = self.readFromXmlFile(fileName)
            if(len(dic.keys()) > 0):
                self.unckeckAll()
            for key in dic.keys():
                if(len(dic[key]) > 0):
                    for subElement in dic[key]:
                        self.searchForItem(key, subElement)
    
    def updateProgress(self, value):
        self.pbar.setValue(value)

    def saveFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Document XML (*.xml)", options=options)
        if fileName:
            dic = self.getCheckedItem()
            if(".xml" not in fileName):
                fileName += ".xml"
            self.createXMLFile(dic, fileName)
    
    def createXMLFile(self, dic, path):
        keys = dic.keys()
        data = ET.Element('Tests')
        data.set('path', self.path)
        for key in keys:
            testName = ET.SubElement(data, "Test")
            testName.set('name',key)
            for element in dic[key]:
                elem = ET.SubElement(testName, "Element")
                elem.set('name',element)
        mydata = ET.tostring(data)
        myfile = open(path, "wb")
        myfile.write(mydata)

    def readFromXmlFile(self, path):
        dic = {}
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            self.config.setText("Configuration file : " + (ntpath.basename(path)).replace(".xml", ""))
            for elem in root:
                dic[elem.attrib['name']] = []
                for subelem in elem:
                    dic[elem.attrib['name']].append(subelem.attrib['name'])
            self.createTree(root.attrib['path'])
        except:
            dic = {}
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("File's format not valid")
            msg.setWindowTitle("Error")
            msg.exec_()
        return dic
    
    def unckeckAll(self):
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                child.setCheckState(0, Qt.Unchecked)
        recurse(self.tree.invisibleRootItem())
    

    def searchForItem(self, element, subElement):

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                elif(grand_children == 0 and child.text(0) == subElement):
                    child.setCheckState(0, Qt.Checked)
        recurse(self.tree.invisibleRootItem())
    
    def setInitialColor(self):
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                child.setDisabled(False)
                if grand_children > 0:
                    recurse(child)
                else:
                    child.setForeground(0,QtGui.QBrush(QtGui.QColor("black")))
                    child.setFont(0, QtGui.QFont('Arial', 8))
        recurse(self.tree.invisibleRootItem())
    
    def colorActuelTest(self, name, status):
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                child.setDisabled(True)
                if grand_children > 0:
                    recurse(child)
                elif(grand_children == 0 and child.text(0) == name and child.checkState(0) == Qt.Checked):
                    if status == "actuel":
                        child.setFont(0, QtGui.QFont('Arial', 12, QtGui.QFont.Bold))
                    elif status == "PASS":
                        child.setForeground(0,QtGui.QBrush(QtGui.QColor("green")))
                        child.setFont(0, QtGui.QFont('Arial', 8))
                    elif status == "FAIL":
                        child.setForeground(0,QtGui.QBrush(QtGui.QColor("red")))
                        child.setFont(0, QtGui.QFont('Arial', 8))
        recurse(self.tree.invisibleRootItem())
    
    def listOfTest(self):
        path, dict_Option = self.listOfOption()
        files = glob.glob(path+"/*.robot")
        dict = {}
        for file in files:
            dict[file] = []
            builder = TestSuiteBuilder()
            testsuite = builder.build(file)
            finder = TestCasesFinder()
            testsuite.visit(finder)
            for element in finder.tests:
                dict[file].append(element.name)
        return path, dict_Option, dict
    
    def listOfOption(self):
        dict = {}
        i = 1
        path = "./"
        while(i < len(sys.argv)):
            if(i < len(sys.argv) - 1):
                key = sys.argv[i].strip("-")
                try:
                    dict[key].append(sys.argv[i + 1])
                except:
                    dict[key] = []
                    dict[key].append(sys.argv[i + 1])
            elif(i == len(sys.argv) - 1):
                path = sys.argv[i]
            i += 2
        keys = dict.keys()
        for key in keys:
            if len(dict[key]) == 1:
                dict[key] = dict[key][0]
        return path, dict


application = QtWidgets.QApplication(sys.argv)
window = Window()
window.setWindowTitle('Robot Launcher')
window.resize(800, 900)
window.show()
window.activateWindow()
sys.exit(application.exec_())
