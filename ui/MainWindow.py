from datetime import date, datetime, timedelta
from pandas import IndexSlice
from PySide.QtCore import *
from PySide.QtGui import *

import api.query_db
from ui import stylesheet
from ui import translation
from ui.Edit_Item import UiEditItem
from ui.export_view import UIExportView
from ui.import_view import UIImportView
from ui.notification import UInotification
from ui.widgets.mainwindow_ui import Ui_MainWindow
from ui.widgets import title_bar


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


class _QTableWidget(QTableWidget):
    def __init__(self, parent):
        super(_QTableWidget, self).__init__(parent)
        self.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().customContextMenuRequested.connect(lambda pos: self.column_menu.exec_(self.horizontalHeader().mapToGlobal(pos)))
        self.column_menu = QMenu(self)

    def column_menu_fill(self, items):
        """

        Args:
            items (list):

        Returns:

        """
        if self.column_menu.isEmpty():
            [self.column_menu.addAction(QAction(item, self, triggered=lambda x=item:print(x))) for item in items]


    # def mousePressEvent(self, event):
    #     super(_QTableWidget, self).mousePressEvent(event)
        # print(event.pos())


class UIMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UIMainWindow, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(stylesheet.houdini)
        self.setWindowFlags(Qt.FramelessWindowHint)

        top_btn_row = self.verticalLayout.takeAt(0)
        search_line = self.verticalLayout.takeAt(0)
        unknown = self.verticalLayout.takeAt(0)
        record_mng = self.verticalLayout.takeAt(0)

        self._title = title_bar.TitleBar(self, '', 30)
        self.verticalLayout.addWidget(self._title)
        # self._title.title.setMenu(self.menuFile)
        self.menubar.hide()

        self._title.menu_bar.addMenu(self.menuFile)
        self._title.menu_bar.addMenu(self.menuDB)
        self._title.menu_bar.addMenu(self.menu_Settings)

        self.verticalLayout.addItem(top_btn_row)
        self.verticalLayout.addItem(search_line)

        self.verticalLayout.removeWidget(self.tbl_main)
        self.tbl_main.deleteLater()
        self.tbl_main = _QTableWidget(self.centralwidget)
        self.tbl_main.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_main.setAlternatingRowColors(True)
        self.tbl_main.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_main.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_main.setObjectName("tbl_main")
        self.tbl_main.setColumnCount(0)
        self.tbl_main.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_main)

        self.verticalLayout.addItem(record_mng)

        self.db = api.query_db.DB(db_path='sqlite:///db.sqlite')

        self.resize(1280+100, 720)

        self.add_item_dialogue = UiEditItem()
        self.add_item_dialogue.setStyleSheet(self.styleSheet())
        self.add_item_dialogue.buttonBox.buttons()[0].setText('Add')
        x = self.add_item_dialogue.buttonBox.addButton('Test', QDialogButtonBox.ApplyRole)
        x.clicked.connect(self.add_item_dialogue.read_fields)
        self.btn_add.clicked.connect(self.add_item_dialogue.exec_)

        self.preview_import = UIImportView()
        self.preview_import.setStyleSheet(self.styleSheet())
        self.action_Import.triggered.connect(self.preview_import.show)

        self.export_view = UIExportView()
        self.export_view.setStyleSheet(self.styleSheet())
        self.action_Export.triggered.connect(self.export_view.show)

        self.notification7 = UInotification(self)
        # self.notification7.show()

        self.shortcut_delete = QShortcut(QKeySequence(self.tr("Ctrl+Del")), self)
        self.shortcut_delete.setContext(Qt.WindowShortcut)
        self.shortcut_delete.activated.connect(self.delete_item)

        self.shortcut_import = QShortcut(QKeySequence(self.tr("Ctrl+i")), self)
        self.shortcut_import.setContext(Qt.WindowShortcut)
        self.shortcut_import.activated.connect(self.preview_import.show)

        self.shortcut_export = QShortcut(QKeySequence(self.tr("Ctrl+e")), self)
        self.shortcut_export.setContext(Qt.WindowShortcut)
        self.shortcut_export.activated.connect(self.export_view.show)

        self.btn_delete.pressed.connect(self.delete_item)
        self.edit_item_dialogue = UiEditItem()
        self.edit_item_dialogue.setStyleSheet(self.styleSheet())
        self.edit_item_dialogue.buttonBox.buttons()[0].setText('Edit')
        self.btn_edit.clicked.connect(self.edit_item_dialogue.exec_)
        # On [edit]
        @self.edit_item_dialogue.buttonBox.accepted.connect
        def change_car():
            self.db.change_car(self.edit_item_dialogue.read_fields())
            self.search()

        # Fill table with nothing
        self.btn_2.clicked.connect(lambda: self.fill_table([{}]))

        # Paint by date
        self.btn_4.clicked.connect(self.paint_by_date)

        self.name_interface()
        self.setup_table()
        # /////////////////

        # Update DB table readout
        self.btn_1.clicked.connect(self.update_table)
        self.btn_3.clicked.connect(self.notify)
        self.line_search.textChanged.connect(self.search)
        self.box_search_selector.currentIndexChanged.connect(self.search)

        self.tbl_main.itemActivated.connect(lambda: self.edit_item_dialogue.exec_())

        self.tbl_main.doubleClicked.connect(self.edit_item)
        self.btn_edit.clicked.connect(self.edit_item)

        # self.btn_edit.clicked.connect(lambda: self.edit_item_dialogue.exec_())
        self.btn_add.clicked.connect(self.add_item)

        self.update_table()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.notify)
        self.timer.start(60000)

    def notify(self, title='Алюрт', desc=''):
        df = self.db.get_all(api.query_db.DataType.DATAFRAME)
        print(df.columns)
        overdue = df[df['Silenced'] == False]
        # overdue = df[df['Пропуски_Silenced'] == True]

        overdue = overdue[overdue['Дата Конца'].dt.date.gt(date.fromtimestamp(100000))]  # With a date
        overdue = overdue[overdue['Дата Конца'].dt.date.le(date.today())]  # Less or equal of today
        overdue['Дата Конца'] = overdue['Дата Конца'].dt.floor('d')
        overdue = overdue.rename(columns=translation.permit_table)
        if len(overdue):
            # print(overdue.columns)
            # overdue = overdue.reindex(columns=['Заказчик', 'Номер авто', 'Дата по'])
            # overdue['Осталось дней'] = type(overdue['Дата по']-date.today())
            # print(overdue['Дата по'].dt)
            overdue.index += 1  # Shift index +1 so it matches with the table
            if len(overdue) > 1:
                not_title = ''
            else:
                not_title = ''
                overdue = overdue.transpose()
            # print(overdue.loc[:,'Зона'])

            not_desc = overdue.style.format({'Дата Подачи': "{:%Y.%m.%d}",
                                             'Дата Начала': "{:%Y.%m.%d}",
                                             'Дата Конца': "{:%Y.%m.%d}"}).render()
            self.notification7.set_data(not_title, not_desc)
            self.notification7.show()
            # self.notification7.setParent(None)

    # DB search functionality
    def search(self):
        key = next(key for key, value in translation.permit_table.items() if value == self.box_search_selector.currentText())
        self.fill_table(self.db.get_entry_as_dict(self.line_search.text(), key))

    def update_table(self):
        self.fill_table(self.db.get_all(api.query_db.DataType.DICT))

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

    def delete_item(self):
        self.shortcut_delete.setEnabled(False)
        if len(self.tbl_main.selectedIndexes()):  # If something is selected
            row_index = self.tbl_main.selectedIndexes()[0].row()

            highlight_row = translation.permit_table['car_number']
            for i in range(self.tbl_main.horizontalHeader().count()):
                row_name = self.tbl_main.model().headerData(i, Qt.Horizontal)
                if row_name == highlight_row:
                    highlight_row = i
                    break

            item = self.tbl_main.item(row_index, highlight_row)
            selected_car = item.text()

            self.db.delete_entry(selected_car, 'car_number')
            self.search()
            self.tbl_main.selectRow(row_index)
            print('Item {} Deleted'.format(selected_car))
        QTimer.singleShot(50, lambda : self.shortcut_delete.setEnabled(True))

    def add_item(self):
        print('adding item')
        self.db.add_new_car(self.add_item_dialogue.read_fields())
        self.search()


    def name_interface(self):
        self.btn_1.setText('Загрузить таблицу')
        self.btn_2.setText('Очистить таблицу')
        self.btn_3.setText('Оповестить')
        self.btn_4.setText('Раскрасить')
        self.btn_add.setText('Добавить запись')
        self.btn_edit.setText('Редактировать запись')
        self.btn_delete.setText('Удалить запись')

        self.add_item_dialogue.setWindowTitle('Добавление записи')
        self.edit_item_dialogue.setWindowTitle('Редактирование записи')

    def setup_table(self):
        self.tbl_main.setColumnCount(2)
        self.tbl_main.setRowCount(20)
        # QHeaderView
        self.tbl_main.horizontalHeader().setHighlightSections(True)
        print(self.tbl_main.horizontalHeader().highlightSections())

    def fill_table(self, data: list):
        """
        Fills the table with info from the Permits table

        Args:
            data(list): List of dicts of Permits table
        """
        self.tbl_main.setRowCount(0)
        self.tbl_main.setColumnCount(0)
        if len(data):
            list_of_rows = data
            col_list = list(data[0].keys())
            self.tbl_main.setRowCount(len(list_of_rows))
            self.tbl_main.setColumnCount(len(col_list))
            translated_horizontal_labels = [translation.permit_table[i] for i in col_list]
            self.tbl_main.setHorizontalHeaderLabels(translated_horizontal_labels)
            self.tbl_main.column_menu_fill(translated_horizontal_labels)
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
                # self.box_search_selector.addItems(col_list)
                self.box_search_selector.addItems(translated_horizontal_labels)
            # self.box_search_selector.clear()

            hide_list = ['Эко класс', 'Путь']
            for i, v in enumerate(translated_horizontal_labels):
                self.tbl_main.horizontalHeader().hideSection(i) if v in hide_list else 0
        else:
            self.tbl_main.setRowCount(0)
            self.tbl_main.setColumnCount(0)
            print('Empty SQL result')

        self.tbl_main.resizeColumnsToContents()

    def fill_table2(self, data):
        """
        Fills the table with info from the Permits table

        Args:
            data(DataFrame): List of dicts of Permits table
        """
        self.tbl_main.setRowCount(0)
        self.tbl_main.setColumnCount(0)
        if len(data):
            list_of_rows = data
            col_list = data.columns
            self.tbl_main.setRowCount(len(list_of_rows))
            self.tbl_main.setColumnCount(len(col_list))
            # translated_horizontal_labels = [translation.permit_table[i] for i in col_list]
            self.tbl_main.setHorizontalHeaderLabels(col_list)
            self.tbl_main.column_menu_fill(col_list)
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
                # self.box_search_selector.addItems(col_list)
                self.box_search_selector.addItems(translated_horizontal_labels)
            # self.box_search_selector.clear()

            hide_list = ['Эко класс', 'Путь']
            for i, v in enumerate(translated_horizontal_labels):
                self.tbl_main.horizontalHeader().hideSection(i) if v in hide_list else 0
        else:
            self.tbl_main.setRowCount(0)
            self.tbl_main.setColumnCount(0)
            print('Empty SQL result')

        self.tbl_main.resizeColumnsToContents()

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
            if date_date < date.fromtimestamp(100000):
                continue
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
