import random

class Anthill:
    """Class for an anthill"""

    def __init__(self, type):
        self.type = type

class Ant(Anthill):
    """Class for an ant"""

    def __init__(self, type, sexe, life):
        super().__init__(type)
        self.sexe = sexe
        self.life = life

    @property
    def everyDayLife(self):
        """Delete a day in the life of the ant and return True if she has less than 1 life"""
        self.life -= 1
        return self.life <= 0

    def __str__(self):
        return f"type: {self.type} - sexe: {self.sexe} - vie: {self.life}"

def generateAnts(nombre_fourmis):
    """Return a dictionary containing the objects created with the Ant class"""
    objectAllAnts = {}
    antTypes = ["Atta", "Camponotus", "Formica", "Formica", "Solenopsis"]
    antSexe = ["M", "F"]
    antLife = list(range(23))

    for i in range(nombre_fourmis):
        antType = random.choice(antTypes)
        sexe = random.choice(antSexe)
        nbrLife = random.choice(antLife)
        objectAllAnts[i] = Ant(antType, sexe, nbrLife)

    return objectAllAnts
