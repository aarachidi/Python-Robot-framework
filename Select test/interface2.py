import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from robot.running import TestSuiteBuilder
from robot.model import SuiteVisitor
import glob
from robot import run
import xml.etree.ElementTree as ET
from os import rename, remove, path


class TestCasesFinder(SuiteVisitor):
    def __init__(self):
        self.tests = []

    def visit_test(self, test):
        self.tests.append(test)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # List of tests
        data = self.listOfTest()
        keys = data.keys()

        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.setHeaderLabel("")
        for key in keys:
            parent = QtWidgets.QTreeWidgetItem(self.tree)
            title = key.replace(".robot", "")
            parent.setText(0, title)
            parent.setFlags(parent.flags() | Qt.ItemIsTristate |
                            Qt.ItemIsUserCheckable)
            for element in data[key]:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, element)
                child.setCheckState(0, Qt.Unchecked)


        self.tree.expandAll()
        # Tree position
        self.tree.move(50, 50)
        self.tree.setColumnWidth(0, 400)
        self.tree.resize(500, 400)

        # Launch Button
        pybutton = QtWidgets.QPushButton('Launch', self)
        pybutton.resize(100, 60)
        pybutton.clicked.connect(self.clickMethodLaunch)
        pybutton.move(250, 500)

        #Save Button
        pybutton2 = QtWidgets.QPushButton('Save', self)
        pybutton2.resize(100, 60)
        pybutton2.move(400, 500)
        pybutton2.clicked.connect(self.clickMethodSave)

        #Load Button
        pybutton3 = QtWidgets.QPushButton('Load', self)
        pybutton3.resize(100, 60)
        pybutton3.move(100, 500)
        pybutton3.clicked.connect(self.clickMethodLoad)

    def clickMethodLaunch(self, event):
        dic = self.getCheckedItem()
        keys = dic.keys()
        self.setEnabled(False)
        for key in keys:
            if len(dic[key]) != 0:
                pa = key + ".robot"
                run(pa, name='Example', test=dic[key])
                if path.exists(key + ".html"):
                    remove(key + ".html")
                rename("report.html", key + ".html")
        self.setEnabled(True)
        print(dic)

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

    def listOfTest(self):
        files = glob.glob("*.robot")
        dict = {}
        for file in files:
            dict[file] = []
            builder = TestSuiteBuilder()
            testsuite = builder.build(file)
            finder = TestCasesFinder()
            testsuite.visit(finder)
            for element in finder.tests:
                dict[file].append(element.name)
        return dict

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




application = QtWidgets.QApplication(sys.argv)
window = Window()
window.setWindowTitle('Robot Launcher')
window.resize(600, 600)
window.show()
sys.exit(application.exec_())
