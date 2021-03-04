"""Randomly pick customer and print customer info"""

import customers 
from random import choice


def get_random_customer(customers):
    """
    Choice a person from customer list 
    """
    lucky_customer = choice(customers)

    return lucky_customer


def print_winner():
    """ Run and print the winner
    """

    lst_customers = customers.get_customers_from_file("customers.txt")
    winner = get_random_customer(lst_customers)

    print (f"Name: {winner.name}")
    print (f"Email: {winner.email}")
    print (f"Street: {winner.street}")
    print (f"City: {winner.city}")
    print (f"Zipcode: {winner.zipcode}")


if __name__ == '__main__':
    print_winner()