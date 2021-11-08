import sys

from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog

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
        self.saveButton.clicked.connect(self.save_data)
        self.qrButton.clicked.connect(self.scan_qr)

    def save_data(self):
        name = self.nameInput.text()
        count = int(self.countInput.text())
        barcode = self.barCodeInput.text()
        owner_id = self.area.id
        price = float(self.priceInput.text().replace(',', '.'))
        item = Item(name, count, barcode, owner_id, price)
        add_item(item)
        self.close()

    def scan_qr(self):
        barcode_path = QFileDialog.getOpenFileName(self,
                                                   'Выберите картинку с нужным QR-кодом', '')[0]
        barcode = get_data(barcode_path)
        self.barCodeInput.setText(barcode)
#
#
# def except_hook(cls, exception, traceback):
#     sys.__excepthook__(cls, exception, traceback)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = AddItem()
#     ex.show()
#     sys.excepthook = except_hook
#     sys.exit(app.exec())
