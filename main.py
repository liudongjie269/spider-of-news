from PyQt5 import QtCore,QtGui,QtWidgets
import sys
from Models.agent import *
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    win1=a_main_ui()
    win1.show()
    app.exec_()
