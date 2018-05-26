from PyQt5 import QtWidgets,QtGui,QtCore
class M_tray(QtWidgets.QSystemTrayIcon):
    def __init__(self,aa):
        super(M_tray, self).__init__(aa)
        self.setIcon(QtGui.QIcon("res/Tray.ico"))
        #托盘被点击icocliced
        self.activated.connect(self.icoclicked)
        self.icon = self.MessageIcon()
        self.showmenu()
    def showmenu(self):
        pw=self.parent()
        self.mainmenu=QtWidgets.QMenu()
        self.mainAction = QtWidgets.QAction("显示主界面", self, triggered=pw.show)
        self.settinAction = QtWidgets.QAction("设置", self, triggered=pw.aa.show)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=pw.show)
        self.mainmenu.addAction(self.mainAction)
        self.mainmenu.addAction(self.settinAction)
        self.mainmenu.addAction(self.quitAction)
        self.setContextMenu(self.mainmenu)
    def icoclicked(self,reason):
        pw=self.parent()
        if reason==2:
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
