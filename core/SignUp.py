from PyQt5.QtWidgets import QDialog

from frontend.SignUpDialog import SignUpDialog
from helpers.DatabaseHelper import *


class SignUp(QDialog, SignUpDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signupButton.clicked.connect(self.sign_up)

    def sign_up(self):
        title = self.titleInput.text()
        login = self.loginInput.text()
        password = hash_password(self.passwordInput.text())

        area = Area(title, login, password)
        add_area_in_db(area)
