import pandas as pd


def excel2df(xls_path):
    xls = pd.ExcelFile(xls_path)
    df1 = xls.parse()
    return df1


if __name__ == '__main__':
    df = excel2df(r'../excel_data/Propuski.xlsx')
    print(df)
