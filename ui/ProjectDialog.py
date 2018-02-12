# coding:utf8
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui


QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class ProjectDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        super(ProjectDialog, self).__init__(parent)

        # Interface set
        self.setWindowTitle("Set Project Directory")
        self.setMinimumSize(400, 200)

        # Object set
        self.createSetProjectGroupBox()
        self.createFolderNameGroupBox()
        self.createButtonsLayout()

        # Main layout set
        main_layout = QtGui.QVBoxLayout()
        main_layout.addWidget(self.setProjectGroupBox)
        main_layout.addWidget(self.setFolderNameGroupBox)
        main_layout.addStretch()
        main_layout.addLayout(self.buttonsLayout)
        self.setLayout(main_layout)

    def createSetProjectGroupBox(self):
        self.setProjectGroupBox = QtGui.QGroupBox("Set Project")

        label_project = QtGui.QLabel(self.tr("工程目录"))
        self.line_edit_project = QtGui.QLineEdit(u"输入项目路径")
        button_project = self.createButton("...", self.openProjectDirectory)

        setProjectGroupBoxLayout = QtGui.QGridLayout()
        setProjectGroupBoxLayout.addWidget(label_project, 0, 0)
        setProjectGroupBoxLayout.addWidget(self.line_edit_project, 0, 1)
        setProjectGroupBoxLayout.addWidget(button_project, 0, 2)
        self.setProjectGroupBox.setLayout(setProjectGroupBoxLayout)

    def createFolderNameGroupBox(self):
        self.setFolderNameGroupBox = QtGui.QGroupBox("Folder Name")

        label_animation = QtGui.QLabel(self.tr("动画文件夹名"))
        label_asset = QtGui.QLabel(self.tr("资产文件夹名"))

        line_edit_animation = QtGui.QLineEdit("Animation")
        line_edit_asset = QtGui.QLineEdit("Asset")

        setFolderNameGroupBoxLayout = QtGui.QGridLayout()
        setFolderNameGroupBoxLayout.addWidget(label_animation, 0, 0)
        setFolderNameGroupBoxLayout.addWidget(line_edit_animation, 0, 1)
        setFolderNameGroupBoxLayout.addWidget(label_asset, 1, 0)
        setFolderNameGroupBoxLayout.addWidget(line_edit_asset, 1, 1)
        self.setFolderNameGroupBox.setLayout(setFolderNameGroupBoxLayout)

    def createButtonsLayout(self):
        self.button_ok = self.createButton("OK", self.savePorjectData)
        self.button_cancel = self.createButton("Cancel", self.close)

        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.button_ok)
        self.buttonsLayout.addWidget(self.button_cancel)

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

    def openProjectDirectory(self):
        self.poject_directory = QtGui.QFileDialog.getExistingDirectory(self, "Open file directory")
        self.line_edit_project.setText(str(self.poject_directory))

    def savePorjectData(self):
        # TODO: 把数据保存为临时文件好让主窗口的表格提取数据。

        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication([])
    myui = ProjectDialog()
    myui.show()
    app.exec_()
