
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialoge(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1107, 846)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 810, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "BACK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialoge()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
