
from PyQt5 import QtCore, QtGui, QtWidgets
from stats101 import *
from graph101 import *
class Ui_MainWindow(object):
    def abc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 863)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 90, 551, 61))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 200, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 390, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.abc)#############################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        self.menuStart_Page = QtWidgets.QMenu(self.menubar)
        self.menuStart_Page.setObjectName("menuStart_Page")
        self.menuStats = QtWidgets.QMenu(self.menubar)
        self.menuStats.setObjectName("menuStats")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLine = QtWidgets.QAction(MainWindow)
        self.actionLine.setObjectName("actionLine")
        self.actionLength = QtWidgets.QAction(MainWindow)
        self.actionLength.setObjectName("actionLength")
        self.menuStats.addAction(self.actionLine)
        self.menuStats.addAction(self.actionLength)
        self.menubar.addAction(self.menuStart_Page.menuAction())
        self.menubar.addAction(self.menuStats.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cricket Bowling Analyser"))
        self.label_2.setText(_translate("MainWindow", "-By Team Ultraa"))
        self.pushButton.setText(_translate("MainWindow", "Start!"))
        self.menuStart_Page.setTitle(_translate("MainWindow", "Start Page"))
        self.menuStats.setTitle(_translate("MainWindow", "Stats"))
        self.actionLine.setText(_translate("MainWindow", "Line"))
        self.actionLength.setText(_translate("MainWindow", "Length"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
