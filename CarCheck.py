# pd.set_option('display.width', pd.get_option('display.width')*3)
from PySide import QtCore, QtUiTools, QtGui



def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = loadUiWidget("gui/widgets/mainwindow.ui")
    MainWindow.show()
    sys.exit(app.exec_())