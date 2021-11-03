from PyQt5.QtWidgets import QMainWindow

from frontend.MainWindow import Ui_MainWindow
from core.SignIn import area


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.area = area
        self.shopNameLabel.setText(area.title)
