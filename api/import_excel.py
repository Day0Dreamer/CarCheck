import pandas as pd
from api.query_db import *

def excel2df(xls_path):
    xls = pd.ExcelFile(xls_path)
    df1 = xls.parse()
    return df1


if __name__ == '__main__':
    db = DB()

    df = excel2df(r'../excel_data/Propuski.xlsx')
    # print(df.to_string())

    # 1st list
    x = [x for i, x in df.loc[:, ['ЗАКАЗЧИК', 'РЕГ.ЗНАК', 'ЗОНА ДЕЙСТВИЯ  ПРОПУСКА', 'СРОК ДЕЙСТВИЯ ПО']].iterrows()]
    list_of_rows = x
    for row in list_of_rows:
        db.add_new_car(client_name=row['ЗАКАЗЧИК'],
                         car_number=row['РЕГ.ЗНАК'],
                         zone=row['ЗОНА ДЕЙСТВИЯ  ПРОПУСКА'],
                         date_end=row['СРОК ДЕЙСТВИЯ ПО'])
