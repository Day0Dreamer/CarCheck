# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\CarCheck\ui\widgets\mainwindow.ui'
#
# Created: Thu Mar 29 18:09:23 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 528)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_1 = QtGui.QPushButton(self.centralwidget)
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout.addWidget(self.btn_1)
        self.btn_2 = QtGui.QPushButton(self.centralwidget)
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout.addWidget(self.btn_2)
        self.btn_3 = QtGui.QPushButton(self.centralwidget)
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout.addWidget(self.btn_3)
        self.btn_4 = QtGui.QPushButton(self.centralwidget)
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout.addWidget(self.btn_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_search = QtGui.QLineEdit(self.centralwidget)
        self.line_search.setObjectName("line_search")
        self.horizontalLayout_3.addWidget(self.line_search)
        self.box_search_selector = QtGui.QComboBox(self.centralwidget)
        self.box_search_selector.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.box_search_selector.setObjectName("box_search_selector")
        self.horizontalLayout_3.addWidget(self.box_search_selector)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tbl_main = QtGui.QTableWidget(self.centralwidget)
        self.tbl_main.setObjectName("tbl_main")
        self.tbl_main.setColumnCount(0)
        self.tbl_main.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_main)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_add = QtGui.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_2.addWidget(self.btn_add)
        self.btn_edit = QtGui.QPushButton(self.centralwidget)
        self.btn_edit.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout_2.addWidget(self.btn_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_1.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_2.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_3.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_4.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))

