"https://dbdiagram.io/d/64f3140102bd1c4a5ed84328"  # database tables


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URI = 'sqlite:///restaurant.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    rest_id = Column(Integer, Sequence('rest_id_seq'), primary_key=True)
    rest_name = Column(String)
    rest_price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')


class Customer(Base):
    __tablename__ = 'customer'
    cust_id = Column(Integer, Sequence('cust_id_seq'), primary_key=True)
    cust_fname = Column(String)
    cust_lname = Column(String)

    reviews = relationship('Review', back_populates='customer')


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, Sequence('review_id_seq'), primary_key=True)
    star_rating = Column(Integer)
    rest_id = Column(Integer, ForeignKey('restaurant.rest_id'))
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
