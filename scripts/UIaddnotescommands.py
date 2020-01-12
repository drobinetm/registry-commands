# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces/addnotescommands.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from interfaces.UIaddnotescommands import Ui_Dialog
from services.services import Services

class UIAddNotesCommands(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)        
        self.setupUi(self)
        
        self.btnCancel.clicked.connect(self.close)
