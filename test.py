from PyQt5 import QtWidgets,QtCore,QtGui
from Models import *
from Libs import *
import os
class mymain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(mymain, self).__init__()
        addButton = QtWidgets.QPushButton(u"添加控件",self)
        addButton.setGeometry(QtCore.QRect(10, 0, 91, 41))
        addButton.clicked.connect(self.add)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(19, 79, 400, 400))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-2, 0, 600, 700))
        # self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(600, 700))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def add(self):
        btncont = self.gridLayout.count()
        widget = QtWidgets.QPushButton(str(btncont))
        self.gridLayout.addWidget(widget)


if __name__ == '__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    win1=mymain()
    win1.show()
    app.exec()




