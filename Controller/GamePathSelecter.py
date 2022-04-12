from PyQt5 import QtCore, QtGui, QtWidgets
from View.QTUI_GamePathSelect import QTUI_GamePathSelect


#显示QTUI_GamePathSelect.py的窗口
class GamePathSelecter(QtWidgets.QMainWindow, QTUI_GamePathSelect):
    def __init__(self):
        super(GamePathSelecter, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_path_select_window)
        self.pushButton.setText("选择游戏路径")
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setFont(QtGui.QFont("Microsoft YaHei", 10, QtGui.QFont.Bold))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(0.5 * (screenWidth - mainWindowWidth), 0.5 * (screenHeight - mainWindowHeight), mainWindowWidth, mainWindowHeight))

    def show_path_select_window(self):
        self.path_select_window = QTUI_GamePathSelect()
        self.path_select_window.show()