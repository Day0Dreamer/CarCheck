from ui.widgets import notification_ui
from ui.widgets import title_bar
from ui import stylesheet
from PySide.QtGui import *
from PySide.QtCore import *


class UInotification(QWidget, notification_ui.Ui_Notification):
    def __init__(self, parent=None):
        super(UInotification, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet.houdini)
        # self.setStyleSheet('border: 1px solid red')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Window)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.screen = QDesktopWidget.availableGeometry(QDesktopWidget())
        self.screen.setSize(QSize(self.screen.width()*.992, self.screen.height()*.992))

        self.btn_close.clicked.connect(self.hide)

        self.lbl_topic.hide()

        self._title = title_bar.TitleBar(self, '', 26)
        self._title.setStyleSheet('QWidget{color: #c2c2c2;background-color:#333}')
        self._title.close_btn.setStyleSheet('QPushButton{background-color: #333; border: 0px}')
        self._title.maximize_btn.hide()
        self._title.minimize_btn.hide()
        self._title.restore_btn.hide()
        self._title.mouseDoubleClickEvent = lambda x: x
        self.lay_titlebar.addWidget(self._title)
        self.lay_titlebar.addItem(self.lay_titlebar.takeAt(0))

        self.btn_close.hide()

    def set_data(self, title='', desc='', icon=''):
        self.resize(0, 0)
        QApplication.processEvents()
        self.lbl_topic.setText(title)
        self.lbl_message.setText(desc)
        self.lbl_logo.setText(icon)
        QApplication.processEvents()
        self.resize(0, 0)
        # if not self.isVisible():
        #
        #     #

    def showEvent(self, *args, **kwargs):
        self.setGeometry(QStyle.alignedRect(Qt.RightToLeft, Qt.AlignBottom, self.size(), self.screen))
        QApplication.processEvents()

    # def mousePressEvent(self, event):
    #     # QMouseEvent.
    #     if event.buttons() == Qt.RightButton:
    #         self.dragPos = event.globalPos()
    #         event.accept()
    #
    # def mouseMoveEvent(self, event):
    #     if event.buttons() == Qt.RightButton:
    #         self.move(self.pos() + event.globalPos() - self.dragPos)
    #         self.dragPos = event.globalPos()
    #         event.accept()


if __name__ == '__main__':
    from PySide.QtGui import QApplication
    app = QApplication([])
    ui = UInotification()
    ui.show()
    app.exec_()

