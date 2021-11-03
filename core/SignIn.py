import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication

import Constant
from classes.Area import Area
from core.SignUp import SignUp
from frontend.SignInDialog import SignInDialog
from exceptions.PasswordException import *
from helpers.DatabaseHelper import get_area
from core.Main import Main

area = Area(Constant.NOT_STATED, Constant.NOT_STATED, Constant.NOT_STATED)


class SignIn(QDialog, SignInDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signInButton.clicked.connect(self.sign_in)
        self.signUpButton.clicked.connect(self.go_to_sign_up)
        self.sign_up_dialog = SignUp()
        self.main_window = Main()

    def go_to_sign_up(self):
        self.sign_up_dialog.setWindowModality(Qt.ApplicationModal)
        self.sign_up_dialog.show()

    def sign_in(self):
        global area
        login = self.loginInput.text()
        password = self.passwordInput.text()

        try:
            area = get_area(login, password)
            # Запускаем основное окно
            self.main_window.show()
            self.close()

        except LoginNotFoundException:
            print(Constant.LOGIN_NOT_FOUND_TEXT)
        except PasswordNotCorrect:
            print(Constant.PASSWORD_NOT_CORRECT_TEXT)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SignIn()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
