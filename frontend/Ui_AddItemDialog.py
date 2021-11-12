# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/AddItemDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddItemDialog(object):
    def setupUi(self, AddItemDialog):
        AddItemDialog.setObjectName("AddItemDialog")
        AddItemDialog.resize(480, 483)
        AddItemDialog.setStyleSheet("background-color: rgb(255, 224, 207);")
        self.label = QtWidgets.QLabel(AddItemDialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameInput = QtWidgets.QLineEdit(AddItemDialog)
        self.nameInput.setGeometry(QtCore.QRect(170, 110, 121, 23))
        self.nameInput.setObjectName("titleInput")
        self.label_2 = QtWidgets.QLabel(AddItemDialog)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddItemDialog)
        self.label_3.setGeometry(QtCore.QRect(190, 330, 71, 16))
        self.label_3.setObjectName("label_3")
        self.barcodeInput = QtWidgets.QLineEdit(AddItemDialog)
        self.barcodeInput.setGeometry(QtCore.QRect(170, 350, 121, 23))
        self.barcodeInput.setText("")
        self.barcodeInput.setObjectName("barCodeInput")
        self.saveButton = QtWidgets.QPushButton(AddItemDialog)
        self.saveButton.setGeometry(QtCore.QRect(190, 400, 80, 23))
        self.saveButton.setObjectName("saveButton")
        self.label_4 = QtWidgets.QLabel(AddItemDialog)
        self.label_4.setGeometry(QtCore.QRect(180, 260, 111, 21))
        self.label_4.setObjectName("label_4")
        self.qrButton = QtWidgets.QPushButton(AddItemDialog)
        self.qrButton.setGeometry(QtCore.QRect(190, 290, 81, 31))
        self.qrButton.setObjectName("qrButton")
        self.label_5 = QtWidgets.QLabel(AddItemDialog)
        self.label_5.setGeometry(QtCore.QRect(210, 140, 57, 15))
        self.label_5.setObjectName("label_5")
        self.priceInput = QtWidgets.QDoubleSpinBox(AddItemDialog)
        self.priceInput.setGeometry(QtCore.QRect(170, 160, 121, 31))
        self.priceInput.setObjectName("priceInput")
        self.label_6 = QtWidgets.QLabel(AddItemDialog)
        self.label_6.setGeometry(QtCore.QRect(190, 210, 81, 16))
        self.label_6.setObjectName("label_6")
        self.countInput = QtWidgets.QSpinBox(AddItemDialog)
        self.countInput.setGeometry(QtCore.QRect(170, 230, 121, 24))
        self.countInput.setObjectName("countInput")
        self.toast = QtWidgets.QLabel(AddItemDialog)
        self.toast.setGeometry(QtCore.QRect(60, 430, 351, 20))
        self.toast.setText("")
        self.toast.setObjectName("toast")

        self.retranslateUi(AddItemDialog)
        QtCore.QMetaObject.connectSlotsByName(AddItemDialog)

    def retranslateUi(self, AddItemDialog):
        _translate = QtCore.QCoreApplication.translate
        AddItemDialog.setWindowTitle(_translate("AddItemDialog", "Добавление товара"))
        self.label.setText(_translate("AddItemDialog", "Данные о новом товаре."))
        self.label_2.setText(_translate("AddItemDialog", "Название"))
        self.label_3.setText(_translate("AddItemDialog", "Штрих-код"))
        self.saveButton.setText(_translate("AddItemDialog", "Сохранить."))
        self.label_4.setText(_translate("AddItemDialog", "Считать QR-код"))
        self.qrButton.setText(_translate("AddItemDialog", ""))
        self.label_5.setText(_translate("AddItemDialog", "Цена"))
        self.label_6.setText(_translate("AddItemDialog", "Количество"))
