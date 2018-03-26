from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == '__main__':

    from os import remove
    remove(r'../db.sqlite')

    # Create engine: engine
    engine = create_engine('sqlite:///../db.sqlite')
    # engine = create_engine('sqlite:///db.sqlite', echo=True)

# metadata = MetaData()
#
# # Define a new table with a name, count, amount, and valid column: data
# data = Table('Собственники', metadata,
#              Column('id', Integer(), unique=True, autoincrement=True, primary_key=True),
#              Column('name', String(255), unique=True)
#              )
#
# data2 = Table('Заказчики', metadata,
#               Column('id', Integer(), unique=True, autoincrement=True, primary_key=True),
#               Column('name', String(255), unique=True)
#               )
#
# data3 = Table('СтатусыПропуска', metadata,
#               Column('id', Integer(), unique=True, autoincrement=True, primary_key=True),
#               Column('name', String(255), unique=True)
#               )
#
# data4 = Table('Пропуски', metadata,
#               Column('Заказчик', Integer, ForeignKey('Заказчики.id')),
#               Column('Собственник', Integer(), ForeignKey('Собственники.id')),
#               Column('РегЗнак', String(8), primary_key=True, unique=True),
#               Column('ЗонаДействия', String(8)),
#               Column('Статус', Integer()),
#               Column('ДатаНачала', Date()),
#               Column('ДатаКонца', Date()),
#               Column('Цена', Float()),
#               Column('Оплата', Float()),
#               Column('Примечания', String())
#               )
#
# # Use the metadata to create the table
# metadata.create_all(engine)


Base = declarative_base()


class PermitStats(Base):
    __tablename__ = 'СтатусыПропуска'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    permit = relationship('Permits', back_populates='status_name')

    def __repr__(self):
        return "<Status(id='{}', name='{}')>".format(self.id, self.name)


class Permits(Base):
    __tablename__ = 'Пропуски'
    client = relationship('Clients', back_populates='permit')
    owner  = relationship('Owners', back_populates='permit')
    car_number   = Column('РегЗнак', String(8), primary_key=True, unique=True)
    zone         = Column('ЗонаДействия', String(8))
    status       = Column(Integer(), ForeignKey('СтатусыПропуска.id'))
    status_name  = relationship('PermitStats', back_populates='permit')
    date_start   = Column('ДатаНачала', Date())
    date_end     = Column('ДатаКонца', Date())
    price        = Column('Цена', Float())
    payment      = Column('Оплата', Float())
    description  = Column('Примечания', String())

    def __repr__(self):
        return "Заказчик: {}, Собственник: {},РегЗнак: {}, ЗонаДействия: {},Статус: {}, ДатаНачала: {}, " \
               "ДатаКонца: {},Цена: {}, Оплата: {}, Примечания: {}".format(self.client, self.owner, self.car_number,
                                                                           self.zone, self.status, self.date_start,
                                                                           self.date_end, self.price, self.payment,
                                                                           self.description)


class Owners(Base):
    __tablename__ = 'Собственники'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    permit_car_number = Column(String(), ForeignKey('Пропуски.РегЗнак'))

    permit = relationship('Permits', back_populates='owner')

    def __repr__(self):
        return "<Status(id='{}', name='{}')>".format(self.id, self.name)


class Clients(Base):
    __tablename__ = 'Заказчики'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    permit_car_number = Column(String(), ForeignKey('Пропуски.РегЗнак'))

    permit = relationship('Permits', back_populates='client')

    def __repr__(self):
        return "<Status(id='{}', name='{}')>".format(self.id, self.name)


# PermitStats.__table__
if __name__ == '__main__':
    Base.metadata.create_all(engine)

