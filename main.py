from PyQt5 import QtCore,QtGui,QtWidgets
import sys
from Models.agent import *
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    win1=s_mian_ui()
    win1.show()
    app.exec_()
