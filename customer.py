from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    cust_id = Column(Integer, Sequence('cust_id_seq'), primary_key=True)
    cust_fname = Column(String)
    cust_lname = Column(String)

    reviews = relationship('Review', back_populates='customer')


    def reviews(self):
        return self.reviews  

    def restaurants(self):
        return [review.restaurant for review in self.reviews]  

    def full_name(self):
        return f"{self.cust_fname} {self.cust_lname}"  

    def favorite_restaurant(self):
        return max(self.reviews, key=lambda review: review.star_rating).restaurant 

    def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()