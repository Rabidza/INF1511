# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbx.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineAmount = QtGui.QLineEdit(Dialog)
        self.lineAmount.setEnabled(False)
        self.lineAmount.setGeometry(QtCore.QRect(120, 240, 113, 20))
        self.lineAmount.setObjectName(_fromUtf8("lineAmount"))
        self.checkPizza20 = QtGui.QCheckBox(Dialog)
        self.checkPizza20.setGeometry(QtCore.QRect(140, 50, 191, 17))
        self.checkPizza20.setObjectName(_fromUtf8("checkPizza20"))
        self.checkHotDog5 = QtGui.QCheckBox(Dialog)
        self.checkHotDog5.setGeometry(QtCore.QRect(140, 90, 171, 17))
        self.checkHotDog5.setObjectName(_fromUtf8("checkHotDog5"))
        self.checkFries10 = QtGui.QCheckBox(Dialog)
        self.checkFries10.setGeometry(QtCore.QRect(140, 130, 191, 17))
        self.checkFries10.setObjectName(_fromUtf8("checkFries10"))
        self.checkBurger15 = QtGui.QCheckBox(Dialog)
        self.checkBurger15.setGeometry(QtCore.QRect(140, 170, 171, 17))
        self.checkBurger15.setObjectName(_fromUtf8("checkBurger15"))
        self.CalculateButton = QtGui.QPushButton(Dialog)
        self.CalculateButton.setGeometry(QtCore.QRect(100, 200, 151, 23))
        self.CalculateButton.setObjectName(_fromUtf8("CalculateButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "XYZ Food Corner", None))
        self.label_2.setText(_translate("Dialog", "Total Amount", None))
        self.checkPizza20.setText(_translate("Dialog", "Pizza $20", None))
        self.checkHotDog5.setText(_translate("Dialog", "Hot Dog $5", None))
        self.checkFries10.setText(_translate("Dialog", "French Fries $10", None))
        self.checkBurger15.setText(_translate("Dialog", "Chicken Burger $15", None))
        self.CalculateButton.setText(_translate("Dialog", "Calculate Amount", None))

