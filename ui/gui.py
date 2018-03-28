from ui.widgets.MainWindow import UIMainWindow


if __name__ == '__main__':
    from PySide.QtGui import QApplication
    app = QApplication([])
    ui = UIMainWindow()
    ui.show()
    app.exec_()
