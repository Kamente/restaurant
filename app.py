from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'  
    id = Column(Integer, primary_key=True)
    name = Column(String)  
    price = Column(Integer)  

  
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship(
        'Customer', secondary='reviews', back_populates='restaurants')

    def reviews(self):
        return session.query(Review).filter_by(restaurant=self).all()

    def customers(self):
        return session.query(Customer).join(Review).filter(Review.restaurant == self).all()


class Customer(Base):
    __tablename__ = 'customers'  
    id = Column(Integer, primary_key=True)
    first_name = Column(String)  
    last_name = Column(String)  

    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship(
        'Restaurant', secondary='reviews', back_populates='customers')

    def reviews(self):
        return session.query(Review).filter_by(customer=self).all()

    def restaurants(self):
        return session.query(Restaurant).join(Review).filter(Review.customer == self).all()


class Review(Base):
    __tablename__ = 'reviews'  
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
 
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
 
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def restaurant(self):
        return self.restaurant

    def customer(self):
        return self.customer


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
