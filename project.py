""" This is our final project """

class Person:
    """Instantiates a person
    
    Attributes:
        name (string)
        balance (int)
        membership (boolean)
    """
    def __init__(self, filepath):
        self.people = []
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                people = {}
                
                name, balance, membership = line.split("\t")
                
                people["name"] = name
                people["balance"] = float(balance)
                if membership is "true":
                    people["membership"] = True
                elif membership is "false":
                    people["membership"] = False
                
                self.people.append(people)
        
    def membership_list(self):
        
        for person in self.people:
            if self.membership is True:
            
    
class Conversion_Shop:
    """Class for converting currency."""

    def USD_EUR():
        pass