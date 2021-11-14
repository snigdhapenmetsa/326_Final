""" This is our final project """

class Person:
    """Instantiates a person
    
    Attributes:
        name (string)
        balance (int)
        membership (boolean)
    """
    def __init__(self, filepath,name, balance, membership):
        
        people = list()
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                city = {}
                
                name, lat, lon, pop = line.split("\t")
                
                city["name"] = name
                city["lat"] = float(lat)
                city["lon"] = float(lon)
                city["pop"] = int(pop)
                
                self.cities.append(city)
        
        for line in F:
            self.name = name
            self.balance = balance
            self.membership = membership
            
            self.cities = []
        
                
        sorted_cities = sorted(self.cities, key=lambda city: get_dist((lat, lon), 
            (city["lat"],city["lon"])))
        filtered_cities = [city for city in sorted_cities if city["pop"] >= 
            min_population]
        
        return filtered_cities[:n]
        
    def membership_list(self):
        
        for person in people:
            if self.membership is True:
            
    
class Convert:
    """Class for converting currency."""

    def USD_EUR():
        pass
    
def main(filename, a1_name, a2_name, pause=2.0):
    """ Create two aardvarks from the aardvark catalog and stage a battle.
    
    Args:
        filename (str): A file with other data.
        a1_name (str): The name of the first aardvark, taken from the file.
        a2_name (str): The name of the second aardvark, taken from the file.
        pause (float): an amount of time in seconds to pause between attacks in
            a battle. Allows the user time to read the outcome of each attack.
            Default: 2.0.
        
    Side effects:
        See battle().
    """
    catalog = Catalog(filename)
    a1 = catalog.get_aardvark(a1_name)
    a2 = catalog.get_aardvark(a2_name)
    if a1_name == a2_name:
        a1.name += " 1"
        a2.name += " 2"
    battle(a1, a2, pause)