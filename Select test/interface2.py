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


class TestCasesFinder(SuiteVisitor):
    def __init__(self):
        self.tests = []

    def visit_test(self, test):
        self.tests.append(test)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QtWidgets.QGridLayout()

        # List of tests
        self.path, self.option, self.data = self.listOfTest()
        print(self.option)
        keys = self.data.keys()

        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.setHeaderLabel("")
        for key in keys:
            parent = QtWidgets.QTreeWidgetItem(self.tree)
            key_temp = ntpath.basename(key)
            title = key_temp.replace(".robot", "")
            parent.setText(0, title)
            parent.setFlags(parent.flags() | Qt.ItemIsTristate |
                            Qt.ItemIsUserCheckable)
            for element in self.data[key]:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, element)
                child.setCheckState(0, Qt.Unchecked)


        self.tree.expandAll()
        # Tree position
        self.tree.resize(500, 400)
        grid.addWidget(self.tree, 1, 1, 3, 5)
        self.tree.setColumnWidth(0, 400)
        

        # Launch Button
        pybutton = QtWidgets.QPushButton('Launch', self)
        pybutton.resize(100, 60)
        pybutton.clicked.connect(self.clickMethodLaunch)
        grid.addWidget(pybutton, 5, 3)

        #Save Button
        pybutton2 = QtWidgets.QPushButton('Save', self)
        pybutton2.resize(100, 60)
        grid.addWidget(pybutton2, 5, 5)
        pybutton2.clicked.connect(self.clickMethodSave)

        #Load Button
        pybutton3 = QtWidgets.QPushButton('Load', self)
        pybutton3.resize(100, 60)
        grid.addWidget(pybutton3, 5, 1)
        pybutton3.clicked.connect(self.clickMethodLoad)

        grid.setSpacing(50)

        #Progress bar
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.resize(300, 30)
        grid.addWidget(self.pbar, 4, 2, 1, 3)

        self.setLayout(grid)

    def clickMethodLaunch(self, event):
        dic = self.getCheckedItem()
        keys = dic.keys()
        self.setEnabled(False)
        current_path = getcwd()
        self.option['test'] = []
        for key in keys:
            if len(dic[key]) != 0:
                chdir(self.path)
                pa = key + ".robot"
                self.option['test'] = dic[key]
                print(self.option)
                run(pa, **self.option)
                if path.exists(key + ".html"):
                    remove(key + ".html")
                chdir(current_path)
                if path.exists(key + ".html"):
                    remove(key + ".html")
                rename("report.html", self.path+"/" + key + ".html")
                chdir(self.path)
        chdir(current_path)
        self.setEnabled(True)

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
    
    def clickMethodSave(self, event):
        self.saveFileDialog()

    def clickMethodLoad(self, event):
        self.openFileNameDialog()

    def keyPressEvent(self, event):
        if event.key() == 16777220:
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
            for elem in root:
                dic[elem.attrib['name']] = []
                for subelem in elem:
                    dic[elem.attrib['name']].append(subelem.attrib['name'])
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
window.resize(600, 600)
window.show()
sys.exit(application.exec_())
