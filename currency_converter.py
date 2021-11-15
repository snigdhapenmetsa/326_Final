from argparse import ArgumentParser
import sys

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
    
    def __init__(self, person_file, item_file):
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
    
def main(person_file, item_file):
    currency_shop = Currency_Shop(person_file, item_file)
    print(currency_shop.people)
    print(currency_shop.items)
            
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("person_file", help="path to txt file containing people")
    parser.add_argument("item_file", help="path to txt file containing items")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.person_file, args.item_file)