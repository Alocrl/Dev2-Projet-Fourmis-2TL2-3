import random
import json

#class to create a food
class Food:
    def __init__(self,all_type_and_life):
        self.all_type_and_life = all_type_and_life # = quantity d'energie
    
    def check_class(self):
        if not self.all_type_and_life:
            return False
        else:
            return True
        
    def del_food(self):
        if not self.all_type_and_life:
            return False
        else:
            all_key = len(list(self.all_type_and_life.keys()))
            for foodName in list(self.all_type_and_life.keys()) :
                if self.all_type_and_life[foodName] <= 0 :
                    del self.all_type_and_life[foodName]
                else :
                    self.all_type_and_life[foodName] -= 1
                    return True
            return False

            
    def add_food(self, nbr_collect):
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
        all_food = 0
        for i in self.all_type_and_life:
            all_food += self.all_type_and_life[i] 
        return all_food
    
    def __str__(self):
       return f"here's the object of the class : {self.all_type_and_life}"




#function to generate food
def generate_food(nbre_nouriture):
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
    print(all_type_and_life_object)
    allfood = Food(all_type_and_life_object)
    return allfood

