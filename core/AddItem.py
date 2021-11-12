import sys

from PIL import UnidentifiedImageError
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog

import Constant
from classes.Item import Item
from frontend.Ui_AddItemDialog import Ui_AddItemDialog
from helpers.BarcodeHelper import get_data
from helpers.DatabaseHelper import add_item
from classes.Area import Area


class AddItem(QDialog, Ui_AddItemDialog):
    def __init__(self, area: Area):
        super().__init__()
        self.setupUi(self)
        self.area = area
        self.countInput.setRange(0, 2147483647)
        self.priceInput.setRange(0, 2147483647)
        self.qrButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "border: none;")
        self.qrButton.setIcon(QIcon('../data/qr_background.png'))
        self.qrButton.setFixedSize(40, 40)
        self.qrButton.setIconSize(QSize(40, 40))
        self.saveButton.clicked.connect(self.save_data)
        self.qrButton.clicked.connect(self.scan_qr)

    def save_data(self):
        name = self.nameInput.text()
        # перекрашиваем lineEdit
        if not name:
            self.nameInput.setStyleSheet('border-radius: 2px;\n'
                                         'border-width: 1px;\n'
                                         'border-style: solid;\n'
                                         'border-color: rgb(255, 20, 3);')
            self.toast.setText(Constant.EMPTY_NAME)
            return
        else:
            self.nameInput.setStyleSheet('border-radius: 2px;\n'
                                         'border-width: 1px;\n'
                                         'border-style: solid;\n'
                                         'border-color: rgb(0, 0, 0, 80);')
            self.toast.setText('')
        count = int(self.countInput.text())
        barcode = self.barcodeInput.text()
        if not barcode:
            self.barcodeInput.setStyleSheet('border-radius: 2px;\n'
                                            'border-width: 1px;\n'
                                            'border-style: solid;\n'
                                            'border-color: rgb(255, 20, 3);')
            self.toast.setText(Constant.IMAGE_EMPTY)
            return
        else:
            self.nameInput.setStyleSheet('border-radius: 2px;\n'
                                         'border-width: 1px;\n'
                                         'border-style: solid;\n'
                                         'border-color: rgb(0, 0, 0, 80);')
            self.toast.setText('')
        owner_id = self.area.id
        price = float(self.priceInput.text().replace(',', '.'))
        item = Item(name, count, barcode, owner_id, price)
        add_item(item)
        self.close()

    def scan_qr(self):
        barcode_path = QFileDialog.getOpenFileName(self,
                                                   'Выберите картинку с нужным QR-кодом', '')[0]
        try:
            barcode = get_data(barcode_path)

            if barcode:
                self.barcodeInput.setText(barcode)
                self.barcodeInput.setStyleSheet('border-radius: 2px;\n'
                                                'border-width: 1px;\n'
                                                'border-style: solid;\n'
                                                'border-color: rgb(0, 0, 0, 80);')
                self.toast.setText('')
            else:
                self.barcodeInput.setStyleSheet('border-radius: 2px;\n'
                                                'border-width: 1px;\n'
                                                'border-style: solid;\n'
                                                'border-color: rgb(255, 20, 3);')
                self.toast.setText(Constant.IMAGE_EMPTY)
        except UnidentifiedImageError:
            self.barcodeInput.setStyleSheet('border-radius: 2px;\n'
                                            'border-width: 1px;\n'
                                            'border-style: solid;\n'
                                            'border-color: rgb(255, 20, 3);')
            self.toast.setText(Constant.FILE_NOT_CORRECT)
