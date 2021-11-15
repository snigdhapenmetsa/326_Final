""" This is our final project """

from argparse import ArgumentParser
import sys

class Person:
    """Instantiates a person.
    
    Attributes:
        name (string)
        balance (int)
        membership (boolean)
    """
    def __init__(self, name, balance, membership):
        """
        self.people = []
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                people = {}
                
                name, balance, membership = line.split("\t")
                
                people["name"] = name
                people["balance"] = float(balance)
                if membership == "true":
                    people["membership"] = True
                elif membership == "false":
                    people["membership"] = False
                
                self.people.append(people)
        """
        
        self.name = name
        self.balance = balance
        self.membership = membership
            
    def membership_list(self):
        """
        for person in self.people:
            if person.membership is True:
        """
        if self.membership == "silver":
            return 10
        elif self.membership == "gold":
            return 15
        elif self.membership == "platinum":
            return 20
    
class Conversion_Shop:
    """Class for converting currency."""
    
    def __init__(self, filepath):
        self.people = {}
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                #people = {}
                
                self.name, self.balance, self.membership = line.split(",")
                self.balance = int(self.balance)
                
                self.people[self.name] = (self.balance, self.membership)
 
    def get_person(self, name):
        if name not in self.people:
            raise KeyError
       
        person = Person(name, self.people[name][0], self.people[name][1])
        return person
    
    def conversion(self):
        pass
    
def transaction(customer):
    print(f"{customer.name} has {customer.balance} balance.")
    #while(customer.balance > 0):
     #   print(f"{customer.name} has {customer.balance} balance.")
      #  print()
    
def main(filename, customer_name):
    
    person = Conversion_Shop(filename)
    customer = person.get_person(customer_name)
    #person.get_person(name)
    transaction(customer)

def parse_args(arglist):

    parser = ArgumentParser()
    parser.add_argument("filename",
                        help="path to CSV file containing people")
    parser.add_argument("name", help="name of customer")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.name)
