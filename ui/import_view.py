from ui.widgets.import_view_ui import Ui_import_view_ui
from PySide.QtGui import *
import api.import_excel


class UIImportView(QWidget, Ui_import_view_ui):
    def __init__(self):
        super(UIImportView, self).__init__()
        self.setupUi(self)
        self.btn_browse.clicked.connect(self.load_excel)
        self.resize(1280, 658)
        self.btn_import.clicked.connect(self.import_from_df)
        self.df = None

    def load_excel(self):
        file, filtr = QFileDialog.getOpenFileName(self,
                                                  "Choose your files for conversion", '.',
                                                  "All Files (*.*);;Excel (*.xlsx)", "Excel (*.xlsx)")
        self.df = api.import_excel.excel2df(file)
        self.show_df(self.df.to_html())

    def show_df(self, df):
        self.textBrowser.setText(df)

    def import_from_df(self):
        api.import_excel.import_from_df(self.df)

if __name__ == '__main__':
    from PySide.QtGui import QApplication
    app = QApplication([])
    ui = UIImportView()
    ui.show()
    app.exec_()
