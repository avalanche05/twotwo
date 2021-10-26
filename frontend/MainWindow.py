# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.itemsTableView = QtWidgets.QTableView(self.centralwidget)
        self.itemsTableView.setGeometry(QtCore.QRect(20, 30, 491, 541))
        self.itemsTableView.setObjectName("itemsTableView")
        self.shopNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.shopNameLabel.setGeometry(QtCore.QRect(540, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.shopNameLabel.setFont(font)
        self.shopNameLabel.setObjectName("shopNameLabel")
        self.addItemButton = QtWidgets.QPushButton(self.centralwidget)
        self.addItemButton.setGeometry(QtCore.QRect(520, 540, 341, 31))
        self.addItemButton.setObjectName("addItemButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 500, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 471, 16))
        self.label.setObjectName("label")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shopNameLabel.setText(_translate("MainWindow", "Название магазина"))
        self.addItemButton.setText(_translate("MainWindow", "Добавить новый товар"))
        self.pushButton.setText(_translate("MainWindow", "Транзакция"))
        self.label.setText(_translate("MainWindow", "Товары в наличии:"))
