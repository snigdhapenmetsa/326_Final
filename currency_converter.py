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
    """Class for converting currency."""
     
    def __init__(self, filepath):
        pass