# from sqlalchemy import *
# from sqlalchemy.orm import sessionmaker
from api.create_db import *

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
    owner = [session.query(Owners).filter(Owners.name == 'МАКТРАНС').first()]
    session.add(Permits(owner=owner, car_number='М906РО48', zone='СК', status=1))
    session.add(Permits(owner=owner, car_number='Т460ОТ77', zone='СК', status=1))
    session.commit()
    session.close()


else:
    def insert_new(table_name: str, data: list):
        metadata = MetaData()
        permit_status = Table(table_name, metadata, autoload=True, autoload_with=engine)
        stmt = insert(permit_status)
        values_list = data
        results = connection.execute(stmt, values_list)
        print(results.rowcount)  # Print result rowcount
        stmt = select([permit_status])  # Build a select statement to validate the insert
        print(connection.execute(stmt).fetchall())  # Print the result of executing the query.

    # Create engine: engine
    engine = create_engine('sqlite:///db.sqlite', echo=True)
    Session = sessionmaker(bind=engine)

    # connection = engine.connect()
    # Delete everything from query
    session = Session()
    session.query(PermitStats).count()
    session.commit()
    session.close()

    insert_new('СтатусыПропуска', [{'name': 'Разовый'}, {'name': 'Временный'}, {'name': 'Полгода'}, {'name': 'Год'}])

    from api.create_db import Clients
    session = Session()
    session.query(Clients).all()
    session.close()

    from api.create_db import Permits
    session = Session()
    session.query(Permits).first()
    session.close()

    session.query(PermitStats).all()



    session.dirty
    session.new
    insert_new('Заказчики', [{'name': 'Чел'}])
    insert_new('Test', [{'Один': 'Чел'}])

    insert_new('Пропуски', [{'Заказчик': 1},
                            {'Собственник': 1},
                            {'РегЗнак': 'фывфы'},
                            ])

    insert_new('Пропуски', [{'Заказчик': 1},
                            {'Собственник': 1},
                            {'РегЗнак': 'фывфывфы'},
                            {'ЗонаДействия': 'СК'},
                            {'Статус': '0'},
                            {'ДатаНачала': '01.01.1991'},
                            {'ДатаКонца': '02.02.1991'},
                            {'Цена': 12333},
                            {'Оплата': 12333},
                            {'Примечания': 'Нет'}
                            ])
