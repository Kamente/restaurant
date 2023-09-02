from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from restaurant import Restaurant

Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, Sequence('review_id_seq'), primary_key=True)
    star_rating = Column(Integer)
    rest_id = Column(Integer, ForeignKey('restaurant.rest_id'))
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')
