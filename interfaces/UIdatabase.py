# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/drobinet/Qt/registrycommands/interfaces/database.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(291, 328)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/drobinet/Qt/registrycommands/interfaces/../icons/Cube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbServer = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbServer.setObjectName("lbServer")
        self.verticalLayout.addWidget(self.lbServer)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lbPort = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbPort.setObjectName("lbPort")
        self.verticalLayout.addWidget(self.lbPort)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lbUser = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbUser.setObjectName("lbUser")
        self.verticalLayout.addWidget(self.lbUser)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lbPassword = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbPassword.setObjectName("lbPassword")
        self.verticalLayout.addWidget(self.lbPassword)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.btnTestConnection = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnTestConnection.setObjectName("btnTestConnection")
        self.verticalLayout.addWidget(self.btnTestConnection)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(40, 270, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(60, 290, 85, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/drobinet/Qt/registrycommands/interfaces/../icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setObjectName("btnCancel")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(150, 290, 81, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/drobinet/Qt/registrycommands/interfaces/../icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon2)
        self.btnOK.setObjectName("btnOK")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings Database"))
        self.lbServer.setText(_translate("Dialog", "Server:"))
        self.lbPort.setText(_translate("Dialog", "Port:"))
        self.lbUser.setText(_translate("Dialog", "User:"))
        self.lbPassword.setText(_translate("Dialog", "Password:"))
        self.btnTestConnection.setText(_translate("Dialog", "Test Connection"))
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
