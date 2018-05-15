# -*- coding: utf-8 -*-
""" This module manages requests to the DB"""
import pandas as pd
from datetime import date, timedelta
from math import isnan
from api.create_db import *
pd.set_option('display.width', pd.get_option('display.width')*3)



class DataType(object):
    OBJECT = 1
    DICT = 2
    DATAFRAME = 3

def xstr(s):
    """This method converts any non-sting objects as empty stings and returns stings as stings.

    Args:
        s(str): A potential string

    Returns:
        str: Always return a string, if received None, then an empty sting.
    """
    if s is not str:
        return ''
    return s


class DB(object):
    """
    DB Class works with a database, creating a connection to it, and offering methods for common operations.
    """
    def __init__(self, db_path='sqlite:///C:\\Python\\CarCheck\\db.sqlite'):
        """
        Creates db_engine and a session handle

        Args:
            db_path: (:class:`DB`) Relative or Absolute path to the DB
        """
        self.engine = create_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self, return_type):
        """
        Return all the rows in a Permits table

        Args:
            return_type(DataType): What type of data to return
        Returns:
            `list` `dataframe`: of Permits objects or Permits dictionaries
        """

        objects = []
        dicts = []
        with SessionWrap(self.Session) as session:
            for permit in session.query(Permits).order_by(Permits.date_end):
                objects.append(permit)
                dicts.append(permit.get_to_dict())
            if return_type == DataType.OBJECT:
                result = objects
            elif return_type == DataType.DICT:
                result = dicts
            elif return_type == DataType.DATAFRAME:
                result = pd.DataFrame(dicts)
            else:
                return None
        return result

    @staticmethod
    def relational_search_or_create(data_set, table_class, data_set_key, session):
        """
        This method searches for existing entry in a relational table, gets the first entry and
        injects it into the data_set.
        In case the searched item is None or Nan or empty object corresponding to id=0 is inserted.
        Otherwise the method creates a new entry inside the related table and relays it's handle to the data_set.

        Args:
            data_set(dict): Dictionary with the data containing all the fields for a table's columns
            table_class: Class responsible for a DB-table
            data_set_key(str): Field to search for (For Clients class it is 'clients')

        Returns:
            dict: New modified data_set
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
        """TODO edit this."""

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
        """
        Modifies an entry in the DB

        Args:
            data_set(dict): data_set containing a new data for a found entry in the DB
        """
        with SessionWrap(self.Session) as session:
            entry = self._find_entry(data_set['car_number'], 'car_number', session)[0]
            data_set = self.relational_search_or_create(data_set, Clients, 'client', session)
            data_set = self.relational_search_or_create(data_set, Owners, 'owner', session)
            data_set = self.relational_search_or_create(data_set, PermitStatus, 'status', session)
            print(data_set)
            entry.set_from_dict(**data_set)
            session.commit()

    @staticmethod
    def _find_entry(request, column_of_interest, session):
        """
        Finds all entries and returns them as list of SQL-objects
        Needs a already started session

        Args:
            request(str): Value contained in a table-cell to find
            column_of_interest(str): Column of a db-table to search across
            session(self.Session): DB session to work with

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
        """
        Starts a :obj:`self.Session` finds and returns a DB entry in a `list` of `dict` of `str` format.

        Args:
            request(str): Value contained in a table-cell to find
            column_of_interest(str): Column of a db-table to search across

        Returns:
            list: of dicts with text representation
        """
        with SessionWrap(self.Session) as session:
            list_of_entries = self._find_entry(request, column_of_interest, session)
            list_of_dicts = [entry.get_to_dict() for entry in list_of_entries]
        return list_of_dicts

    def delete_entry(self, request, column_of_interest):
        """
        Deletes an entry

        Args:
            request(str): Value contained in a table-cell to find
            column_of_interest(str): Column of a db-table to search across

        """
        with SessionWrap(self.Session) as session:
            list_of_entries = self._find_entry(request, column_of_interest, session)
            # list_of_dicts = [entry.get_to_dict() for entry in list_of_entries]
            session.delete(list_of_entries[0])
            session.commit()
        # return list_of_dicts


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