from argparse import ArgumentParser
import sys
import requests

rates = {}

class Person:
    """Creates person objects of which are customers who can shop at the store.
    
    Attributes:
        name (string): the name of a customer
        balance (int): the amount of money the customer has to spend
        membership (boolean): the membership plan a customer has
    """
    
    def __init__(self, name, balance, membership, items_purchased):
        self.name = name
        self.balance = balance
        self.membership = membership
        
    def membership_list(self):
        """Gives discount depending on if customer is a member, and which level.
        
        """
        self.items_purchased = items_purchased
        
    def membership_list(self):
        if self.membership == "silver":
            return 10
        elif self.membership == "gold":
            return 15
        elif self.membership == "platinum":
            return 20
        elif self.membership == "none":
            return 0

class Currency_Shop:
    """A shop in which customers can use any currency of their choosing.
    
    Attributes:
        people (dictionary): reads txt and makes a dictionary of people with
            the persons name as the key and their balance and membership as the
            values
        items (list of str): reads txt file and makes a list of items that 
            customers can purchase from the shop
    """
    
    def __init__(self, person_file, item_file, url):
        self.people = {}
        
        with open(person_file, "r", encoding="utf-8") as f:
            for line in f:
                
                self.name, self.balance, self.membership = line.split(",")
                self.balance = float(self.balance)
                self.membership = self.membership.strip()
                self.items_purchased = list()
                
                self.people[self.name] = (self.balance, self.membership, self.items_purchased)
        
        self.items = list()
        
        with open(item_file, "r", encoding="utf-8") as f:
            for line in f: 
                self.items.append(line.strip())
        
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
        
        person = Person(name, self.people[name][0], self.people[name][1], self.people[name][2])
        return person
    
def main(person_file, item_file, url):
    currency_shop = Currency_Shop(person_file, item_file, url)
    print(currency_shop.people)
    print(currency_shop.items)
    print(currency_shop.get_person("Abby Miller"))
            
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("person_file", help="path to txt file containing people")
    parser.add_argument("item_file", help="path to txt file containing items")
    parser.add_argument("url", help="url for conversion rates")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.person_file, args.item_file, args.url)