# coding:utf8

import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import core.ProjectData as FD
import ui.ProjectDialog as PD


QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Set MainWindow
        self.setWindowTitle("Rendering Management")
        self.setMinimumSize(625, 400)
        # self.resize(625, 160)

        # Set CentralWidget
        self.tabWidget = QtGui.QTabWidget(self)
        self.setCentralWidget(self.tabWidget)

        # Set Interface
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()

        # Set Tab
        # self.addTabWidget()

    def newFile(self):
        global set_project
        set_project = PD.ProjectDialog(self)
        set_project.show()
        if 1==1:        # FIXME: 点击OK后触发
            self.addTabWidget()

    def setProject(self):

        pass

    def closeFile(self):
        self.removeTabWidget()

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")

        # New
        self.newAct =  QtGui.QAction(QtGui.QIcon(
                r'D:\Ben\Python\Rendering_Management\ui\images\new.png'),
                "&New", self,
                shortcut = QtGui.QKeySequence.New,
                statusTip = "Create a new file",
                triggered = self.newFile)
        self.fileMenu.addAction(self.newAct)

        # Open
        # self.openAct =  QtGui.QAction("&Open", self,
        #         shortcut = QtGui.QKeySequence.Open,
        #         statusTip = "Open an existing file",
        #         triggered = self.openFile)
        # self.fileMenu.addAction(self.openAct)

        #  close
        self.closeAct =  QtGui.QAction("&Close", self,
                shortcut = "Ctrl+W",
                statusTip = "Close current tab",
                triggered = self.closeFile)
        self.fileMenu.addAction(self.closeAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newAct)
        # self.fileToolBar.addAction(self.openAct)
        # self.fileToolBar.addAction(self.saveAct)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def createTable(self):

        # TODO：根据工程目录数据生成表格
        self.table = QtGui.QTableWidget()
        self.table.setColumnCount(6)
        self.table.setRowCount(2)
        self.table.setItem(0, 0, QtGui.QTableWidgetItem(self.tr("CutNum")))
        self.table.setItem(0, 1, QtGui.QTableWidgetItem(self.tr("Members")))
        self.table.setItem(0, 2, QtGui.QTableWidgetItem(self.tr("Frames")))
        self.table.setItem(0, 3, QtGui.QTableWidgetItem(self.tr("Status")))
        self.table.setItem(0, 4, QtGui.QTableWidgetItem(self.tr("Feedback")))
        self.table.setItem(0, 5, QtGui.QTableWidgetItem(self.tr("Notes")))

    def addTabWidget(self):
        # tabCount = self.tabWidget.count()
        self.createTable()

        tabName = " Tab %d " % (self.tabWidget.count()+1)
        self.tabWidget.addTab(self.table, tabName)
        self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)

        if self.tabWidget.count() == 1:
            self.tabWidget.tabBar().hide()
        else:
            self.tabWidget.tabBar().show()

    def removeTabWidget(self):
        currentTab = self.tabWidget.currentIndex()
        self.tabWidget.removeTab(currentTab)

if __name__ == "__main__":
    app = QtGui.QApplication([])
    myui = MainWindow()
    myui.show()
    app.exec_()

