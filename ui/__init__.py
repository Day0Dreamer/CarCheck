from ui.MainWindow import UIMainWindow
from PySide.QtGui import *

if __name__ == '__main__':
    app = QApplication([])
    ui = UIMainWindow()
    ui.show()
    app.exec_()
