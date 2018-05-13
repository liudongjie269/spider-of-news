from Models.agent import *
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    Win1=s_mian_ui()
    Win1.show()
    app.exec_()