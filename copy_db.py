from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os


Base = automap_base()
source_engine = create_engine('postgresql://score:Rysherat2@shopscore.devman.org:5432/shop')
dest_uri = ('sqlite://///'+ os.getcwd() +'/orders.db')
dest_engine = create_engine(dest_uri)
dest_session = sessionmaker(dest_engine)

Base.prepare(source_engine, reflect=True)
Orders = Base.classes.orders
source_session = Session(source_engine)

def get_table_attribute():
    table_attribute = source_session.query(Orders.id, Orders.contact_name, 
                                           Orders.contact_phone, Orders.contact_email,
                                           Orders.status, Orders.created, Orders.confirmed,
                                           Orders.comment, Orders.price)
    return table_attribute


def create_table_with_data(table_attribute):
    metadata = MetaData(bind=dest_engine)
    columns = [Column(desc['name'], desc['type']) for desc in table_attribute.column_descriptions]
    table = Table("orders", metadata, *columns)
    table.create(dest_engine)
    session = dest_session()
    for row in table_attribute:
        session.execute(table.insert(row))
    session.commit()


if __name__ == "__main__":
    table_attribute = get_table_attribute()
    create_table_with_data(table_attribute)


