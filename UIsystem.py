# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/drobinet/Qt/registrycommands/system.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from scripts.UIdatabase import UIDatabase as UI_Database
from scripts.UIaddnotescommands import UIAddNotesCommands as UI_AddNotesCommands

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 430)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.extension = QtWidgets.QWidget(Dialog)
        self.extension.setGeometry(QtCore.QRect(10, 120, 429, 311))
        self.extension.setObjectName("extension")
        self.listNotesCommandsFounded = QtWidgets.QListWidget(self.extension)
        self.listNotesCommandsFounded.setGeometry(QtCore.QRect(10, 10, 411, 291))
        self.listNotesCommandsFounded.setObjectName("listNotesCommandsFounded")
        self.lbNotExists = QtWidgets.QLabel(self.extension)
        self.lbNotExists.setGeometry(QtCore.QRect(30, 140, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbNotExists.setFont(font)
        self.lbNotExists.setObjectName("lbNotExists")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 429, 101))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.txtSearchNotesCommands = QtWidgets.QTextEdit(self.groupBox)
        self.txtSearchNotesCommands.setGeometry(QtCore.QRect(10, 60, 411, 31))
        self.txtSearchNotesCommands.setObjectName("txtSearchNotesCommands")
        self.btnHistory = QtWidgets.QPushButton(self.groupBox)
        self.btnHistory.setGeometry(QtCore.QRect(100, 30, 85, 27))
        self.btnHistory.setDefault(True)
        self.btnHistory.setObjectName("btnHistory")
        self.btnAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnAdd.setGeometry(QtCore.QRect(10, 30, 85, 27))
        self.btnAdd.setDefault(True)
        self.btnAdd.setObjectName("btnAdd")
        self.btnDatabase = QtWidgets.QPushButton(self.groupBox)
        self.btnDatabase.setGeometry(QtCore.QRect(340, 30, 85, 27))
        self.btnDatabase.setObjectName("btnDatabase")
        
        self.btnAdd.clicked.connect(self.showAddNotesUI)
        self.btnDatabase.clicked.connect(self.showDatabaseUI)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def showDatabaseUI(self):
        ui = UI_Database()
        ui.exec_()
        ui.show()

    def showAddNotesUI(self):
        ui = UI_AddNotesCommands()
        ui.exec_()
        ui.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbNotExists.setText(_translate("Dialog", "Not found notes or commands on database"))
        self.groupBox.setTitle(_translate("Dialog", "Functions:"))
        self.txtSearchNotesCommands.setPlaceholderText(_translate("Dialog", "Search notes and commands ..."))
        self.btnHistory.setText(_translate("Dialog", "&History"))
        self.btnAdd.setText(_translate("Dialog", "&Add"))
        self.btnDatabase.setText(_translate("Dialog", "&Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
