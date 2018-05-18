# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\CarCheck\ui\widgets\notification.ui'
#
# Created: Fri May 18 00:14:31 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Notification(object):
    def setupUi(self, Notification):
        Notification.setObjectName("Notification")
        Notification.resize(250, 297)
        Notification.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Notification.setWindowOpacity(0.9)
        self.verticalLayout = QtGui.QVBoxLayout(Notification)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lay_titlebar = QtGui.QVBoxLayout()
        self.lay_titlebar.setObjectName("lay_titlebar")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_logo = QtGui.QLabel(Notification)
        self.lbl_logo.setText("")
        self.lbl_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_logo.setObjectName("lbl_logo")
        self.horizontalLayout.addWidget(self.lbl_logo)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_topic = QtGui.QLabel(Notification)
        self.lbl_topic.setMargin(5)
        self.lbl_topic.setOpenExternalLinks(True)
        self.lbl_topic.setObjectName("lbl_topic")
        self.gridLayout.addWidget(self.lbl_topic, 0, 0, 1, 1)
        self.lbl_message = QtGui.QLabel(Notification)
        self.lbl_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_message.setMargin(5)
        self.lbl_message.setOpenExternalLinks(True)
        self.lbl_message.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lbl_message.setObjectName("lbl_message")
        self.gridLayout.addWidget(self.lbl_message, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.btn_close = QtGui.QPushButton(Notification)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QtCore.QSize(75, 0))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.horizontalLayout.setStretch(1, 100)
        self.horizontalLayout.setStretch(2, 40)
        self.lay_titlebar.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.lay_titlebar)

        self.retranslateUi(Notification)
        QtCore.QMetaObject.connectSlotsByName(Notification)

    def retranslateUi(self, Notification):
        self.lbl_topic.setText(QtGui.QApplication.translate("Notification", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_message.setText(QtGui.QApplication.translate("Notification", "<style  type=\"text/css\" >\n"
"</style>  \n"
"<table id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92da\" > \n"
"<thead>    <tr> \n"
"        <th class=\"blank level0\" ></th> \n"
"        <th class=\"col_heading level0 col0\" >5</th> \n"
"    </tr></thead> \n"
"<tbody>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row0\" class=\"row_heading level0 row0\" >Номер авто</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow0_col0\" class=\"data row0 col0\" >А009УР197</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row1\" class=\"row_heading level0 row1\" >Заказчик</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow1_col0\" class=\"data row1 col0\" >Симонян</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row2\" class=\"row_heading level0 row2\" >Дата по</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow2_col0\" class=\"data row2 col0\" >1970-01-03</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row3\" class=\"row_heading level0 row3\" >Дата от</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow3_col0\" class=\"data row3 col0\" >1970-01-01</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row4\" class=\"row_heading level0 row4\" >Описание</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow4_col0\" class=\"data row4 col0\" >None</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row5\" class=\"row_heading level0 row5\" >Эко класс</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow5_col0\" class=\"data row5 col0\" >None</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row6\" class=\"row_heading level0 row6\" >Скрыто</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow6_col0\" class=\"data row6 col0\" >False</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row7\" class=\"row_heading level0 row7\" >Владелец</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow7_col0\" class=\"data row7 col0\" >None</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row8\" class=\"row_heading level0 row8\" >Оплата</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow8_col0\" class=\"data row8 col0\" >nan</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row9\" class=\"row_heading level0 row9\" >Цена</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow9_col0\" class=\"data row9 col0\" >nan</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row10\" class=\"row_heading level0 row10\" >Заглушенно</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow10_col0\" class=\"data row10 col0\" >False</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row11\" class=\"row_heading level0 row11\" >Статус</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow11_col0\" class=\"data row11 col0\" >None</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row12\" class=\"row_heading level0 row12\" >Номер СТС</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow12_col0\" class=\"data row12 col0\" >77 ХС 842429</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row13\" class=\"row_heading level0 row13\" >Путь</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow13_col0\" class=\"data row13 col0\" >None</td> \n"
"    </tr>    <tr> \n"
"        <th id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92dalevel0_row14\" class=\"row_heading level0 row14\" >Зона</th> \n"
"        <td id=\"T_6d631314_5a1b_11e8_83fe_7824af8f92darow14_col0\" class=\"data row14 col0\" >СК</td> \n"
"    </tr></tbody> \n"
"</table> ", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_close.setText(QtGui.QApplication.translate("Notification", "Close", None, QtGui.QApplication.UnicodeUTF8))

