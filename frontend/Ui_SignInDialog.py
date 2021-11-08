# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/SignInDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from labels import ClickedLabel


class Ui_SignInDialog(object):
    def setupUi(self, SignInDialog):
        SignInDialog.setObjectName("SignInDialog")
        SignInDialog.resize(484, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignInDialog.sizePolicy().hasHeightForWidth())
        SignInDialog.setSizePolicy(sizePolicy)
        SignInDialog.setStyleSheet("background-color: rgb(255, 224, 207);")
        self.label_2 = QtWidgets.QLabel(SignInDialog)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(SignInDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 200, 141, 46))
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(SignInDialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(170, 140, 141, 46))
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
        self.signInButton = QtWidgets.QPushButton(SignInDialog)
        self.signInButton.setGeometry(QtCore.QRect(200, 290, 91, 21))
        self.signInButton.setObjectName("signupButton")
        self.toast = QtWidgets.QLabel(SignInDialog)
        self.toast.setGeometry(QtCore.QRect(120, 320, 251, 30))
        self.label = QtWidgets.QLabel(SignInDialog)
        self.label.setGeometry(QtCore.QRect(190, 250, 121, 16))
        self.label.setObjectName("label")
        self.signUpButton = ClickedLabel.ClickedLabel(SignInDialog)
        self.signUpButton.setGeometry(QtCore.QRect(180, 270, 141, 16))
        self.signUpButton.setStyleSheet("color: rgb(6, 64, 255);")
        self.signUpButton.setObjectName("signUpButton")
        self.visibleButton = QtWidgets.QPushButton(SignInDialog)
        self.visibleButton.setGeometry(QtCore.QRect(320, 225, 20, 20))
        self.visibleButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "border: none;")
        self.visibleButton.setText("")
        self.visibleButton.setObjectName("visibleButton")

        self.retranslateUi(SignInDialog)
        QtCore.QMetaObject.connectSlotsByName(SignInDialog)

    def retranslateUi(self, SignInDialog):
        _translate = QtCore.QCoreApplication.translate
        SignInDialog.setWindowTitle(_translate("SignInDialog", "Вход"))
        self.label_2.setText(_translate("SignInDialog", "Вход"))
        self.label_4.setText(_translate("SignInDialog", "Пароль"))
        self.label_5.setText(_translate("SignInDialog", "Логин"))
        self.signInButton.setText(_translate("SignInDialog", "Войти"))
        self.label.setText(_translate("SignInDialog", "Ещё нет аккаунта?"))
        self.signUpButton.setText(_translate("SignInDialog", "Зарегистрироваться."))
