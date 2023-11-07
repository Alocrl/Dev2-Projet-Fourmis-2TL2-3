import random

class Ant :
    """class for an ant"""
    def __init__(self,type, sexe, life) :
        self.type = type
        self.sexe = sexe
        self.life = life

    @property
    def everyDayLife (self):
        """ delete a day in the life of the ant and return true if she have less than 1 live"""
        self.life -= 1
        if self.life <= 0 :
            return True
        else:
            return False

    def __str__(self) :
        return f"type : {self.type} - sexe : {self.sexe} - vie : {self.life}"


def generateAnts(nombre_fourmis):
    """"return a dictionary containing the objects created with the Ants class"""

    objectAllAnts = {}
    antType = random.choice(["Atta", "Camponotus", "Formica", "Formica", "Solenopsis"])
    antSexe = ["M", "F"]
    antLife = range(23)

    for i in range(nombre_fourmis) :
        sexe = random.choice(antSexe)
        nbrLife = random.choice(antLife)

        objectAllAnts[i] = Ant(antType, sexe, nbrLife)

    return objectAllAnts