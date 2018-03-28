from ui.widgets.mainwindow_ui import Ui_MainWindow
from PySide.QtGui import QMainWindow


class UIMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UIMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    from PySide.QtGui import QApplication
    app = QApplication([])
    ui = UIMainWindow()
    ui.show()
    app.exec_()
