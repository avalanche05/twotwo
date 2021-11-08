# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/SignUpDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(484, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color: rgb(255, 224, 207);")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 150, 141, 46))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.titleInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.titleInput.setObjectName("titleInput")
        self.verticalLayout.addWidget(self.titleInput)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 270, 141, 46))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.passwordInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.passwordInput.setObjectName("passwordInput")
        self.verticalLayout_2.addWidget(self.passwordInput)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(170, 210, 141, 46))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.loginInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.loginInput.setObjectName("loginInput")
        self.verticalLayout_3.addWidget(self.loginInput)
        self.signupButton = QtWidgets.QPushButton(Dialog)
        self.signupButton.setGeometry(QtCore.QRect(170, 320, 139, 23))
        self.signupButton.setObjectName("signupButton")
        self.visibleButton = QtWidgets.QPushButton(Dialog)
        self.visibleButton.setGeometry(QtCore.QRect(315, 295, 20, 20))
        self.visibleButton.setMinimumSize(QtCore.QSize(20, 20))
        self.visibleButton.setMaximumSize(QtCore.QSize(20, 20))
        self.visibleButton.setBaseSize(QtCore.QSize(20, 20))
        self.visibleButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.visibleButton.setText("")
        self.visibleButton.setObjectName("visibleButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Регистрация"))
        self.label_2.setText(_translate("Dialog", "Регистрация"))
        self.label_3.setText(_translate("Dialog", "Название магазина"))
        self.label_4.setText(_translate("Dialog", "Пароль"))
        self.label_5.setText(_translate("Dialog", "Логин"))
        self.signupButton.setText(_translate("Dialog", "Зарегистрироваться"))
