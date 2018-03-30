# pd.set_option('display.width', pd.get_option('display.width')*3)
import ui
import api.query_db


if __name__ == '__main__':
    app = ui.QApplication([])
    ui = ui.UIMainWindow()

    db = api.query_db.DB('sqlite:///C:\\Python\\CarCheck\\db.sqlite')
    li = db.get_all()
    # [print(i) for i in li]
    empty = [{}]

    ui.btn_1.clicked.connect(lambda: ui.fill_table(li))
    ui.btn_1.setText('Загрузить таблицу')
    ui.btn_2.clicked.connect(lambda: ui.fill_table(empty))
    ui.btn_2.setText('Очистить таблицу')
    search = lambda: ui.fill_table(db.find_entry(ui.line_search.text(), ui.box_search_selector.currentText()))
    ui.btn_3.setText('Повторить поиск')
    ui.btn_3.clicked.connect(search)
    ui.line_search.textChanged.connect(search)
    ui.box_search_selector.currentIndexChanged.connect(search)
    ui.btn_4.setText('Раскрасить')
    ui.btn_4.clicked.connect(lambda: ui.paint_by_date())



    ui.show()
    app.exec_()
