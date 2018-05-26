from PyQt5 import QtWidgets,QtCore,QtGui
from Models import *
#s_setting-ui为agent设置界面类
class a_setting_ui(Models.M_setting.Ui_Dialog,QtWidgets.QWidget):
    def __init__(self):
        super(a_setting_ui, self).__init__()
        self.setupUi(self)
#a_main_ui为agent主界面类
class a_main_ui(Models.M_main.Ui_Dialog,QtWidgets.QWidget):
    def __init__(self):
        super(a_main_ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.aa)
        self.aa = a_setting_ui()
        self.systemtray=Models.M_tray.M_tray(self)
        self.systemtray.show()
    def aa(self):
        self.aa.show()

