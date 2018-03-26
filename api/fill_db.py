# from sqlalchemy import *
# from sqlalchemy.orm import sessionmaker
from api.create_db import *
from datetime import date

if __name__ == '__main__':
    engine = create_engine('sqlite:///../db.sqlite')
    Session = sessionmaker(bind=engine)

    # Add new items to СтатусыПропуска
    session = Session()
    session.query(PermitStats).delete()  # Drop all data from the table
    for i in ['Разовый', 'Временный', 'Полгода', 'Год']:
        session.add(PermitStats(name=i))
    session.commit()
    session.close()

    # Add sample owners
    session = Session()
    session.query(Owners).delete()  # Drop all data from the table
    for i, v in enumerate(['ООО "Развоз"', 'МАКТРАНС', 'УМ-77', 'Кучин']):
        session.add(Owners(name=v))
    session.commit()
    session.close()

    # Add sample clients
    session = Session()
    session.query(Clients).delete()  # Drop all data from the table
    for i in ['ДИМА', 'Артем Хачатрян', 'Джамал', 'МАКТРАНС']:
        session.add(Clients(name=i))
    session.commit()
    session.close()

    # Add sample permits
    session = Session()
    session.query(Permits).delete()  # Drop all data from the table
    test = session.query(PermitStats).filter(PermitStats.name == 'Год').first()
    session.add(Permits(client_id=1, owner_id=3, car_number='М906РО48', zone='СК', status_id=1, date_start=date(1991,1,1), date_end=date(1991,1,31), price=190.00, payment=180.00, description='Однако'))
    session.add(Permits(client_id=2, owner_id=3, car_number='Т460ОТ77', zone='СК', status=test))
    session.commit()
    session.close()


else:
    # Create engine: engine
    engine = create_engine('sqlite:///db.sqlite', echo=True)
    Session = sessionmaker(bind=engine)

    # Delete everything from query
    session = Session()
    session.query(PermitStats).count()
    session.commit()
    session.close()

    session = Session()
    session.query(Clients).all()
    session.close()

    session = Session()
    session.query(Permits).first()
    session.close()

    session.query(PermitStats).all()
