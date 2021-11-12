from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from frontend.Ui_SignUpDialog import Ui_Dialog
from helpers.DatabaseHelper import *


class SignUp(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signupButton.clicked.connect(self.sign_up)
        self.titleInput.setPlaceholderText(Constant.TITLE_HINT)
        self.loginInput.setPlaceholderText(Constant.LOGIN_HINT)
        self.passwordInput.setPlaceholderText(Constant.PASSWORD_HINT)
        self.is_password_visible = False
        self.set_password_policy()
        self.visibleButton.clicked.connect(self.change_visible)

    def sign_up(self):
        title = self.titleInput.text()
        login = self.loginInput.text()
        password = hash_password(self.passwordInput.text())

        is_error = False

        if not login:
            self.loginInput.setStyleSheet('border-radius: 2px;\n'
                                          'border-width: 1px;\n'
                                          'border-style: solid;\n'
                                          'border-color: rgb(255, 20, 3);')
            is_error = True
        else:
            self.loginInput.setStyleSheet('border-radius: 2px;\n'
                                          'border-width: 1px;\n'
                                          'border-style: solid;\n'
                                          'border-color: rgb(0, 0, 0, 80);')
        if not title:
            self.titleInput.setStyleSheet('border-radius: 2px;\n'
                                          'border-width: 1px;\n'
                                          'border-style: solid;\n'
                                          'border-color: rgb(255, 20, 3);')
            is_error = True
        else:
            self.titleInput.setStyleSheet('border-radius: 2px;\n'
                                          'border-width: 1px;\n'
                                          'border-style: solid;\n'
                                          'border-color: rgb(0, 0, 0, 80);')
        if not self.passwordInput.text():
            self.passwordInput.setStyleSheet('border-radius: 2px;\n'
                                             'border-width: 1px;\n'
                                             'border-style: solid;\n'
                                             'border-color: rgb(255, 20, 3);')
            is_error = True
        else:
            self.passwordInput.setStyleSheet('border-radius: 2px;\n'
                                             'border-width: 1px;\n'
                                             'border-style: solid;\n'
                                             'border-color: rgb(0, 0, 0, 80);')
        if is_error:
            return
        area = Area(title, login, password)
        add_area(area)
        self.close()

    def change_visible(self):
        self.is_password_visible = not self.is_password_visible
        self.set_password_policy()

    def set_password_policy(self):
        if not self.is_password_visible:
            self.visibleButton.setIcon(QIcon('../data/password_not_visible.png'))
            self.visibleButton.setIconSize(QSize(20, 20))
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.visibleButton.setIcon(QIcon('../data/password_visible.png'))
            self.visibleButton.setIconSize(QSize(20, 20))
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
