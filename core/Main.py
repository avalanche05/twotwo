from PyQt5.QtWidgets import QMainWindow

import Global
from frontend.MainWindow import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.area = Global.area
        self.shopNameLabel.setText('oofuhih')
