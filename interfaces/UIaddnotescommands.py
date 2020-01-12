# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/drobinet/Qt/registrycommands/interfaces/addnotescommands.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 288)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/drobinet/Qt/registrycommands/interfaces/../icons/Cube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbTitle.setObjectName("lbTitle")
        self.verticalLayout.addWidget(self.lbTitle)
        self.editTitle = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.editTitle.setObjectName("editTitle")
        self.verticalLayout.addWidget(self.editTitle)
        self.lbNoteCommand = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbNoteCommand.setObjectName("lbNoteCommand")
        self.verticalLayout.addWidget(self.lbNoteCommand)
        self.editNoteCommand = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.editNoteCommand.setObjectName("editNoteCommand")
        self.verticalLayout.addWidget(self.editNoteCommand)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(120, 250, 85, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/drobinet/Qt/registrycommands/interfaces/../icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setObjectName("btnCancel")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(210, 250, 85, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/drobinet/Qt/registrycommands/interfaces/../icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon2)
        self.btnOK.setObjectName("btnOK")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Notes/Commands"))
        self.lbTitle.setText(_translate("Dialog", "Title"))
        self.lbNoteCommand.setText(_translate("Dialog", "Note/Command"))
        self.editNoteCommand.setPlaceholderText(_translate("Dialog", "Note or Command"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
        self.btnOK.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
