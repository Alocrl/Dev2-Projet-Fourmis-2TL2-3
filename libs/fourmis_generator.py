
class Ant:
    """Main class for the ants"""
    def __init__(self, life, type):
        self.life = life
        self.type = type

    @property
    def everyDayLife(self):
        """Delete a day in the life of the ant and return True if she has less than 1 life"""
        self.life -= 1
        return self.life <= 0

class AntWorker (Ant):
    """Class for a worker ant"""

    def __init__(self, life, type, nbrFoodCollectPerDay):
        super().__init__(life, type)
        self.nbrFoodCollectPerDay = nbrFoodCollectPerDay

    def __str__(self):
        return f"The worker ant have {self.life} lives left, she product {self.nbrFoodCollectPerDay} food per day."

class AntQween (Ant):
    """Class for a qween ant"""
    def __init__(self, life, type, nbrEgsPerDay):
        super().__init__(life, type)
        self.nbrEgsPerDay = nbrEgsPerDay
    def __str__(self):
        return f"The qween ant have {self.life} lives left, she product {self.nbrEgsPerDay} eggs per day."

class AntSolder (Ant):
    """Class for a solder ant"""
    def __init__(self, life, type, damage):
        super().__init__(life, type)
        self.damage = damage

    def __str__(self):
        return f"The solder ant have {self.life} lives left, she can attack with {self.damage} domages per hit."




def generateColloniewWorkers(nbrworkers, life, type, nbrFoodCollectPerDay):
    """Generate and return some ant workers"""
    workers = {}
    for i in range(nbrworkers):
        workers[i] = AntWorker(life, type, nbrFoodCollectPerDay)
    return workers

def generateColloniewQween(life, type, nbrEgsPerDay):
    """Generate and return a ant qween"""
    qween = {}
    qween[0] = AntQween(life, type, nbrEgsPerDay)
    return qween

def generateColloniewsoldiers(nbrworkers, life, type, damage):
    """Generate and return some ant soldiers"""
    soldiers = {}
    for i in range(nbrworkers):
        soldiers[i] = AntSolder(life, type, damage)
    return soldiers

def generateCollonie(typeAntProprety, type, nbrworkers, nbrsoldiers, food):
    """Generate and return a collonie of ants base on the type of ants"""

    workers = generateColloniewWorkers(nbrworkers, typeAntProprety["worker"]["life"], type, typeAntProprety["worker"]["nbrFoodCollectPerDay"])
    qween = generateColloniewQween(typeAntProprety["qween"]["life"], type, typeAntProprety["qween"]["nbrEgsPerDay"])
    soldiers = generateColloniewsoldiers(nbrsoldiers, typeAntProprety["soldier"]["life"], type, typeAntProprety["soldier"]["damage"])

    return {"antProprety": typeAntProprety, "type" : type, "workers" : workers, "qween" : qween, "soldiers" : soldiers, "food" : food}