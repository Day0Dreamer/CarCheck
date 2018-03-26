from datetime import date
from api.create_db import *


class DB(object):
    def __init__(self):
        self.engine = create_engine('sqlite:///../db.sqlite')
        self.Session = sessionmaker(bind=engine)

    def get_all(self):
        result = []
        with SessionWrap(self.Session) as session:
            for permit in session.query(Permits).order_by(Permits.car_number):
                result.append(permit.__repr__())
        return result

    def add_new_car(self, client_name, owner_name, car_number, zone, status, date_start, date_end,
                    price, payment, description=None):
        with SessionWrap(self.Session) as session:

            client = session.query(Clients).filter(Clients.name == client_name).first()  # Get existing client
            if client is None:
                client = Clients(name=client_name)                                       # Or create a new one

            owner = session.query(Owners).filter(Owners.name == owner_name).first()      # Get existing owner
            if owner is None:
                owner = Owners(name=owner_name)                                          # Or create a new one

            session.add(Permits(client=client, owner=owner, car_number=car_number, zone=zone,
                                status=session.query(PermitStats).filter(PermitStats.name == status).first(),
                                date_start=date_start, date_end=date_end, price=price, payment=payment,
                                description=description))
            session.commit()

    @staticmethod
    def find_using_car_number(car_number):
        result = []
        with SessionWrap(Session) as session:

            for permit in session.query(Permits).filter(Permits.car_number == car_number).order_by(Permits.car_number):
                result.append(permit.__repr__())
        return result

    def test(self):
        with SessionWrap(Session) as session:
            if 0:
                session = Session()
            print(session.query(Permits).count())


if __name__ == '__main__':
    engine = create_engine('sqlite:///../db.sqlite')
    Session = sessionmaker(bind=engine)

    # print(DB().find_using_car_number('М906РО48'))
    # DB().add_new_car('МАКТРАНС0', 'Хабибулина', 'Т4600Т27', 'СК', 'Год', date(1991, 1, 1), date(1991, 1, 21), 10, 10)
    # DB().exists(Owners, 'МАКТРАНС')
    [print(x) for x in DB().get_all()]
