import phonenumbers, time
from phonenumbers import carrier
from create_local_db import destination_session,engine
from sqlalchemy import MetaData,Table, Column, Integer

SLEEP_TIME = 180
metadata = MetaData()


updated_orders = Table('updated_orders',metadata,
                 Column('contact_phone',Integer),
                 Column('upd_number',Integer))    


def make_beautiful_number():
    connection = engine.connect()
    transaction = connection.begin()
    target_orders = destination_session.query(updated_orders).filter(updated_orders.c.upd_number.is_(None))
    for order in target_orders:
        upd_number = phonenumbers.parse(order.contact_phone, "RU").national_number
        inserted_number = updated_orders.update().values(upd_number = upd_number).\
                                                  where(updated_orders.c.contact_phone == order.contact_phone)
        connection.execute(inserted_number)
    transaction.commit()
    time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    while True:
        make_beautiful_number()