

from PyQt5 import QtCore, QtGui, QtWidgets
from graph101 import *

class Ui_Dialog(object):
    def abd(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialoge()
        self.ui.setupUi(self.window)
        dialog.hide()
        self.window.show()
    def setupUi(self, Dialog):
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
        self.pushButton_2.clicked.connect(self.abd)###########################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Your Preference"))
        self.pushButton.setText(_translate("Dialog", "Line"))
        self.pushButton_2.setText(_translate("Dialog", "Length"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
