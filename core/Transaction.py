import sys

import PIL
from PIL import UnidentifiedImageError
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog

import Constant
from classes.Area import Area
from frontend.Ui_TransactionDialog import Ui_TransactionDialog
from helpers.BarcodeHelper import get_data
from helpers.DatabaseHelper import update_item, get_item_name


class Transaction(QDialog, Ui_TransactionDialog):
    def __init__(self, area: Area):
        super().__init__()
        self.setupUi(self)
        self.area = area
        self.saleBool.setChecked(True)
        self.spinBox.setEnabled(False)
        self.qrButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "border: none;")
        self.qrButton.setIcon(QIcon('../data/qr_background.png'))
        self.qrButton.setFixedSize(40, 40)
        self.qrButton.setIconSize(QSize(40, 40))
        self.qrButton.clicked.connect(self.scan_qr)
        self.barCodeInput.textChanged.connect(self.barcode_changed)
        self.doneButton.clicked.connect(self.do_transaction)

    def barcode_changed(self):
        barcode = self.barCodeInput.text()
        name, count = get_item_name(barcode, self.area.id)
        if count == -1:
            self.spinBox.setRange(0, 0)
            self.spinBox.setDisabled(True)
        else:
            self.spinBox.setDisabled(False)
            self.spinBox.setRange(0, count)
        self.itemLabel.setText(name)

    def do_transaction(self):
        barcode = self.barCodeInput.text()
        count = int(self.spinBox.text())
        is_sale = self.saleBool.isChecked()
        update_item(barcode, self.area.id, (-1 if is_sale else 1) * count)
        self.close()

    def scan_qr(self):
        barcode_path = QFileDialog.getOpenFileName(self,
                                                   'Выберите картинку с нужным QR-кодом', '')[0]
        try:
            barcode = get_data(barcode_path)
            self.barCodeInput.setText(barcode)
        except PIL.UnidentifiedImageError:
            self.barCodeInput.setStyleSheet('border-radius: 2px;\n'
                                            'border-width: 1px;\n'
                                            'border-style: solid;\n'
                                            'border-color: rgb(255, 20, 3);')
            self.itemLabel.setText(Constant.FILE_NOT_CORRECT)
        except AttributeError:
            self.barCodeInput.setStyleSheet('border-radius: 2px;\n'
                                            'border-width: 1px;\n'
                                            'border-style: solid;\n'
                                            'border-color: rgb(255, 20, 3);')
            self.itemLabel.setText(Constant.NOT_FILE)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Transaction(Area(1, 'fefef', 'feefefe', 1))
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
