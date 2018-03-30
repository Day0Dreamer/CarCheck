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
    __tablename__ = 'Пропуски'
    client = relationship('Clients', back_populates='permit')
    client_id    = Column(Integer(), ForeignKey('Заказчики.id'))
    owner  = relationship('Owners', back_populates='permit')
    owner_id     = Column(Integer(), ForeignKey('Собственники.id'))
    car_number   = Column('РегЗнак', String(8), primary_key=True, unique=True)
    zone         = Column('ЗонаДействия', String(8))
    status = relationship('PermitStats', back_populates='permit')
    status_id    = Column(Integer(), ForeignKey('СтатусыПропуска.id'))
    date_start   = Column('ДатаНачала', Date())
    date_end     = Column('ДатаКонца', Date())
    price        = Column('Цена', Float())
    payment      = Column('Оплата', Float())
    description  = Column('Примечания', String())
    silenced     = Column('Silenced', Boolean(), default=False)
    hide         = Column('Hidden', Boolean(), default=False)

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

    def dict(self):
        return {
            'Clients':      self.client,
            'Owners':       self.owner,
            'РегЗнак':      self.car_number,
            'ЗонаДействия': self.zone,
            'PermitStats':  self.status,
            'ДатаНачала':   self.date_start,
            'ДатаКонца':    self.date_end,
            'Цена':         self.price,
            'Оплата':       self.payment,
            'Примечания':   self.description,
            'Silenced':     self.silenced
        }


class Clients(Base):
    __tablename__ = 'Заказчики'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, unique=True)
    permit = relationship('Permits', back_populates='client')

    def __repr__(self):
        return str(self.name)
        # return "<Status(id='{}', name='{}')>".format(self.id, self.name)


class Owners(Base):
    __tablename__ = 'Собственники'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, unique=True)
    permit = relationship('Permits', back_populates='owner')

    def __repr__(self):
        return str(self.name)
        # return "<Status(id='{}', name='{}')>".format(self.id, self.name)


class PermitStats(Base):
    __tablename__ = 'СтатусыПропуска'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    permit = relationship('Permits', back_populates='status')

    def __repr__(self):
        return str(self.name)
        # return "<Status(id='{}', name='{}')>".format(self.id, self.name)


# PermitStats.__table__
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

