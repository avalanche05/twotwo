# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/TransactionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransactionDialog(object):
    def setupUi(self, TransactionDialog):
        TransactionDialog.setObjectName("TransactionDialog")
        TransactionDialog.resize(498, 521)
        TransactionDialog.setStyleSheet("background-color: rgb(255, 224, 207);")
        self.label = QtWidgets.QLabel(TransactionDialog)
        self.label.setGeometry(QtCore.QRect(150, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(TransactionDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 110, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saleBool = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.saleBool.setObjectName("saleBool")
        self.horizontalLayout.addWidget(self.saleBool)
        self.entranceBool = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.entranceBool.setObjectName("entranceBool")
        self.horizontalLayout.addWidget(self.entranceBool)
        self.barcodeInput = QtWidgets.QLineEdit(TransactionDialog)
        self.barcodeInput.setGeometry(QtCore.QRect(150, 180, 113, 23))
        self.barcodeInput.setObjectName("barcodeInput")
        self.qrButton = QtWidgets.QPushButton(TransactionDialog)
        self.qrButton.setGeometry(QtCore.QRect(285, 170, 61, 41))
        self.qrButton.setObjectName("qrButton")
        self.spinBox = QtWidgets.QSpinBox(TransactionDialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 300, 181, 31))
        self.spinBox.setObjectName("spinBox")
        self.itemLabel = QtWidgets.QLabel(TransactionDialog)
        self.itemLabel.setGeometry(QtCore.QRect(150, 220, 211, 21))
        self.itemLabel.setObjectName("itemLabel")
        self.label_2 = QtWidgets.QLabel(TransactionDialog)
        self.label_2.setGeometry(QtCore.QRect(150, 280, 81, 16))
        self.label_2.setObjectName("label_2")
        self.doneButton = QtWidgets.QPushButton(TransactionDialog)
        self.doneButton.setGeometry(QtCore.QRect(210, 350, 80, 23))
        self.doneButton.setObjectName("doneButton")

        self.retranslateUi(TransactionDialog)
        QtCore.QMetaObject.connectSlotsByName(TransactionDialog)

    def retranslateUi(self, TransactionDialog):
        _translate = QtCore.QCoreApplication.translate
        TransactionDialog.setWindowTitle(_translate("TransactionDialog", "Транзакция"))
        self.label.setText(_translate("TransactionDialog", "Новая транзакция"))
        self.saleBool.setText(_translate("TransactionDialog", "Продажа"))
        self.entranceBool.setText(_translate("TransactionDialog", "Поступление"))
        self.qrButton.setText(_translate("TransactionDialog", ""))
        self.itemLabel.setText(_translate("TransactionDialog", "Товара с таким штрих-кодом нет"))
        self.label_2.setText(_translate("TransactionDialog", "Количество"))
        self.doneButton.setText(_translate("TransactionDialog", "Готово"))
