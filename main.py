from  Models.M_main import *
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
class my_main_ui(Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(my_main_ui, self).__init__()
        self.setupUi(self)
        self.textEdit.textChanged.connect(lambda:print(self.textEdit.toPlainText()))

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    Win1=my_main_ui()
    Win1.show()
	12
    app.exec_()