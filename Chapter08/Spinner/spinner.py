# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spinner.ui'
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
        Dialog.resize(357, 196)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(130, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 60, 62, 22))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.lineFirstValue = QtGui.QLineEdit(Dialog)
        self.lineFirstValue.setEnabled(False)
        self.lineFirstValue.setGeometry(QtCore.QRect(230, 20, 113, 20))
        self.lineFirstValue.setObjectName(_fromUtf8("lineFirstValue"))
        self.lineSecondValue = QtGui.QLineEdit(Dialog)
        self.lineSecondValue.setEnabled(False)
        self.lineSecondValue.setGeometry(QtCore.QRect(230, 60, 113, 20))
        self.lineSecondValue.setObjectName(_fromUtf8("lineSecondValue"))
        self.AddButton = QtGui.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.labelAddition = QtGui.QLabel(Dialog)
        self.labelAddition.setGeometry(QtCore.QRect(156, 100, 91, 20))
        self.labelAddition.setText(_fromUtf8(""))
        self.labelAddition.setObjectName(_fromUtf8("labelAddition"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Select First value", None))
        self.label_2.setText(_translate("Dialog", "Select Second value", None))
        self.AddButton.setText(_translate("Dialog", "Add", None))

