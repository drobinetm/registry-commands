# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/drobinet/Qt/registrycommands/ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(447, 306)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 150)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.txtSearchNotesCommands_5 = QtWidgets.QTextEdit(self.groupBox)
        self.txtSearchNotesCommands_5.setGeometry(QtCore.QRect(10, 60, 411, 31))
        self.txtSearchNotesCommands_5.setObjectName("txtSearchNotesCommands_5")
        self.btnShowHide_5 = QtWidgets.QPushButton(self.groupBox)
        self.btnShowHide_5.setGeometry(QtCore.QRect(390, 30, 31, 27))
        self.btnShowHide_5.setCheckable(True)
        self.btnShowHide_5.setAutoDefault(False)
        self.btnShowHide_5.setObjectName("btnShowHide_5")
        self.btnHistory_5 = QtWidgets.QPushButton(self.groupBox)
        self.btnHistory_5.setGeometry(QtCore.QRect(100, 30, 85, 27))
        self.btnHistory_5.setDefault(True)
        self.btnHistory_5.setObjectName("btnHistory_5")
        self.btnAdd_5 = QtWidgets.QPushButton(self.groupBox)
        self.btnAdd_5.setGeometry(QtCore.QRect(10, 30, 85, 27))
        self.btnAdd_5.setDefault(True)
        self.btnAdd_5.setObjectName("btnAdd_5")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.extension = QtWidgets.QWidget(self.gridLayoutWidget)
        self.extension.setObjectName("extension")
        self.listNotesCommandsFounded_2 = QtWidgets.QListWidget(self.extension)
        self.listNotesCommandsFounded_2.setGeometry(QtCore.QRect(10, 10, 411, 291))
        self.listNotesCommandsFounded_2.setObjectName("listNotesCommandsFounded_2")
        self.gridLayout_2.addWidget(self.extension, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.btnShowHide_5.toggled['bool'].connect(self.extension.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Functions:"))
        self.txtSearchNotesCommands_5.setPlaceholderText(_translate("Form", "Search notes and commands ..."))
        self.btnShowHide_5.setText(_translate("Form", "..."))
        self.btnHistory_5.setText(_translate("Form", "&History"))
        self.btnAdd_5.setText(_translate("Form", "&Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
