from ui.widgets.import_view_ui import Ui_import_view_ui
from PySide.QtGui import *
import api.import_excel
import api.query_db


class UIExportView(QWidget, Ui_import_view_ui):
    def __init__(self):
        super(UIExportView, self).__init__()
        self.setupUi(self)
        self.btn_browse.clicked.connect(self.save_excel)
        self.resize(1280, 658)

        self.btn_browse.setText('Export')

        self.db = api.query_db.DB()
        self.df = None

    def showEvent(self, event):
        super(UIExportView, self).showEvent(event)
        self.df = self.db.get_all(api.query_db.DataType.DATAFRAME)
        self.show_df(self.df.to_html())

    def save_excel(self):
        file, filtr = QFileDialog.getSaveFileName(self,
                                                  "Choose your files for conversion", '.',
                                                  "All Files (*.*);;Excel (*.xlsx)", "Excel (*.xlsx)")
        api.import_excel.df2excel(self.df, file)

    # def make_df(self):
    #     self.db.get_all(as_dict=)


    def show_df(self, df):
        self.textBrowser.setText(df)

if __name__ == '__main__':
    from PySide.QtGui import QApplication
    app = QApplication([])
    ui = UIExportView()
    ui.show()
    app.exec_()
