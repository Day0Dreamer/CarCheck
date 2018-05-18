# -*- coding: utf-8 -*-

# Form implementation generated from reading user_interface file 'C:\Python\CarCheck\user_interface\widgets\import_view.user_interface'
#
# Created: Sun May  6 22:18:45 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class Ui_import_view_ui(object):
    def setupUi(self, import_view_ui):
        import_view_ui.setObjectName("import_view_ui")
        import_view_ui.resize(1129, 554)
        self.horizontalLayout_2 = QHBoxLayout(import_view_ui)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_browse = QPushButton(import_view_ui)
        self.btn_browse.setMinimumSize(QSize(0, 50))
        self.btn_browse.setObjectName("btn_browse")
        self.horizontalLayout.addWidget(self.btn_browse)
        self.btn_import = QPushButton(import_view_ui)
        self.btn_import.setMinimumSize(QSize(0, 50))
        self.btn_import.setObjectName("btn_import")
        self.horizontalLayout.addWidget(self.btn_import)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QTextBrowser(import_view_ui)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(import_view_ui)
        QMetaObject.connectSlotsByName(import_view_ui)

    def retranslateUi(self, import_view_ui):
        import_view_ui.setWindowTitle(QApplication.translate("import_view_ui", "Form", None, QApplication.UnicodeUTF8))
        self.btn_browse.setText(QApplication.translate("import_view_ui", "Browse", None, QApplication.UnicodeUTF8))
        self.btn_import.setText(QApplication.translate("import_view_ui", "Import", None, QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QApplication.translate("import_view_ui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QApplication.UnicodeUTF8))

