#!/usr/bin/python
 
# Import PySide classes
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
 

class App:
  def __init__(self):
    # Create a Qt application
    self.app = QApplication(sys.argv)
    
    # Tray Menu
    trayIconMenu = QMenu()

    settingAction = trayIconMenu.addAction("setting")
    exitAction = trayIconMenu.addAction("exit")

    settingAction.triggered.connect(self.setting)
    exitAction.triggered.connect(sys.exit)
    
    # Tray
    icon = QIcon("icons/Cube.png")

    self.tray = QSystemTrayIcon()
    self.tray.setIcon(icon)
    self.tray.setContextMenu(trayIconMenu)
    self.tray.setToolTip("unko!")
    self.tray.showMessage("hoge", "moge")
    self.tray.showMessage("fuga", "moge")
    self.tray.activated.connect(self.showSearchDialog)
    self.tray.show()
    
  def run(self):
    # Enter Qt application main loop
    self.app.exec_()
    sys.exit()

  def setting(self):
    self.dialog = QDialog()
    self.dialog.setWindowTitle("Setting Dialog")
    self.dialog.show()

  def showSearchDialog(self, reason):
      if reason == QSystemTrayIcon.ActivationReason.Trigger:
          self.setting()

if __name__ == "__main__":
  app = App()
  app.run()