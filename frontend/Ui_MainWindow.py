# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ваши товары")
        MainWindow.resize(876, 622)
        MainWindow.setStyleSheet("background-color: rgb(255, 224, 207);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.addItemButton = QtWidgets.QPushButton(self.centralwidget)
        self.addItemButton.setObjectName("addItemButton")
        self.gridLayout.addWidget(self.addItemButton, 4, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.shopNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.shopNameLabel.setFont(font)
        self.shopNameLabel.setObjectName("shopNameLabel")
        self.gridLayout.addWidget(self.shopNameLabel, 0, 1, 1, 1)
        self.transactionButton = QtWidgets.QPushButton(self.centralwidget)
        self.transactionButton.setMinimumSize(QtCore.QSize(0, 32))
        self.transactionButton.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.transactionButton.setFont(font)
        self.transactionButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.transactionButton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ваши товары"))
        self.label.setText(_translate("MainWindow", "Товары в наличии:"))
        self.addItemButton.setText(_translate("MainWindow", "Добавить новый товар"))
        self.shopNameLabel.setText(_translate("MainWindow", "Название магазина"))
        self.transactionButton.setText(_translate("MainWindow", "Транзакция"))
