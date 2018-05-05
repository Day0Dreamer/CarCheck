from ui.widgets.edit_item_ui import Ui_Edit_Item_ui
from PySide.QtGui import *
from PySide.QtCore import *


class UiEditItem(QDialog, Ui_Edit_Item_ui):
    def __init__(self):
        super(UiEditItem, self).__init__()
        self.setupUi(self)

        self.line_car_number.setValidator(QRegExpValidator(QRegExp('\D\d{3}\D{2}\d{3}'), self))
        '''\D matches any character that\'s not a digit (equal to [^0-9])
        \d{3} matches a digit (equal to [0-9])
        \D{2} matches any character that\'s not a digit (equal to [^0-9])
        \d{3} matches a digit (equal to [0-9])'''
        self.line_sts.setValidator(QRegExpValidator(QRegExp('\d{2} \d{2} \d{6}'), self))
        '''\d{2} matches a digit (equal to [0-9]) matches the character   literally (case sensitive)
        \d{2} matches a digit (equal to [0-9])
        №  matches the characters  №  literally (case sensitive)
        \d{6} matches a digit (equal to [0-9])'''

    def write_fields(self, item: dict):
        self.line_client.setText(item['client'].name)
        self.line_owner.setText(item['owner'].name)
        self.line_car_number.setText(item['car_number'])
        self.line_sts.setText(item['sts_number'])
        self.box_zone.setCurrentIndex(self.box_zone.findText(item['zone']) if (item['zone']) else -1)
        self.box_status.setCurrentIndex(self.box_status.findText(item['status'].name) if item['status'] else -1)
        self.box_eco.setCurrentIndex(self.box_eco.findText(item['eco_class']))
        self.date_start.setDate(item['date_start'])
        self.date_end.setDate(item['date_end'])
        self.line_price.setText(str(item['price']) if item['price'] else '')
        self.line_payment.setText(str(item['payment']) if item['payment'] else '')
        self.plain_description.setPlainText(item['description'])
        self.check_hidden.setChecked(item['hidden'])
        self.check_silenced.setChecked(item['silenced'])

    def read_fields(self):
        print(self.line_price.text())
        result = dict(
            client=self.line_client.text() or None,
            owner=self.line_owner.text() or None,
            car_number=self.line_car_number.text() or None,
            sts_number=self.line_sts.text() or None,
            zone=self.box_zone.currentText() or None,
            status=self.box_status.currentText() or None,
            eco_class=self.box_eco.currentText() or None,
            date_start=self.date_start.date().toPython() or None,
            date_end=self.date_end.date().toPython() or None,
            price=float(self.line_price.text()) if self.line_price.text() else None,
            payment=float(self.line_payment.text()) if self.line_payment.text() else None,
            description=self.plain_description.toPlainText() or None,
            tba_1=None,
            hidden=self.check_hidden.isChecked(),
            silenced=self.check_silenced.isChecked())
        # print(result)
        return result



if __name__ == '__main__':
    from PySide.QtGui import QApplication
    app = QApplication([])
    ui = UiEditItem()
    ui.show()
    app.exec_()
