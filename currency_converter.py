from argparse import ArgumentParser
import sys

class Person:
    """Instantiates a person.
    
    Attributes:
        name (string)
        balance (int)
        membership (boolean)
    """
    
    def __init__(self, filepath):
        self.people = {}
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                
                self.name, self.balance, self.membership = line.split(",")
                self.balance = float(self.balance)
                self.membership = self.membership.strip()
                
                self.people[self.name] = (self.balance, self.membership)
                print(self.name, self.balance, self.membership)

class Currency_Shop:
    """Class for converting currency.
    
    Attributes:
        items (list of str)
    """
    
    def __init__(self, filepath):
        self.items = list()
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f: 
                self.items.append(line.strip())
    
def main(person_file, item_file):
    person = Person(person_file)
    item = Currency_Shop(item_file)
            
def parse_args(arglist):

    parser = ArgumentParser()
    parser.add_argument("person_file", help="path to txt file containing people")
    parser.add_argument("item_file", help="path to txt file containing items")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.person_file, args.item_file)