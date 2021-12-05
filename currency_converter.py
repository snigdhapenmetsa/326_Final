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
    """
    
    def __init__(self, name, balance, membership):
        self.name = name
        self.balance = balance
        self.membership = membership
        
    def membership_list(self):
        """Gives discount depending on customer's membership status.
        
        Args:
            items_purchased (list): items purchased by customer.
        
        Returns:
            Discount (int): represents the discout a customer will receive with purchase.
        """
        
        if self.membership == "silver":
            return 10
        elif self.membership == "gold":
            return 15
        elif self.membership == "platinum":
            return 20
        else:
            return 0
        
    def buy_ticket(self):
        """A plane ticket from the Team Dunder Airport costs $200. This cost can 
        be converted to the desired currency of the customer, and the total 
        is subtracted from their balance.
        """
        ticket_cost = 200.0
        cost = ticket_cost * self.membership_list()
        if self.balance >= ticket_cost:
            self.balance -= ticket_cost
            print(self.balance)
        else:
            raise ValueError("Insufficient funds!")
        
    def __repr__(self):
        return f"Person({self.name}, {self.balance}, {self.membership})"

class Currency_Shop:
    """A shop in which customers can use any currency of their choosing.
    
    Attributes:
        people (dictionary): reads txt and makes a dictionary of people with
            the persons name as the key and their balance and membership as the
            values
        items (list of str): reads txt file and makes a list of items that 
            customers can purchase from the shop
    """
    
    def __init__(self, person_file, url):
        self.people = {}
        
        with open(person_file, "r", encoding="utf-8") as f:
            for line in f:
                
                self.name, self.balance, self.membership = line.split(",")
                self.balance = float(self.balance)
                self.membership = self.membership.strip()
                
                self.people[self.name] = (self.balance, self.membership)
        
        values = values = requests.get(url).json()
        self.rates = values["rates"] 
                
    def converter(self, toCurrency, balance): 
        """Converts customer's balance originally in USD to desired currency
        
        Args: 
            toCurrency (str) = the currency which user wants to convert to 
            balance (float) = the members balance"""
        og_balance = self.people[self.name][0]
        balance = balance/self.rates["USD"]
        balance = round(balance*self.rates[toCurrency], 2)
        print(f"{self.name}'s balance of {og_balance} in USD is {balance} in {toCurrency}")
                
    def get_person(self, name):
        if name not in self.people:
            raise KeyError
        
        person = Person(name, self.people[name][0], self.people[name][1])
        return person
    
def main(person_file, url):
    currency_shop = Currency_Shop(person_file, url)
    print(currency_shop.people)
    print(currency_shop.get_person("Abby Miller"))
    print(currency_shop.converter("EUR", currency_shop.balance))
            
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("person_file", help="path to txt file containing people")
    parser.add_argument("url", help="url for conversion rates")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.person_file, args.url)