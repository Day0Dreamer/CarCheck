import ui.translation
import ui
import api.query_db
from PySide.QtCore import *
from PySide.QtGui import *
# todo проверку правописания при заполнении машины
from ui import translation

if __name__ == '__main__':
    app = ui.QApplication([])
    ui = ui.UIMainWindow()


    ui.show()
    app.exec_()
