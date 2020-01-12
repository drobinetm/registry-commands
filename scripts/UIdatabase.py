# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/drobinet/Qt/registrycommands/interfaces/database.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from interfaces.UIdatabase import Ui_Dialog
from services.services import Services

class UIDatabase(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)        
        self.setupUi(self)
        self.openConectionSetting()
        
        self.btnTestConnection.clicked.connect(self.testConectionDatabase)
        self.btnOK.clicked.connect(self.saveConectionDatabase)
        self.btnCancel.clicked.connect(self.close)
        
    def openConectionSetting(self):
        self.services = Services("", 0, "", "")
        self.services.read_settings_connection()
        
        self.lineEdit.setText(self.services.server)
        self.lineEdit_2.setText(str(self.services.port))
        self.lineEdit_3.setText(self.services.user)
        self.lineEdit_4.setText(self.services.password)
                
    def createConectionServices(self):
        server = self.lineEdit.text()
        port = self.lineEdit_2.text()
        user = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        
        self.services = Services(server, int(port), user, password)
        
    def testConectionDatabase(self):  
        self.createConectionServices()
            
        openConection = self.services.connection()
                
        if openConection is not False:
            QtWidgets.QMessageBox.information(None, "Information", "Database conection success") 
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "Error Database conection") 
        
    def saveConectionDatabase(self, ):
        self.createConectionServices()
        self.services.write_settings_connection()
        self.close()
