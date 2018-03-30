from api.create_db import *
from datetime import date

if __name__ == '__main__':
    engine = create_engine('sqlite:///../db.sqlite')
    Session = sessionmaker(bind=engine)


    # Add new items to СтатусыПропуска
    with SessionWrap(Session) as session:
        session.query(PermitStatus).delete()  # Drop all data from the table
        for i in ['разовый', 'временный', 'полугодовой', 'годовой']:
            session.add(PermitStatus(name=i))
        session.commit()

    # # Add sample owners
    # with SessionWrap(Session) as session:
    #     session.query(Owners).delete()  # Drop all data from the table
    #     for i, v in enumerate(['ООО "Развоз"', 'МАКТРАНС', 'УМ-77', 'Кучин']):
    #         session.add(Owners(name=v))
    #     session.commit()
    #     session.close()
    #
    # # Add sample clients
    # with SessionWrap(Session) as session:
    #     session.query(Clients).delete()  # Drop all data from the table
    #     for i in ['ДИМА', 'Артем Хачатрян', 'Джамал', 'МАКТРАНС']:
    #         session.add(Clients(name=i))
    #     session.commit()
    #
    # # Add sample permits
    # with SessionWrap(Session) as session:
    #     session.query(Permits).delete()  # Drop all data from the table
    #     test = session.query(PermitStatus).filter(PermitStatus.name == 'Год').first()
    #     session.add(Permits(client_id=1, owner_id=3, car_number='М906РО48', zone='СК', status_id=1, date_start=date(1991,1,1), date_end=date(1991,1,31), price=190.00, payment=180.00, description='Однако'))
    #     session.add(Permits(client_id=2, owner_id=3, car_number='Т460ОТ77', zone='СК', status=test))
    #     session.commit()
    #
