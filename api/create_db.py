# -*- coding: utf-8 -*-
""" This module creates a database and deletes previous one if it exists"""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == '__main__':

    from os import remove
    remove(r'../db.sqlite')

    # Create engine: engine
    engine = create_engine('sqlite:///../db.sqlite')
    # engine = create_engine('sqlite:///db.sqlite', echo=True)

Base = declarative_base()


class Permits(Base):
    """Representation of table Пропуски

    Methods:
    =======================
    get_to_dict()

    set_from_dict()


"""
    __tablename__ = 'Пропуски'
    client = relationship('Clients', back_populates='permit')
    client_id    = Column(Integer(), ForeignKey('Заказчики.id'))
    owner  = relationship('Owners', back_populates='permit')
    owner_id     = Column(Integer(), ForeignKey('Собственники.id'))
    car_number   = Column('РегЗнак', String(8), primary_key=True, unique=True)
    sts_number   = Column('СТС', String(11), unique=True)
    zone         = Column('ЗонаДействия', String(8))
    status = relationship('PermitStatus', back_populates='permit')
    status_id    = Column(Integer(), ForeignKey('СтатусыПропуска.id'))
    date_start   = Column('ДатаНачала', Date())
    date_end     = Column('ДатаКонца', Date())
    eco_class    = Column('ЭкоКласс', String())
    price        = Column('Цена', Float())
    payment      = Column('Оплата', Float())
    description  = Column('Примечания', String())
    tba_1        = Column('Путь', String())
    silenced     = Column('Silenced', Boolean(), default=False)
    hidden         = Column('Hidden', Boolean(), default=False)

    def __str__(self):
        return "РегЗнак: {}, ЗонаДей.: {}, От: {:^10}, До: {:^10}, Зак.: {}, Собст.: {}, Статус: {}, Цена: {}, " \
               "Оплата: {}, Примечания: {}, Silenced: {}, Hidden: {}".format(self.car_number,
                                                                             self.zone,
                                                                             self.date_start.__str__(),
                                                                             self.date_end.__str__(),
                                                                             self.client,
                                                                             self.owner,
                                                                             self.status,
                                                                             self.price,
                                                                             self.payment,
                                                                             self.description,
                                                                             self.silenced,
                                                                             self.hidden)

    def get_to_dict(self):
        """
        Returns:
            dict: client, owner, car_number, sts_number, zone, status, date_start, date_end, eco_class, price, payment,
            description, tba_1, silenced, hidden."""
        return {
            'client':      self.client,
            'owner':       self.owner,
            'car_number':  self.car_number,
            'sts_number':  self.sts_number,
            'zone':        self.zone,
            'status':      self.status,
            'date_start':  self.date_start,
            'date_end':    self.date_end,
            'eco_class':   self.eco_class,
            'price':       self.price,
            'payment':     self.payment,
            'description': self.description,
            'tba_1':       self.tba_1,
            'silenced':    self.silenced,
            'hidden':      self.hidden
        }

    def set_from_dict(self, **kwargs):
        """
        **kwargs:
            dict: client, owner, car_number, sts_number, zone, status, date_start, date_end, eco_class, price, payment,
            description, tba_1, silenced, hidden."""

        self.client =       kwargs['client']
        self.owner =        kwargs['owner']
        self.car_number =   kwargs['car_number']
        self.sts_number =   kwargs['sts_number']
        self.zone =         kwargs['zone']
        self.status =       kwargs['status']
        self.date_start =   kwargs['date_start']
        self.date_end =     kwargs['date_end']
        self.eco_class =    kwargs['eco_class']
        self.price =        kwargs['price']
        self.payment =      kwargs['payment']
        self.description =  kwargs['description']
        self.tba_1 =        kwargs['tba_1']
        self.silenced =     kwargs['silenced']
        self.hidden =       kwargs['hidden']


class Clients(Base):
    __tablename__ = 'Заказчики'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, unique=True)
    phone = Column(String)
    permit = relationship('Permits', back_populates='client')

    def __repr__(self):
        return str(self.name)
        # return "<Status(id='{}', name='{}')>".format(self.id, self.name)


class Owners(Base):
    __tablename__ = 'Собственники'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, unique=True)
    phone = Column(String)
    permit = relationship('Permits', back_populates='owner')

    def __repr__(self):
        return str(self.name)
        # return "<Status(id='{}', name='{}')>".format(self.id, self.name)


class PermitStatus(Base):
    __tablename__ = 'СтатусыПропуска'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    permit = relationship('Permits', back_populates='status')

    def __repr__(self):
        return str(self.name)
        # return "<Status(id='{}', name='{}')>".format(self.id, self.name)


# PermitStatus.__table__
class SessionWrap(object):
    def __init__(self, session_class):
        self.session = session_class()

    def __enter__(self):
        return self.session

    def __exit__(self, *args):
        # print(args)
        self.session.close()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    with SessionWrap(sessionmaker(bind=engine)) as session:
        session.add(Clients(id=0))
        session.add(Owners(id=0))
        session.commit()

