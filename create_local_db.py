from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, DateTime, String, Integer
import sqlalchemy as sa


engine = create_engine('URI')
destination_session = Session(engine)
Base = declarative_base()


class NewOrders(Base):
    __tablename__ = 'updated_orders'
    orders_id = sa.Column(sa.Integer, primary_key=True)
    created = sa.Column(sa.DateTime)
    status = sa.Column(sa.String)
    confirmed = sa.Column(sa.DateTime)
    contact_phone = sa.Column(sa.Unicode(255))
    contact_email = sa.Column(sa.String)
    price = sa.Column(sa.Integer)
    comment = sa.Column(sa.String)
    contact_name = sa.Column(String)

    def __init__(self, orders_id, created, status, confirmed,
                 contact_phone, contact_email, price, comment, contact_name):
        self.orders_id = orders_id
        self.created = created
        self.status = status
        self.confirmed = confirmed
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.price = price
        self.comment = comment
        self.contact_name = contact_name


if __name__ == "__main__":
    Base.metadata.create_all(engine)
