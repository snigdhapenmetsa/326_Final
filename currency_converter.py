class Person:
    """Instantiates a person.
    
    Attributes:
        name (string)
        balance (int)
        membership (boolean)
    """
    def __init__(self, name, balance, membership):
        self.name = name
        self.balance = balance
        self.membership = membership

class Currency_Shop:
    """Class for converting currency.
    
    Attributes:
        filepath (str)
    """
     
    def __init__(self, filepath):
        self.people = {}
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                
                self.name, self.balance, self.membership = line.split(",")
                self.balance = float(self.balance)
                self.membership = self.membership.strip()
                
                self.people[self.name] = (self.balance, self.membership)