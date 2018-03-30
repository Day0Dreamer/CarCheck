from ui.widgets.edit_item_ui import Ui_Edit_Item_ui
from PySide.QtGui import QDialog


class UiEditItem(QDialog, Ui_Edit_Item_ui):
    def __init__(self):
        super(UiEditItem, self).__init__()
        self.setupUi(self)

    def write_fields(self, item: dict):
        self.line_car_number.setText(item['РегЗнак'])
        self.line_client.setText(item['Clients'].name)
        self.line_owner.setText(item['Owners'].name)
        self.line_zone.setText(item['ЗонаДействия'])
        self.line_status.setText(item['PermitStatus'])
        self.date_start.setDate(item['ДатаНачала'])
        self.date_end.setDate(item['ДатаКонца'])
        self.line_price.setText(item['Цена'])
        self.line_payment.setText(item['Оплата'])
        self.plain_description.setPlainText(item['Примечания'])
        self.check_hidden.setCheckState(item['Hidden'])
        self.check_silenced.setChecked(item['Silenced'])

    def read_fields(self):
        result = dict()
        result['Clients']      = self.line_client.text() or None,
        result['Owners']       = self.line_owner.text() or None,
        result['РегЗнак']      = self.line_car_number.text() or None,
        result['СТС']          = self.line_sts.text() or None,
        result['ЗонаДействия'] = self.line_zone.text() or None,
        result['PermitStatus'] = self.line_status.text() or None,
        result['ДатаНачала']   = self.date_start.date().toPython() or None,
        result['ДатаКонца']    = self.date_end.date().toPython() or None,
        result['ЭкоКласс']     = self.line_eco.text() or None,
        result['Цена']         = self.line_price.text() or None,
        result['Оплата']       = self.line_payment.text() or None,
        result['Примечания']   = self.plain_description.toPlainText() or None,
        result['Путь']         = None,
        result['Silenced']     = self.check_silenced.isChecked(),
        result['Hidden']       = self.check_hidden.isChecked(),
        [print(i) for i in result.items()]
        return result


if __name__ == '__main__':
    from PySide.QtGui import QApplication
    app = QApplication([])
    ui = UiEditItem()
    ui.show()
    app.exec_()
