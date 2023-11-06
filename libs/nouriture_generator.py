import random
class Food :
    def __init__(self, type) :
        self.type = type

def generateFood(nbre_nouriture) :
    """"return a dictionary containing the objects created with the Food class """

    objectAllFood = {}
    foodType = ["fraise", "bannane", "pomme", "noisette", "graine"]


    for index in range(nbre_nouriture) :
        food = random.choice(foodType)
        objectAllFood[index] = Food(food)
    
    return objectAllFood