from PyQt5 import QtCore,QtGui,QtWidgets
from Models.M_main import *
class  s_mian_ui(Ui_Dialog,QtWidgets.QWidget ):
    def __init__(self):
        super(s_mian_ui, self).__init__()
        self.setupUi(self)
        self.installEventFilter(self)
    def show(self):
        super(s_mian_ui, self).show()
        print("ldj")
