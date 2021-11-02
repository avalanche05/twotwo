from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class ClickedLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()
