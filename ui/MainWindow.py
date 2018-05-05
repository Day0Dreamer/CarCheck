from ui.widgets.mainwindow_ui import Ui_MainWindow
from ui.Edit_Item import UiEditItem
from ui import translation
from ui import stylesheet
from PySide.QtGui import *
from PySide.QtCore import *
from datetime import date, datetime
import api.query_db


def translate(value, left_min, left_max, right_min, right_max):
    # Figure out how 'wide' each range is
    leftSpan = left_max - left_min
    rightSpan = right_max - right_min

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - left_min) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return right_min + (valueScaled * rightSpan)


def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(min(int(max(0, 255*(1 - ratio))), 255))
    r = int(min(int(max(0, 255*(ratio - 1))), 255))
    g = int(min(int(max(0, (255 - b - r))), 255))
    return b, g, r


class UIMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UIMainWindow, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(stylesheet.houdini)
        self.db = api.query_db.DB()

        self.add_item_dialogue = UiEditItem()
        self.add_item_dialogue.setStyleSheet(self.styleSheet())
        self.add_item_dialogue.buttonBox.buttons()[0].setText('Add')
        x = self.add_item_dialogue.buttonBox.addButton('Test', QDialogButtonBox.ApplyRole)
        x.clicked.connect(self.add_item_dialogue.read_fields)
        self.btn_add.clicked.connect(self.add_item_dialogue.exec_)

        self.edit_item_dialogue = UiEditItem()
        self.edit_item_dialogue.setStyleSheet(self.styleSheet())
        self.edit_item_dialogue.buttonBox.buttons()[0].setText('Edit')
        self.btn_edit.clicked.connect(self.edit_item_dialogue.exec_)
        # On [edit]
        @self.edit_item_dialogue.buttonBox.accepted.connect
        def change_car():
            self.db.change_car(self.edit_item_dialogue.read_fields())

        # Fill table with nothing
        self.btn_2.clicked.connect(lambda: self.fill_table([{}]))

        # Paint by date
        self.btn_4.clicked.connect(self.paint_by_date)

        self.name_interface()
        # /////////////////
        li = self.db.get_all()
        self.fill_table(li)

        # Update DB table readout
        self.btn_1.clicked.connect(lambda: self.fill_table(li))
        # DB search functionality
        search = lambda: self.fill_table(self.db.get_entry_as_dict(self.line_search.text(),
                                                                   self.box_search_selector.currentText()))
        self.btn_3.clicked.connect(search)
        self.line_search.textChanged.connect(search)
        self.box_search_selector.currentIndexChanged.connect(search)

        self.tbl_main.itemActivated.connect(lambda: self.edit_item_dialogue.exec_())

        self.tbl_main.doubleClicked.connect(self.edit_item)
        self.btn_edit.clicked.connect(self.edit_item)

        # self.btn_edit.clicked.connect(lambda: self.edit_item_dialogue.exec_())
        self.btn_add.clicked.connect(self.add_item)

    def edit_item(self):
        row_index = self.tbl_main.selectedIndexes()[0].row()

        highlight_row = translation.permit_table['car_number']
        for i in range(self.tbl_main.horizontalHeader().count()):
            row_name = self.tbl_main.model().headerData(i, Qt.Horizontal)
            if row_name == highlight_row:
                highlight_row = i
                break

        item = self.tbl_main.item(row_index, highlight_row)
        selected_car = item.text()

        entry = self.db.get_entry_as_dict(selected_car, 'car_number')[0]
        # print(entry['status'])
        self.edit_item_dialogue.write_fields(entry)
        # print(entry)


    def add_item(self):
        print('adding item')
        self.db.add_new_car(**self.add_item_dialogue.read_fields())


    def name_interface(self):
        self.btn_1.setText('Загрузить таблицу')
        self.btn_2.setText('Очистить таблицу')
        self.btn_3.setText('Повторить поиск')
        self.btn_4.setText('Раскрасить')

        self.add_item_dialogue.setWindowTitle('Добавление записи')
        self.edit_item_dialogue.setWindowTitle('Редактирование записи')

    def setup_table(self):
        self.tbl_main.setColumnCount(2)
        self.tbl_main.setRowCount(20)

    def fill_table(self, data: list):
        if len(data):
            list_of_rows = data
            col_list = list(data[0].keys())
            self.tbl_main.setRowCount(len(list_of_rows))
            self.tbl_main.setColumnCount(len(col_list))
            translated_horizontal_labels = [translation.permit_table[i] for i in col_list]
            self.tbl_main.setHorizontalHeaderLabels(translated_horizontal_labels)
            # For each row which is a dictionary, get row index and row's dictionary
            for row, row_dict in enumerate(list_of_rows):
                # For each column in a row, get column index and it's key
                for col, key in enumerate(row_dict.keys()):
                    value = row_dict[key]       # Get value assigned to the key
                    item = QTableWidgetItem()   # Create a new item
                    value = str(value).replace('None', '') if value else ''  # Replace None data with empty string
                    item.setText(value)    # Rename the item with the value
                    self.tbl_main.setItem(row, col, item)  # Add to the table indexRow and indexCol and the item

            if not self.box_search_selector.count():
                self.box_search_selector.addItems(col_list)
            # self.box_search_selector.clear()
        else:
            self.tbl_main.setRowCount(0)
            self.tbl_main.setColumnCount(0)
            print('Empty SQL result')

    def paint_by_date(self):
        highlight_row = 'Дата по'
        for i in range(self.tbl_main.horizontalHeader().count()):
            row_name = self.tbl_main.model().headerData(i, Qt.Horizontal)
            if row_name == highlight_row:
                highlight_row = i
                break
        for row_n in range(self.tbl_main.rowCount()):
            str_date = self.tbl_main.item(row_n, highlight_row).text()
            date_date = datetime.strptime(str_date, '%Y-%m-%d').date()
            date_delta = date_date - date.today()
            color_code = rgb(0,7,date_delta.days)
            # color_code = '#{:03x}'.format(max(0, int(translate(date_delta.days, 0, 30, 0xf, 0x0))))
            self.tbl_main.item(row_n, highlight_row).setBackground(QBrush(QColor(*color_code)))
            self.tbl_main.item(row_n, highlight_row).setToolTip(str(date_delta))


if __name__ == '__main__':
    app = QApplication([])
    ui = UIMainWindow()
    ui.show()
    app.exec_()
