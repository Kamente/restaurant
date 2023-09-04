from app import session, Restaurant, Customer, Review

# insertion of data into the database tables
restaurant1 = Restaurant(name="Cratex", price=3)
restaurant2 = Restaurant(name="Pronto", price=2)
restaurant3 = Restaurant(name="Kilimanjaro", price=4)


customer1 = Customer(first_name="Kamente", last_name="Justin")
customer2 = Customer(first_name="Karter", last_name="John")
customer3 = Customer(first_name="Kim", last_name="Allison")


review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)
review3 = Review(star_rating=3, restaurant=restaurant3, customer=customer3)

# adding all the data into the respective tables
session.add_all([restaurant1, restaurant2, restaurant3, customer1, customer2, customer3, review1, review2, review3])
session.commit()


session.close()
