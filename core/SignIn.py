import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication

import Constant
from core.SignUp import SignUp
from frontend.Ui_SignInDialog import Ui_SignInDialog
from exceptions.PasswordException import *
from helpers.DatabaseHelper import get_area
from core.Main import Main


class SignIn(QDialog, Ui_SignInDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signInButton.clicked.connect(self.sign_in)
        self.signUpButton.clicked.connect(self.open_sign_up)
        self.visibleButton.clicked.connect(self.change_visible)
        self.sign_up_dialog = SignUp()
        self.main_window = None
        self.is_password_visible = False
        self.set_password_policy()

    def change_visible(self):
        self.is_password_visible = not self.is_password_visible
        self.set_password_policy()

    def set_password_policy(self):
        if self.is_password_visible:
            self.visibleButton.setIcon(QIcon('../data/password_visible.png'))
            self.visibleButton.setIconSize(QSize(20, 20))
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.visibleButton.setIcon(QIcon('../data/password_not_visible.png'))
            self.visibleButton.setIconSize(QSize(20, 20))
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

    def open_sign_up(self):
        self.sign_up_dialog.setWindowModality(Qt.ApplicationModal)
        self.sign_up_dialog.show()

    def sign_in(self):
        login = self.loginInput.text()
        password = self.passwordInput.text()

        if not login:
            self.loginInput.setStyleSheet('border-radius: 2px;\n'
                                          'border-width: 1px;\n'
                                          'border-style: solid;\n'
                                          'border-color: rgb(255, 20, 3);')
            self.toast.setText(Constant.EMPTY_LOGIN)
        else:
            self.loginInput.setStyleSheet('border-radius: 2px;\n'
                                          'border-width: 1px;\n'
                                          'border-style: solid;\n'
                                          'border-color: rgb(0, 0, 0, 80);')
        if not password:
            self.passwordInput.setStyleSheet('border-radius: 2px;\n'
                                             'border-width: 1px;\n'
                                             'border-style: solid;\n'
                                             'border-color: rgb(255, 20, 3);')
            self.toast.setText(Constant.EMPTY_PASSWORD)
        else:
            self.passwordInput.setStyleSheet('border-radius: 2px;\n'
                                             'border-width: 1px;\n'
                                             'border-style: solid;\n'
                                             'border-color: rgb(0, 0, 0, 80);')
        if login and password:
            try:
                area = get_area(login, password)
                # Запускаем основное окно
                self.main_window = Main(area)
                self.main_window.show()
                self.close()

            except LoginNotFoundException:
                self.loginInput.setStyleSheet('border-radius: 2px;\n'
                                              'border-width: 1px;\n'
                                              'border-style: solid;\n'
                                              'border-color: rgb(255, 20, 3);')
                self.toast.setText(Constant.LOGIN_NOT_FOUND_TEXT)
            except PasswordNotCorrect:
                self.loginInput.setStyleSheet('border-radius: 2px;\n'
                                              'border-width: 1px;\n'
                                              'border-style: solid;\n'
                                              'border-color: rgb(0, 0, 0, 80);')

                self.passwordInput.setStyleSheet('border-radius: 2px;\n'
                                                 'border-width: 1px;\n'
                                                 'border-style: solid;\n'
                                                 'border-color: rgb(255, 20, 3);')
                self.toast.setText(Constant.PASSWORD_NOT_CORRECT_TEXT)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SignIn()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
