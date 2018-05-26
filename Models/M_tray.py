from PyQt5 import QtWidgets,QtGui,QtCore
class M_tray(QtWidgets.QSystemTrayIcon):
    def __init__(self,aa):
        super(M_tray, self).__init__(aa)
        self.setIcon(QtGui.QIcon("res/Tray.ico"))
        self.activated.connect(self.cc)
        self.showmenu()
        self.icon = self.MessageIcon()
    def showmenu(self):
        self.mainmenu=QtWidgets.QMenu()
        self.showAction = QtWidgets.QAction("显示消息1", self, triggered=self.showM)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.showM)
        self.mainmenu.addAction(self.showAction)
        self.mainmenu.addAction(self.quitAction)
        self.setContextMenu(self.mainmenu)
    def showM(self):
        self.showMessage("测试", "我是消息", self.icon)
    def cc(self,reason):
        print(reason)