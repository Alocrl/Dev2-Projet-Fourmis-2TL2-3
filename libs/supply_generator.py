import random
import json

#class to create a Supply
class Supply:

    def __init__(self,all_type_and_life: dict):
        """ Initialize the Food class

        PRE :   - all_type_and_life (dict) : is a dict with all the type of food and her quantity.

        POST : initalize the self.all_type_and_life.
        """

        for food_type, properties in all_type_and_life.items():
            if "nbr_life_eat" in properties:
                nbr_life_eat = properties["nbr_life_eat"]
                if not isinstance(nbr_life_eat, int) or isinstance(nbr_life_eat, bool) :
                    raise ValueError("nbr_life_eat must be an integer.")
                elif nbr_life_eat < 1:
                    raise ValueError("nbr_life_eat must be greater than or equal to 1 for all food types.")
        self.all_type_and_life = all_type_and_life

    def check_supply(self):
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
            for food_name in list(self.all_type_and_life.keys()) :
                if self.all_type_and_life[food_name]["nbr_life_eat"] <= 1 :
                    del self.all_type_and_life[food_name]
                    return True
                else :
                    self.all_type_and_life[food_name]["nbr_life_eat"] -= 1
                    return True
    
    def add_food(self, nbr_collect: int):
        """ Add a certain number of food in the object

        PRE :   - nbre_nouriture (int) : tell you how many food have to be create.

        POST : return nothing but add food to the object. The amount of food is chose with the param,
                and the type of food is randomely chosen in the JSON file.
        """

        try:
            with open("/Users/maxime/Documents/GitHub/Dev2-Projet-Fourmis-2TL2-3/data/eat_data.json") as file:
                all_data_eat = json.load(file)
        except IOError as e:
            print(f"IOERROR : {e}")

        for _ in range(nbr_collect) :
            type_food = random.choice(list(all_data_eat.keys()))
            if type_food not in self.all_type_and_life.keys():
                self.all_type_and_life[type_food] = {"nbr_life_eat":all_data_eat[type_food]["nbr_life_eat"]}
            else:
                self.all_type_and_life[type_food]["nbr_life_eat"] += all_data_eat[type_food]["nbr_life_eat"]
    
    def all_supply(self):
        """ Say how many food you have

        PRE : /

        POST : return the number of food you have in total (all the types of food are combine).
        """
        all_food = 0
        for i in self.all_type_and_life:
            all_food += self.all_type_and_life[i]["nbr_life_eat"]
        return all_food
    
    def all_type_in_supply(self):
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
        return f"here is the object of the class : {self.all_type_and_life}"

#function to generate supply
def generate_supply(nbre_nouriture: int):
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
        with open("/Users/maxime/Documents/GitHub/Dev2-Projet-Fourmis-2TL2-3/data/eat_data.json") as file:
            all_data_eat = json.load(file)
    except IOError as e:
        print(f"IOERROR : {e}")

    all_type_and_life_object = {}
    for _ in range(nbre_nouriture):
        type_food = random.choice(list(all_data_eat.keys()))
        if type_food not in all_type_and_life_object.keys():
            all_type_and_life_object[type_food] = {"nbr_life_eat":all_data_eat[type_food]["nbr_life_eat"]}
        else :
            all_type_and_life_object[type_food]["nbr_life_eat"] += all_data_eat[type_food]["nbr_life_eat"]
    allfood = Supply(all_type_and_life_object)
    return allfood

