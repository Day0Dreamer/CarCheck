import pandas as pd
from api.query_db import *
from sqlalchemy import exc


def excel2df(xls_path):
    xls = pd.ExcelFile(xls_path)
    df1 = xls.parse()
    return df1


if __name__ == '__main__':
    db = DB('sqlite:///C:\\Python\\CarCheck\\db.sqlite')

    # df = excel2df(r'excel_data/Novye_propuska.xlsx')
    df = excel2df(r'../excel_data/Novye_propuska.xlsx')
    df = df.fillna({'СРОК ДЕЙСТВИЯ ОТ':date.fromordinal(1), 'СРОК ДЕЙСТВИЯ ДО':date.fromordinal(1)})
    # df.keys()
    # print(df.to_string())

    # Select only needed columns
    x = df.reindex(columns=['СОБСТВЕННИК',
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

            db.add_new_car(**car_dict)
        except exc.IntegrityError as e:
            print(e)
            print(row)
