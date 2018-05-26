from PyQt5 import QtCore,QtGui,QtWidgets
from Models.M_main import *
from Models.M_tray import *
class  s_mian_ui(Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(s_mian_ui, self).__init__()
        self.setupUi(self)
        llll=M_tray(self)
        llll.show()

