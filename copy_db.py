from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from create_local_db import NewOrders,destination_session
import sqlalchemy as sa


Base = automap_base()
source_engine = create_engine('postgresql://score:Rysherat2@shopscore.devman.org:5432/shop')
Base.prepare(source_engine, reflect=True)
Orders = Base.classes.orders
source_session = Session(source_engine)


def insert_into_db():
    inserted_orders = source_session.query(Orders)
    for order in inserted_orders:
        target_order = NewOrders(order.id, order.created, order.status,
                                 order.confirmed, order.contact_phone, order.contact_email,
                                 order.price,order.comment,order.contact_name)
        destination_session.add(target_order)
        destination_session.commit()


if __name__ == "__main__":
    insert_into_db()
    
