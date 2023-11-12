import random


class Food:
    def __init__(self, species):
        self.species = species


def generate_food(nbre_nouriture):
    """"return a dictionary containing the objects created with the Food class """

    object_all_food = {}
    food_type = ["fraise", "bannane", "pomme", "noisette", "graine"]

    for index in range(nbre_nouriture):
        food = random.choice(food_type)
        object_all_food[index] = Food(food)

    return object_all_food
