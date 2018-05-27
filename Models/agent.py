from PyQt5 import QtWidgets,QtCore,QtGui
from Models import *
from Libs import *
import os
#s_setting-ui为agent设置界面类
fileofconfig=os.path.dirname(os.path.dirname(__file__))+"/config.txt"
#s_setting-ui为agent设置界面类
class a_setting_ui(Models.M_setting.Ui_Dialog,QtWidgets.QWidget):
    def __init__(self):
        super(a_setting_ui, self).__init__()
        self.setupUi(self)
        self.config()
        self.pushButton.clicked.connect(self.saveconfig)
    def saveconfig(self):
        aa=self.textEdit.toPlainText().split('\n')
        Libs.libs_files.s_write(fileofconfig,aa)
    def config(self):
        if os.path.exists(fileofconfig):
            for i in Libs.libs_files.s_read(fileofconfig):
                self.textEdit.append(i.strip('\n'))
        else:
            print("no")
#a_main_ui为agent主界面类
class a_main_ui(Models.M_main.Ui_Dialog,QtWidgets.QWidget):
    def __init__(self):
        super(a_main_ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.aa)
        #设置界面
        self.aa = a_setting_ui()
        self.systemtray=Models.M_tray.M_tray(self)
        self.systemtray.show()
    def aa(self):
        self.aa.show()
    def closeEvent(self, QCloseEvent):
        #先忽略事件，再将界面隐藏
        QCloseEvent.ignore()
        self.hide()



