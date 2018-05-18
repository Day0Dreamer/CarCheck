from pandas import ExcelWriter, ExcelFile
import api.query_db
from sqlalchemy import exc


def excel2df(xls_path):
    xls = ExcelFile(xls_path)
    _df = xls.parse()
    return _df


def df2excel(_df, xls_path):
    excel_writer = ExcelWriter(xls_path, 'xlsxwriter')
    # _df = pd.DataFrame if True else False
    # _df.to_excel(excel_writer, index=False)
    _df[['client']] = _df[['client']].astype(str)
    _df[['owner']] = _df[['owner']].astype(str)
    _df[['status']] = _df[['status']].astype(str)

    _df.to_excel(excel_writer, index=False)
    worksheet = excel_writer.sheets['Sheet1']
    worksheet.set_column("A:B", 40)
    print(excel_writer.save())



    # excel_writer.save()


def import_from_df(_df):
    db = api.query_db.DB()
    _df = _df.fillna({'СРОК ДЕЙСТВИЯ ОТ':api.query_db.date.fromtimestamp(0), 'СРОК ДЕЙСТВИЯ ДО':api.query_db.date.fromtimestamp(0)})
    # df.keys()
    # print(df.to_string())

    # Select only needed columns
    x = _df.reindex(columns=['СОБСТВЕННИК',
                            'ЗАКАЗЧИК',
                            '№ СТС',
                            'РЕГ.ЗНАК',
                            'ЗОНА ДЕЙСТВИЯ  ПРОПУСКА',
                            'СТАСТУС ПРОПУСКА',
                            'СРОК ДЕЙСТВИЯ ОТ',
                            'СРОК ДЕЙСТВИЯ ДО',
                            'ЦЕНА',
                            'ОПЛАТА',
                            'Примечания'])
    # get each row as an Item
    list_of_rows = x.iterrows()
    for index, row in list_of_rows:
        try:
            car_dict = dict(
                client=None or row['СОБСТВЕННИК'],
                owner=None or row['ЗАКАЗЧИК'],
                sts_number=None or row['№ СТС'],
                car_number=None or row['РЕГ.ЗНАК'],
                zone=None or row['ЗОНА ДЕЙСТВИЯ  ПРОПУСКА'],
                status=None or row['СТАСТУС ПРОПУСКА'],
                eco_class=None,
                date_start=None or row['СРОК ДЕЙСТВИЯ ОТ'],
                date_end=None or row['СРОК ДЕЙСТВИЯ ДО'],
                price=None or row['ЦЕНА'],
                payment=None or row['ОПЛАТА'],
                description=None or row['Примечания'],
                tba_1=None,
                hidden=False,
                silenced=False)

            db.add_new_car(car_dict)
        except exc.IntegrityError as e:
            print(e)
            print(row)


if __name__ == '__main__':


    # df = excel2df(r'excel_data/Novye_propuska.xlsx')
    df = excel2df(r'../excel_data/Novye_propuska.xlsx')
    import_from_df(df)
