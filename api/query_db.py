from datetime import date, timedelta
from math import isnan
from api.create_db import *


def xstr(s):
    if s is not str:
        return ''
    return str(s)


class DB(object):
    def __init__(self, db_path='sqlite:///db.sqlite'):
        self.engine = create_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self):
        result = []
        with SessionWrap(self.Session) as session:
            for permit in session.query(Permits):  # .order_by(Permits.car_number):
                result.append(permit.dict())
        return result

    def add_new_car(self, client_name=None, owner_name=None, car_number=None, zone=None, status=None, date_start=None,
                    date_end=None, price=None, payment=None, description=None):
        with SessionWrap(self.Session) as session:
            nan = False
            if isinstance(client_name, float):
                nan = isnan(client_name)
            client = session.query(Clients).filter(Clients.name == client_name).first()  # Get existing client
            if client is None and not nan:   # If existing is None and new client is not NaN
                client = Clients(name=client_name)           # Create a new one
            elif client is None and nan:
                client = session.query(Clients).filter(Clients.id == 0).first()

            nan = False
            if isinstance(owner_name, float):
                nan = isnan(owner_name)
            owner = session.query(Owners).filter(Owners.name == owner_name).first()      # Get existing owner
            if owner is None and not nan:   # If existing is None and new client is not NaN
                owner = Owners(name=owner_name)           # Create a new one
            elif owner is None and nan:
                owner = session.query(Owners).filter(Owners.id == 0).first()

            session.add(Permits(client=client, owner=owner, car_number=car_number, zone=zone,
                                status=session.query(PermitStats).filter(PermitStats.name == status).first(),
                                date_start=date_start, date_end=date_end, price=price, payment=payment,
                                description=description))
            session.commit()

    def find_entry(self, request, column_of_interest):
        result = []
        column_dict = {
            'Clients': Permits.client.has(Clients.name.like('%{}%'.format(request))),
            'Owners': Permits.owner.has(Clients.name.like('%{}%'.format(request))),
            'РегЗнак': Permits.car_number.like('%{}%'.format(request)),
            'ЗонаДействия': Permits.zone.like('%{}%'.format(request)),
            'PermitStats': Permits.status.has(Clients.name.like('%{}%'.format(request))),
            'ДатаНачала': Permits.date_start.like('%{}%'.format(request)),
            'ДатаКонца': Permits.date_end.like('%{}%'.format(request)),
            'Цена': Permits.price.like('%{}%'.format(request)),
            'Оплата': Permits.payment.like('%{}%'.format(request)),
            'Примечания': Permits.description.like('%{}%'.format(request)),
            'Silenced': Permits.silenced.like('%{}%'.format(request))}
        column_of_interest = column_dict[column_of_interest]
        with SessionWrap(self.Session) as session:
            for permit in session.query(Permits).filter(column_of_interest).order_by(Permits.date_end):
                result.append(permit.dict())
        # print(result)
        return result

    # print(session.query(Permits).filter(Permits.client.has(Clients.name.like('ДИ%'))).all())

    def test(self):
        with SessionWrap(self.Session) as session:
            if 0:
                session = Session()
            print(session.query(Permits).count())


    def get_remaining_days(self):
        result = []
        with SessionWrap(self.Session) as session:
            for permit in session.query(Permits).order_by(Permits.date_end):
                days_remaining = permit.date_end-date.today()
                result.append((permit.client, xstr(permit.owner), permit.car_number, days_remaining.days))
        return result


if __name__ == '__main__':
    db = DB('sqlite:///../db.sqlite')
    db = DB('sqlite:///db.sqlite')

    # print(db.find_entry('Х813НУ190'))
    # db.add_new_car('МАКТРАНС0', 'Хабибулина', 'Т4600Т27', 'СК', 'Год', date(1991, 1, 1), date(1991, 1, 21), 10, 10)
    # DB().exists(Owners, 'МАКТРАНС')
    # print(db.get_all())
    # [pprint('Для номера {}, {}, {} день сдачи через {} дней'.format(x1,x2,x3,y)) for x1,x2,x3,y in DB().get_remaining_days()]