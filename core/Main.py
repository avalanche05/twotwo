from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView

import Constant
from classes.Area import Area
from core.AddItem import AddItem
from frontend.Ui_MainWindow import Ui_MainWindow
from helpers.DatabaseHelper import get_items


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, area: Area):
        super().__init__()
        self.setupUi(self)
        self.area = area
        self.update_result()
        self.shopNameLabel.setText(area.title)
        self.addItemButton.clicked.connect(self.open_add_item)
        self.add_item_dialog = None

    def open_add_item(self):
        self.add_item_dialog = AddItem(self.area)
        self.add_item_dialog.setWindowModality(Qt.ApplicationModal)
        self.add_item_dialog.show()
        self.update_result()

    def update_result(self):
        # Получили результат запроса, который ввели в текстовое поле
        items = get_items(self.area.id)
        # Заполнили размеры таблицы
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(items))
        # Если запись не нашлась, то не будем ничего делать
        if not items:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        parse_data = list(map(lambda item: [item.name, item.price, item.count, item.barcode],
                              items))
        self.tableWidget.setColumnCount(Constant.COLUMN_COUNT)
        self.tableWidget.setHorizontalHeaderLabels(Constant.FIELDS)
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(parse_data):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
