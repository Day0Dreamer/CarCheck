from ui.widgets.mainwindow_ui import Ui_MainWindow
from ui import stylesheet
from PySide.QtGui import *
from PySide.QtCore import *
from datetime import date, datetime

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
        # self.fill_table()

    def setup_table(self):
        self.tbl_main.setColumnCount(2)
        self.tbl_main.setRowCount(20)

    def fill_table(self, data: list):
        if len(data):
            list_of_rows = data
            col_list = list(data[0].keys())
            self.tbl_main.setRowCount(len(list_of_rows))
            self.tbl_main.setColumnCount(len(col_list))
            self.tbl_main.setHorizontalHeaderLabels(col_list)
            # For each row which is a dictionary, get row index and row's dictionary
            for row, row_dict in enumerate(list_of_rows):
                # For each column in a row, get column index and it's key
                for col, key in enumerate(row_dict.keys()):
                    value = row_dict[key]       # Get value assigned to the key
                    item = QTableWidgetItem()   # Create a new item
                    item.setText(str(value))    # Rename the item with the value
                    self.tbl_main.setItem(row, col, item)  # Add to the table indexRow and indexCol and the item

            if not self.box_search_selector.count():
                self.box_search_selector.addItems(col_list)
            # self.box_search_selector.clear()
        else:
            self.tbl_main.setRowCount(0)
            self.tbl_main.setColumnCount(0)
            print('Empty SQL result')

    def paint_by_date(self):
        for row_n in range(self.tbl_main.rowCount()):
            # QTableWidgetItem()
            str_date = self.tbl_main.item(row_n, 6).text()
            date_date = datetime.strptime(str_date, '%Y-%m-%d').date()
            date_delta = date_date - date.today()
            color_code = rgb(0,7,date_delta.days)
            # color_code = '#{:03x}'.format(max(0, int(translate(date_delta.days, 0, 30, 0xf, 0x0))))
            self.tbl_main.item(row_n, 6).setBackground(QBrush(QColor(*color_code)))
            self.tbl_main.item(row_n, 6).setToolTip(str(date_delta))

if __name__ == '__main__':
    app = QApplication([])
    ui = UIMainWindow()
    ui.show()
    app.exec_()
