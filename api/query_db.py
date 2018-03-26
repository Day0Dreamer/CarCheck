from api.create_db import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///../db.sqlite')
    Session = sessionmaker(bind=engine)

    session = Session()
    for permit in session.query(Permits).order_by(Permits.car_number):
        print(permit)
