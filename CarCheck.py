import ui.MainWindow
# todo проверку правописания при заполнении машины

if __name__ == '__main__':
    app = ui.MainWindow.QApplication([])
    ui = ui.MainWindow.UIMainWindow()


    ui.show()
    # QTimer.singleShot(1, app.quit)
    app.exec_()
