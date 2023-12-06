import random
import json


#class to create a food
class Food:
    def __init__(self,all_type_and_life: dict):
        """ Initialize the Food class

        PRE :   - all_type_and_life (dict) : is a dict with all the type of food and her quantity.

        POST : initalize the self.all_type_and_life.
        """
        self.all_type_and_life = all_type_and_life # = quantity d'energie
    
    def check_class(self):
        """ Check class

        PRE : /

        POST :  return True if the class have been created.
                return False if the class havent been created.
        """
        if not self.all_type_and_life:
            return False
        else:
            return True
        
    def del_food(self):
        """ Delete à food

        PRE : /

        POST : The methode will delete à food, if he can delete one then he will return True.
                In the other case (there is no food left), then he will return False.
        """

        if not self.all_type_and_life:
            return False
        else:
            len(list(self.all_type_and_life.keys()))
            for foodName in list(self.all_type_and_life.keys()) :
                if self.all_type_and_life[foodName] <= 0 :
                    del self.all_type_and_life[foodName]
                else :
                    self.all_type_and_life[foodName] -= 1
                    return True
            return False

            
    def add_food(self, nbr_collect: int):
        """ Add a certain number of food in the object

        PRE :   - nbre_nouriture (int) : tell you how many food have to be create.

        POST : return nothing but add food to the object. The amount of food is chose with the param,
                and the type of food is randomely chosen in the JSON file.
        """
        if not self.all_type_and_life:
            return 0

        try:
            with open("data/eat_data.json") as file:
                all_data_eat = json.load(file)
        except IOError as e:
            print(f"IOERROR : {e}")

        for i in range(nbr_collect) :
            type_food = random.choice(list(all_data_eat.keys()))
            if type_food not in self.all_type_and_life.keys():
                self.all_type_and_life[type_food] = all_data_eat[type_food]["nbr_life_eat"]
            else:
                self.all_type_and_life[type_food] += all_data_eat[type_food]["nbr_life_eat"]
        
    def all_storage_food(self):
        """ Say how many food you have

        PRE : /

        POST : return the number of food you have in total (all the types of food are combine).
        """
        all_food = 0
        for i in self.all_type_and_life:
            all_food += self.all_type_and_life[i] 
        return all_food
    
    def all_type_food(self):
        """ Say how many type of food you have.

        PRE : /

        POST : return the number of food types
        """

        return len(self.all_type_and_life)
    
    def __str__(self):
        """ Stingify the data of the food class

        PRE : /

        POST : Return the data of the food class in a string.
        """
        return f"here's the object of the class : {self.all_type_and_life}"




#function to generate food
def generate_food(nbre_nouriture: int):
    """ Generate the food

    PRE :   - nbre_nouriture (int) : tell you how many food have to be create.

    POST : return a dict with the different type of food that are randomely chosen in the JSON file.
            The number of food that have to be created is chose with  the param : "nbre_nouriture".
            Each food that is created equals a quantity of food that is different of each other (carrotes=2, bannane=5),
            that is why the "nbre_nouriture" and the sum of all the nurriture in the object is not equal.
        exmeple :
            - {'carotte': 774, 'banane': 266, 'fraise': 452, 'feuille': 118, 'citrouille': 1400,
                'graine': 131, 'tomate': 476, 'salade': 117}
    """

    # add a json file with food types and their values
    try:
        with open("data/eat_data.json") as file:
            all_data_eat = json.load(file)
    except IOError as e:
        print(f"IOERROR : {e}")

    all_type_and_life_object = {}
    for index in range(nbre_nouriture):  
        type_food = random.choice(list(all_data_eat.keys()))
        if type_food not in all_type_and_life_object.keys() :
            all_type_and_life_object[type_food] = all_data_eat[type_food]["nbr_life_eat"]
        else :
            all_type_and_life_object[type_food] += all_data_eat[type_food]["nbr_life_eat"]
    allfood = Food(all_type_and_life_object)
    return allfood

