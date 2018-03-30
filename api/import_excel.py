import pandas as pd
from api.query_db import *
from sqlalchemy import exc


def excel2df(xls_path):
    xls = pd.ExcelFile(xls_path)
    df1 = xls.parse()
    return df1


if __name__ == '__main__':
    db = DB('sqlite:///C:\\Python\\CarCheck\\db.sqlite')

    # df = excel2df(r'excel_data/Propuski2.xlsx')
    df = excel2df(r'../excel_data/Propuski2.xlsx')
    df = df.fillna({'StartDate':date.fromordinal(1), 'EndDate':date.fromordinal(1)})
    # df.keys()
    # print(df.to_string())

    # 1st list
    x = [x for i, x in df.loc[:, ['СОБСТВЕННИК',
                                  'ЗАКАЗЧИК',
                                  'РЕГ.ЗНАК',
                                  'ЗОНА ДЕЙСТВИЯ  ПРОПУСКА',
                                  'СТАСТУС ПРОПУСКА',
                                  'StartDate',
                                  'EndDate']].iterrows()]
    list_of_rows = x
    for row in list_of_rows:
        try:
            db.add_new_car(owner_name=row['СОБСТВЕННИК'],
                           client_name=row['ЗАКАЗЧИК'],
                           car_number=row['РЕГ.ЗНАК'],
                           zone=row['ЗОНА ДЕЙСТВИЯ  ПРОПУСКА'],
                           status=row['СТАСТУС ПРОПУСКА'],
                           date_start=row['StartDate'],
                           date_end=row['EndDate'])
        except exc.IntegrityError as e:
            print(e)
            print(row)
