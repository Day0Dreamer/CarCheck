# -*- coding: utf-8 -*-

# Form implementation generated from reading user_interface file 'C:\Python\CarCheck\user_interface\widgets\edit_item.user_interface'
#
# Created: Fri Mar 30 23:37:15 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class Ui_Edit_Item_ui(object):
    def setupUi(self, Edit_Item_ui):
        Edit_Item_ui.setObjectName("Edit_Item_ui")
        Edit_Item_ui.resize(255, 433)
        self.formLayout = QFormLayout(Edit_Item_ui)
        self.formLayout.setObjectName("formLayout")
        self.line_owner = QLineEdit(Edit_Item_ui)
        self.line_owner.setObjectName("line_owner")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_owner)
        self.line_client = QLineEdit(Edit_Item_ui)
        self.line_client.setObjectName("line_client")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_client)
        self.label_client = QLabel(Edit_Item_ui)
        self.label_client.setObjectName("label_client")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_client)
        self.label_owner = QLabel(Edit_Item_ui)
        self.label_owner.setObjectName("label_owner")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_owner)
        self.label_zone = QLabel(Edit_Item_ui)
        self.label_zone.setObjectName("label_zone")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_zone)
        self.label_status = QLabel(Edit_Item_ui)
        self.label_status.setObjectName("label_status")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_status)
        self.date_start = QDateEdit(Edit_Item_ui)
        self.date_start.setCalendarPopup(True)
        self.date_start.setObjectName("date_start")
        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.date_start)
        self.date_end = QDateEdit(Edit_Item_ui)
        self.date_end.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_end.setCalendarPopup(True)
        self.date_end.setObjectName("date_end")
        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.date_end)
        self.label_date_start = QLabel(Edit_Item_ui)
        self.label_date_start.setObjectName("label_date_start")
        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_date_start)
        self.label_date_end = QLabel(Edit_Item_ui)
        self.label_date_end.setObjectName("label_date_end")
        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_date_end)
        self.line_price = QLineEdit(Edit_Item_ui)
        self.line_price.setObjectName("line_price")
        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.line_price)
        self.line_payment = QLineEdit(Edit_Item_ui)
        self.line_payment.setObjectName("line_payment")
        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.line_payment)
        self.plain_description = QPlainTextEdit(Edit_Item_ui)
        self.plain_description.setObjectName("plain_description")
        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.plain_description)
        self.label_price = QLabel(Edit_Item_ui)
        self.label_price.setObjectName("label_price")
        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_price)
        self.label_payment = QLabel(Edit_Item_ui)
        self.label_payment.setObjectName("label_payment")
        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_payment)
        self.label_description = QLabel(Edit_Item_ui)
        self.label_description.setObjectName("label_description")
        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_description)
        self.buttonBox = QDialogButtonBox(Edit_Item_ui)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.buttonBox)
        self.check_hidden = QCheckBox(Edit_Item_ui)
        self.check_hidden.setObjectName("check_hidden")
        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.check_hidden)
        self.check_silenced = QCheckBox(Edit_Item_ui)
        self.check_silenced.setObjectName("check_silenced")
        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.check_silenced)
        self.line_sts = QLineEdit(Edit_Item_ui)
        self.line_sts.setObjectName("line_sts")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.line_sts)
        self.label_sts = QLabel(Edit_Item_ui)
        self.label_sts.setObjectName("label_sts")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_sts)
        self.label_eco = QLabel(Edit_Item_ui)
        self.label_eco.setObjectName("label_eco")
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_eco)
        self.box_zone = QComboBox(Edit_Item_ui)
        self.box_zone.setObjectName("box_zone")
        self.box_zone.addItem("")
        self.box_zone.addItem("")
        self.box_zone.addItem("")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.box_zone)
        self.box_status = QComboBox(Edit_Item_ui)
        self.box_status.setObjectName("box_status")
        self.box_status.addItem("")
        self.box_status.addItem("")
        self.box_status.addItem("")
        self.box_status.addItem("")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.box_status)
        self.box_eco = QComboBox(Edit_Item_ui)
        self.box_eco.setObjectName("box_eco")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.box_eco.addItem("")
        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.box_eco)
        self.line_car_number = QLineEdit(Edit_Item_ui)
        self.line_car_number.setObjectName("line_car_number")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_car_number)
        self.label_car_number = QLabel(Edit_Item_ui)
        self.label_car_number.setObjectName("label_car_number")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_car_number)

        self.retranslateUi(Edit_Item_ui)
        QObject.connect(self.buttonBox, SIGNAL("accepted()"), Edit_Item_ui.accept)
        QObject.connect(self.buttonBox, SIGNAL("rejected()"), Edit_Item_ui.reject)
        QMetaObject.connectSlotsByName(Edit_Item_ui)
        Edit_Item_ui.setTabOrder(self.line_client, self.line_owner)
        Edit_Item_ui.setTabOrder(self.line_owner, self.line_sts)
        Edit_Item_ui.setTabOrder(self.line_sts, self.line_price)
        Edit_Item_ui.setTabOrder(self.line_price, self.line_payment)
        Edit_Item_ui.setTabOrder(self.line_payment, self.date_start)
        Edit_Item_ui.setTabOrder(self.date_start, self.date_end)
        Edit_Item_ui.setTabOrder(self.date_end, self.check_hidden)
        Edit_Item_ui.setTabOrder(self.check_hidden, self.check_silenced)
        Edit_Item_ui.setTabOrder(self.check_silenced, self.buttonBox)
        Edit_Item_ui.setTabOrder(self.buttonBox, self.plain_description)

    def retranslateUi(self, Edit_Item_ui):
        Edit_Item_ui.setWindowTitle(QApplication.translate("Edit_Item_ui", "Dialog", None, QApplication.UnicodeUTF8))
        self.label_client.setText(QApplication.translate("Edit_Item_ui", "Заказчик", None, QApplication.UnicodeUTF8))
        self.label_owner.setText(QApplication.translate("Edit_Item_ui", "Владелец", None, QApplication.UnicodeUTF8))
        self.label_zone.setText(QApplication.translate("Edit_Item_ui", "Зона действия", None, QApplication.UnicodeUTF8))
        self.label_status.setText(QApplication.translate("Edit_Item_ui", "Статус", None, QApplication.UnicodeUTF8))
        self.date_start.setDisplayFormat(QApplication.translate("Edit_Item_ui", "dd/MM/yyyy", None, QApplication.UnicodeUTF8))
        self.date_end.setDisplayFormat(QApplication.translate("Edit_Item_ui", "dd/MM/yyyy", None, QApplication.UnicodeUTF8))
        self.label_date_start.setText(QApplication.translate("Edit_Item_ui", "Дата начала", None, QApplication.UnicodeUTF8))
        self.label_date_end.setText(QApplication.translate("Edit_Item_ui", "Дата конца", None, QApplication.UnicodeUTF8))
        self.label_price.setText(QApplication.translate("Edit_Item_ui", "Цена", None, QApplication.UnicodeUTF8))
        self.label_payment.setText(QApplication.translate("Edit_Item_ui", "Оплата", None, QApplication.UnicodeUTF8))
        self.label_description.setText(QApplication.translate("Edit_Item_ui", "Примечания", None, QApplication.UnicodeUTF8))
        self.check_hidden.setText(QApplication.translate("Edit_Item_ui", "Скрытый", None, QApplication.UnicodeUTF8))
        self.check_silenced.setText(QApplication.translate("Edit_Item_ui", "Напоминание", None, QApplication.UnicodeUTF8))
        self.label_sts.setText(QApplication.translate("Edit_Item_ui", "СТС", None, QApplication.UnicodeUTF8))
        self.label_eco.setText(QApplication.translate("Edit_Item_ui", "Эко-класс", None, QApplication.UnicodeUTF8))
        self.box_zone.setItemText(0, QApplication.translate("Edit_Item_ui", "СК", None, QApplication.UnicodeUTF8))
        self.box_zone.setItemText(1, QApplication.translate("Edit_Item_ui", "ТТК", None, QApplication.UnicodeUTF8))
        self.box_zone.setItemText(2, QApplication.translate("Edit_Item_ui", "МКАД", None, QApplication.UnicodeUTF8))
        self.box_status.setItemText(0, QApplication.translate("Edit_Item_ui", "Разовый", None, QApplication.UnicodeUTF8))
        self.box_status.setItemText(1, QApplication.translate("Edit_Item_ui", "Временный", None, QApplication.UnicodeUTF8))
        self.box_status.setItemText(2, QApplication.translate("Edit_Item_ui", "Полугодовой", None, QApplication.UnicodeUTF8))
        self.box_status.setItemText(3, QApplication.translate("Edit_Item_ui", "Годовой", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(0, QApplication.translate("Edit_Item_ui", "Нет данных", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(1, QApplication.translate("Edit_Item_ui", "Не установлен", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(2, QApplication.translate("Edit_Item_ui", "0", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(3, QApplication.translate("Edit_Item_ui", "1", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(4, QApplication.translate("Edit_Item_ui", "2", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(5, QApplication.translate("Edit_Item_ui", "3", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(6, QApplication.translate("Edit_Item_ui", "4", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(7, QApplication.translate("Edit_Item_ui", "5", None, QApplication.UnicodeUTF8))
        self.box_eco.setItemText(8, QApplication.translate("Edit_Item_ui", "6", None, QApplication.UnicodeUTF8))
        self.label_car_number.setText(QApplication.translate("Edit_Item_ui", "РегЗнак", None, QApplication.UnicodeUTF8))

