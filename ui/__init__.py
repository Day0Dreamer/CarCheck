from ui.widgets.MainWindow import UIMainWindow
from PySide.QtGui import *
from PySide.QtCore import *

if __name__ == '__main__':
    app = QApplication([])
    ui = UIMainWindow()
    ui.show()
    app.exec_()
