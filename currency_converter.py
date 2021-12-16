"""Simulates an online shop using a currency converter."""

from argparse import ArgumentParser
import sys
import requests

rates = {}

class Person:
    """Creates person objects of which are customers who can shop at the store.
    
    Attributes:
        name (string): the name of a customer
        balance (int): the amount of money the customer has to spend
        membership (string): the membership plan a customer has
        to_country (string): 3 uppercase letters signifying the country the 
            person wants to buy a plane ticket to
    """
    
    def __init__(self, name, balance, membership, to_country):
        self.name = name
        self.balance = balance
        self.membership = membership
        self.to_country = to_country
        
    def membership_list(self):
        """Gives discount depending on customer's membership status.
        
        Args:
            items_purchased (list): items purchased by customer.
        
        Returns:
            float: represents the discout a customer will receive with purchase.
        """
        
        if self.membership == "silver":
            return .10
        elif self.membership == "gold":
            return .15
        elif self.membership == "platinum":
            return .20
        else:
            return 0
        
    def buy_ticket(self):
        """A plane ticket from the Team Dunder Airport costs $200. This cost can 
            be converted to the desired currency of the customer, and the total 
            is subtracted from their balance.
            
        Raises:
            ValueError: if the person's balance is less than the cost of a ticket,
                a ValueError is raised.
        """
        ticket_cost = 200.0
        cost = ticket_cost * (1 - self.membership_list())
        
        if self.balance >= cost:
            self.balance -= cost
            
        else:
            raise ValueError("Insufficient funds!")
        
    def __repr__(self):
        return f"Person({self.name}, {self.balance}, {self.membership}," 
    "{self.to_country})"

class Currency_Shop:
    """A shop in which customers can use any currency of their choosing.
    
    Attributes:
        people (dictionary): reads txt file and makes a dictionary of people with
            the persons name as the key and their balance, membership, and the 
            the country they want a plane ticket to as the values.
    """
    
    def __init__(self, person_file, url):
        """Assigns attributes, reads a list of people from a .txt file, and 
            gets conversion rates from an API for the currency converter.

        Args:
            person_file (string): the filepath to a .txt file with information
                about people who can buy a plane ticket from the shop.
            url (string): a url to the API with conversion rates for the 
                currency converter.
        """
        self.people = {}
        
        with open(person_file, "r", encoding="utf-8") as f:
            for line in f:
                
                self.name, self.balance, self.membership, self.to_country = \
                    line.strip().split(",")
                self.balance = float(self.balance)
                self.membership = self.membership.strip()
                
                self.people[self.name] = (self.balance, self.membership, 
                                          self.to_country)
        
        values = requests.get(url).json()
        self.rates = values["rates"] 
                
    def converter(self, name, person_balance): 
    # This method is reliant on  source code from 
    # https://www.geeksforgeeks.org/currency-converter-in-python/
    # I changed it to fit to our problem statement by modifying the variables in 
    # the calculations
        """Converts customer's balance originally in USD to desired currency
        Args: 
            name (str): The person's name whose balance will be converted
            person_balance (float): the person's balance
            
        Returns:
            float: the person's balance, converted into the currency of the 
                desired country
        """
        balance = person_balance/self.rates["USD"]
        balance = round(balance * self.rates[self.people.get(name)[2]], 2)
        return balance
                
    def get_person(self, name):
        """Instantiates a Person object.

        Args:
            name (string): the name of a person.

        Raises:
            KeyError: if the name provided is not part of the people list, raise 
            a KeyError.

        Returns:
            object: a Person object of a person defined by the txt file
        """
        if name not in self.people:
            raise KeyError
        
        person = Person(name, self.people[name][0], self.people[name][1], 
                        self.people[name][2])
        return person
    
def main(person_file, name):
    """Prints customer's original balance, the country in which they are visiting,
        their balance after purhcasing the ticket, and their balance in the
        currency of the country they are visiting.
    
    Args: 
        person_file (string): the filepath to a .txt file with information
            about people who can buy a plane ticket from the shop.
        name (string): the name of a person.
    
    Side effects: 
        Prints information to the console.
    """
   access_key = "a702f302693756a5c8c44b988f472fc6"
   url = str.__add__('http://data.fixer.io/api/latest?access_key=', access_key)
   currency_shop = Currency_Shop(person_file, url)
   person = currency_shop.get_person(name)
   print(f"{person.name}'s current balance is {person.balance} in USD.")
   person.buy_ticket()
   print(f"{person.name} purchased a plane ticket to {person.to_country.strip()}."
         f" Their current balance is {person.balance} in USD.")
   print(f"In {person.to_country.strip()}, {person.name}'s balance is" + 
         "{currency_shop.converter(person.name,person.balance)}")
            
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("person_file", help="path to txt file containing people")
    parser.add_argument("name", help="Name of person to get data for")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.person_file, args.name)