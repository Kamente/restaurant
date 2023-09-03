from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship

Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, Sequence('review_id_seq'), primary_key=True)
    star_rating = Column(Integer)
    rest_id = Column(Integer, ForeignKey('restaurant.rest_id'))
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def customer(self):
        return self.customer 
    
    def restaurant(self):
        return self.restaurant 

    def full_review(self):
        return f"Review for {self.restaurant.rest_name} by {self.customer.full_name()}: {self.star_rating} stars."
