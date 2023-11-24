import random
import json

#add a json file with food types and their values 
try :
    with open("data/eat_data.json") as file :
        all_data_eat = json.load(file)
except IOError as e :
    print(f"IOERROR : {e}")

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
            all_key = list(self.all_type_and_life.keys())
            first_key = all_key[0]
            if self.all_type_and_life[first_key] <= 0 :
                del self.all_type_and_life[first_key]
            else :
                self.all_type_and_life[first_key] -= 1
            
            if not self.all_type_and_life:
                return False
            else :
                return True
            
    def add_food(self,nbr_collect):
        if not self.all_type_and_life:
            return 0
        all_key = list(self.all_type_and_life.keys())
        first_key = all_key[0]
        self.all_type_and_life[first_key] += all_data_eat[first_key]["nbr_life_eat"]
        
    def all_storage_food(self):
        all_food = 0
        for i in self.all_type_and_life:
            all_food += self.all_type_and_life[i] 
        return all_food
    
    def __str__(self):
       return f"here's the object of the class : {self.all_type_and_life}"

#function to generate food
def generate_food(nbre_nouriture):
    all_type_and_life_object = {}
    for index in range(nbre_nouriture):  
        type_food = random.choice(list(all_data_eat.keys()))
        if type_food not in all_type_and_life_object.keys() :
            all_type_and_life_object[type_food] = all_data_eat[type_food]["nbr_life_eat"]
        else :
            all_type_and_life_object[type_food] += all_data_eat[type_food]["nbr_life_eat"]
    allfood = Food(all_type_and_life_object)
    return allfood

