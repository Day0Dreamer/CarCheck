# pd.set_option('display.width', pd.get_option('display.width')*3)

import ui
import api.query_db
# todo проверку правописания при заполнении машины

if __name__ == '__main__':
    app = ui.QApplication([])
    ui = ui.UIMainWindow()

    db = api.query_db.DB('sqlite:///C:\\Python\\CarCheck\\db.sqlite')
    li = db.get_all()
    ui.fill_table(li)

    # Update DB table readout
    ui.btn_1.clicked.connect(lambda: ui.fill_table(li))
    # DB search functionality
    search = lambda: ui.fill_table(db.find_entry(ui.line_search.text(), ui.box_search_selector.currentText()))
    ui.btn_3.clicked.connect(search)
    ui.line_search.textChanged.connect(search)
    ui.box_search_selector.currentIndexChanged.connect(search)

    ui.tbl_main.itemActivated.connect(lambda: ui.edit_item_dialogue.exec_())
    def edit_item():
        row_index = ui.tbl_main.selectedIndexes()[0].row()
        item = ui.tbl_main.item(row_index, 2)
        selected_car = item.text()
        entry = db.find_entry(selected_car, 'РегЗнак')[0]
        ui.edit_item_dialogue.write_fields(entry)
        print(entry)
    ui.tbl_main.doubleClicked.connect(edit_item)
    ui.btn_edit.clicked.connect(edit_item)
    # ui.btn_edit.clicked.connect(lambda: ui.edit_item_dialogue.exec_())

    def add_item():
        print('adding item')
        ui.edit_item_dialogue.buttonBox.accepted.connect(lambda: db.add_new_car(
            ui.edit_item_dialogue.line_client.text() or None,
            ui.edit_item_dialogue.line_owner.text() or None,
            ui.edit_item_dialogue.line_car_number.text() or None,
            ui.edit_item_dialogue.line_sts.text() or None,
            ui.edit_item_dialogue.line_zone.text() or None,
            ui.edit_item_dialogue.line_status.text() or None,
            ui.edit_item_dialogue.date_start.date().toPython() or None,
            ui.edit_item_dialogue.date_end.date().toPython() or None,
            ui.edit_item_dialogue.line_eco.text() or None,
            ui.edit_item_dialogue.line_price.text() or None,
            ui.edit_item_dialogue.line_payment.text() or None,
            ui.edit_item_dialogue.plain_description.toPlainText() or None,
            None,
            ui.edit_item_dialogue.check_silenced.isChecked() or None,
            ui.edit_item_dialogue.check_hidden.isChecked() or None,
        ))
        # ui.edit_item_dialogue.exec_()
        # from PySide import QtGui
        # QtGui.QPushButton.
    ui.btn_add.clicked.connect(add_item)
    # QtGui.QTableWidgetItem.te
    # QtCore.QModelIndex.
    # ui.tbl_main.itemEntered.connect(lambda: print('6'))

    ui.show()
    app.exec_()
