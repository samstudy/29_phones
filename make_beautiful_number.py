from sqlalchemy.orm import sessionmaker, relationship
from copy_db import source_engine,dest_engine,Orders
import os, phonenumbers, time
from phonenumbers import carrier


Session = sessionmaker(bind=dest_engine)
session = Session()


def make_beautiful_number():
    sleeping_time = 180
    orders = session.query(Orders).all()
    connection = engine.connect()
    trans = connection.begin()
    for order in orders:
        connection.execute
        ("INSERT or IGNORE into orders(id,contact_name,contact_phone,contact_email,status,comment,price) VALUES(?,?,?,?,?,?,?)",
        (order.id,order.contact_name,order.contact_phone,
        order.contact_email,order.status,order.comment.order.price))
        beautiful_number = phonenumbers.parse(order.contact_phone, "RU").national_number
        connection.execute
        ("UPDATE orders set beautiful_number = ? where id=? ",(beautiful_number, order.id))
    trans.commit()
    time.sleep(sleeping_time)


if __name__ == "__main__":
    while True:
        make_beautiful_number()