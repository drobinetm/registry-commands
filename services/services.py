# -*- coding: utf-8 -*-


from PyQt5.QtSql import QSqlDatabase
from models.settings import Settings
import pickle, os


class Services:
    def __init__(self, server, port, user, password):
        self.db = None
        self.databasename = 'notes_commands'
        self.filename = ".notes_commands.pkl"
        
        self.server = server
        self.port = port
        self.user = user
        self.password = password

    def connection(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName(self.server)
        self.db.setPort(int(self.port))
        self.db.setUserName(self.user)
        self.db.setPassword(self.password)
        self.db.setDatabaseName(self.databasename)        
        return self.db.open()

    def write_settings_connection(self):
        setting = Settings(server=self.server,port=self.port,user=self.user,password=self.password)
        with open(self.filename, 'wb') as output:
            pickle.dump(setting, output, pickle.HIGHEST_PROTOCOL)

    def read_settings_connection(self):
        if not os.path.exists(self.filename):
            self.port = 3306
            return
            
        with open(self.filename, 'rb') as output:
            setting = pickle.load(output)

            self.server = setting.server
            self.port = setting.port
            self.user = setting.user
            self.password = setting.password
