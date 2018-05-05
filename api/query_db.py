# -*- coding: utf-8 -*-
""" This module manages requests to the DB"""
from datetime import date, timedelta
from math import isnan
from api.create_db import *


def xstr(s):
    if s is not str:
        return ''
    return str(s)


class DB(object):
    def __init__(self, db_path='sqlite:///C:\\Python\\CarCheck\\db.sqlite'):
        self.engine = create_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self):
        result = []
        with SessionWrap(self.Session) as session:
            for permit in session.query(Permits):  # .order_by(Permits.car_number):
                result.append(permit.get_to_dict())
                # print(vars(permit))
            # print(Permits.__dict__)
        return result

    @staticmethod
    def relational_search_or_create(data_set, table_class, data_set_key, session):
        """

        Args:
            data_set: **Unpacked dictionary with the data
            table_class: Class responsible for a DB-table
            data_set_key: Field to search for (For Clients class it is 'clients')

        Returns:
            New modified data_set
        """
        nan = False
        if isinstance(data_set[data_set_key], float):            # If client_name is float
            nan = isnan(data_set[data_set_key])                  # Check if client_name is non-a-number

        item = session.query(table_class).filter(                # Out of "Clients" table
            table_class.name == data_set[data_set_key]).first()  # Look for existing client
        if item is None and not nan:                             # If client is not found and new client has a value
            item = table_class(name=data_set[data_set_key])      # Create a new one
        elif item is None and nan:                               # If client is not found and new client has no value
            item = session.query(table_class).filter(            # Get client of id=0
                table_class.id == 0).first()                     # which is of value None
        data_set[data_set_key] = item                            # Save new client-reference back to the data_set
        return data_set

    def add_new_car(self, data_set):
        """, client_name=None, owner_name=None, car_number=None, sts_number=None, zone=None, status=None,
                    date_start=None, date_end=None, eco_class=None, price=None, payment=None, description=None,
                    tba_1=None, silenced=None, hide=None):"""

        with SessionWrap(self.Session) as session:

            # nan = False
            # if isinstance(data_set['client'], float):             # If client_name is float
            #     nan = isnan(data_set['client'])                   # Check if client_name is non-a-number
            #
            # client = session.query(Clients).filter(               # Out of "Clients" table
            #     Clients.name == data_set['client']).first()       # Look for existing client
            # if client is None and not nan:                        # If client is not found and new client has a value
            #     client = Clients(name=data_set['client'])         # Create a new one
            # elif client is None and nan:                          # If client is not found and new client has no value
            #     client = session.query(Clients).filter(           # Get client of id=0
            #         Clients.id == 0).first()                      # which is of value None
            # data_set['client'] = client                           # Save new client-reference back to the data_set
            data_set = self.relational_search_or_create(data_set, Clients, 'client', session)

            # nan = False
            # if isinstance(data_set['owner'], float):
            #     nan = isnan(data_set['owner'])
            #
            # owner = session.query(Owners).filter(
            #     Owners.name == data_set['owner']).first()
            # if owner is None and not nan:
            #     owner = Owners(name=data_set['owner'])
            # elif owner is None and nan:
            #     owner = session.query(Owners).filter(
            #         Owners.id == 0).first()
            # data_set['owner'] = owner
            data_set = self.relational_search_or_create(data_set, Owners, 'owner', session)

            data_set['status'] = session.query(PermitStatus).filter(  # Look into PermitStatus table
                PermitStatus.name == data_set['status']).first()      # for the appropriate status_id

            session.add(Permits(**data_set))
            print('adding new car')
            session.commit()

    def change_car(self, data_set):
        with SessionWrap(self.Session) as session:
            # entry = session.query(Permits).filter(Permits.car_number == data_set['car_number']).first()
            entry = self.__find_entry(data_set['car_number'], 'car_number', session)[0]
                # session.query(Permits).filter(Permits.car_number == data_set['car_number']).first()
            # print(type(entry))
            # print('e', entry)
            # print('n', data_set)
            data_set = self.relational_search_or_create(data_set, Clients, 'client', session)
            data_set = self.relational_search_or_create(data_set, Owners, 'owner', session)
            print(data_set)
            entry.set_from_dict(**data_set)
            session.commit()

    @staticmethod
    def __find_entry(request, column_of_interest, session):
        """
        Finds all entries and returns them as list of SQL-objects

        Args:
            request:
            column_of_interest:

        Returns:
            :obj:`list` of :obj:`dict`: List of SQL-objects
        """
        result = []
        column_dict = {
            'client':      Permits.client.has(Clients.name.like('%{}%'.format(request))),
            'owner':       Permits.owner.has(Clients.name.like('%{}%'.format(request))),
            'car_number':  Permits.car_number.like('%{}%'.format(request)),
            'sts_number':  Permits.sts_number.like('%{}%'.format(request)),
            'zone':        Permits.zone.like('%{}%'.format(request)),
            'status':      Permits.status.has(Clients.name.like('%{}%'.format(request))),
            'date_start':  Permits.date_start.like('%{}%'.format(request)),
            'date_end':    Permits.date_end.like('%{}%'.format(request)),
            'eco_class':   Permits.eco_class.like('%{}%'.format(request)),
            'price':       Permits.price.like('%{}%'.format(request)),
            'payment':     Permits.payment.like('%{}%'.format(request)),
            'description': Permits.description.like('%{}%'.format(request)),
            'tba_1':       Permits.tba_1.like('%{}%'.format(request)),
            'silenced':    Permits.silenced.like('%{}%'.format(request)),
            'hidden':      Permits.hidden.like('%{}%'.format(request))}

        column_of_interest = column_dict[column_of_interest]
        for permit in session.query(Permits).filter(column_of_interest).order_by(Permits.date_end):
            result.append(permit)
        return result

    def get_entry_as_dict(self, request, column_of_interest):
        with SessionWrap(self.Session) as session:
            list_of_entries = self.__find_entry(request, column_of_interest, session)
            list_of_dicts = [entry.get_to_dict() for entry in list_of_entries]
        return list_of_dicts


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
    db = DB('sqlite:///db.sqlite')  # works for console

    # print(db.find_entry('Х813НУ190'))
    # db.add_new_car('МАКТРАНС0', 'Хабибулина', 'Т4600Т27', 'СК', 'Год', date(1991, 1, 1), date(1991, 1, 21), 10, 10)
    # DB().exists(Owners, 'МАКТРАНС')
    # print(db.get_all())
    # [pprint('Для номера {}, {}, {} день сдачи через {} дней'.format(x1,x2,x3,y)) for x1,x2,x3,y in DB().get_remaining_days()]