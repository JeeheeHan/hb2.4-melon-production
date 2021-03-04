"""Randomly pick customer and print customer info"""

import customers 
from random import choice
import sys

def get_random_customer(customers):
    """
    Choice a person from customer list 
    """
    lucky_customer = choice(customers)

    print (f"Name: {lucky_customer.name}")
    print (f"Email: {lucky_customer.email}")
    print (f"Street: {lucky_customer.street}")
    print (f"City: {lucky_customer.city}")
    print (f"Zipcode: {lucky_customer.zipcode}")





#call document in shell

filenames = "customers.txt"
#sys.argv[1:] was not working so putting direct file name

#Return a lucky customer
lst_customers = customers.get_customers_from_file(filenames)

winner = get_random_customer(lst_customers)
