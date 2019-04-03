import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt




class Ui_MainWindow(object):
    def abc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi1(self.window)
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

##Stats page##
class Ui_Dialog(object):
    def abd(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialoge()
        self.ui.setupUi2(self.window)
        Dialog.hide()
        self.window.show()
    def setupUi1(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1120, 857)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 90, 411, 101))
        font = QtGui.QFont()
        font.setFamily("Centaur")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 300, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 470, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.abd)#############################################################
        self.pushButton_2.clicked.connect(self.abd)#############################################################

        self.retranslateUi1(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi1(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Your Preference"))
        self.pushButton.setText(_translate("Dialog", "Line"))
        self.pushButton_2.setText(_translate("Dialog", "Length"))

        ##graph page##
class Ui_Dialoge(object):
    def abe(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi1(self.window)
        Dialoge.hide()
        self.window.show()
    def setupUi2(self, Dialoge):
        Dialoge.setObjectName("Dialoge")
        Dialoge.resize(1107, 846)
        Dialoge.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton = QtWidgets.QPushButton(Dialoge)
        self.pushButton.setGeometry(QtCore.QRect(490, 810, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.abe)#############################################################

        self.retranslateUi2(Dialoge)
        QtCore.QMetaObject.connectSlotsByName(Dialoge)

    def retranslateUi2(self, Dialoge):
        _translate = QtCore.QCoreApplication.translate
        Dialoge.setWindowTitle(_translate("Dialoge", "Dialoge"))
        self.pushButton.setText(_translate("Dialoge", "BACK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QMainWindow()
    Dialoge = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
