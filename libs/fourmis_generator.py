from libs.nouriture_generator import generate_food
import time

class Ant:
    """Main class for the ants"""

    def __init__(self, life: int, species: str):
        """ Initialize the Ant class

        PRE :   - life (int) : tells you how many live the ant have.
                - species (str) : tells you what type of ant it is.
        POST : initalize the self.live & self.spécies.
        """
        self.life = life
        self.species = species

    @property
    def every_day_life(self):
        """ Delete a day in the life of the ant

        PRE : /
        POST : Do minus 1 to the number live the ant have and return True if the ant she has less than 1 life,
                or False is the ant have more than 1 live.
        """
        self.life -= 1
        return self.life <= 0


class AntWorker(Ant):
    """Class for a worker ant"""


    def __init__(self, life: int, species: str, nbr_food_collect_per_day: int):
        """ Initialize the antWorker class

        PRE :   - life (int) : tells you how many live the ant have.
                - species (str) : tells you what type of ant it is.
                - nbr_food_collect_per_day (int) : tell the number of food the ant can collect per day.
        POST : initalize the self.nbr_food_collect_per_day & initalize the super().__init__ variables.
        """
        super().__init__(life, species)
        self.nbr_food_collect_per_day = nbr_food_collect_per_day

    def __str__(self):
        """ stingify the data of the antWorker

        PRE : /
        POST : Return the data of the antWorker in a string.
        """
        return f"The worker ant have {self.life} lives left, she product {self.nbr_food_collect_per_day} food per day."


class Antqween(Ant):
    """Class for a qween ant"""

    def __init__(self, life: int, species: str, nbr_eggs_per_day: int):
        """ Initialize the Antqween class

        PRE :   - life (int) : tells you how many live the ant have.
                - species (str) : tells you what type of ant it is.
                - nbr_eggs_per_day (int) : tell the number of eggs the qween product per day.
        POST : initalize the self.nbr_eggs_per_day & initalize the super().__init__ variables.
        """
        super().__init__(life, species)
        self.nbr_eggs_per_day = nbr_eggs_per_day

    def __str__(self):
        """ stingify the data of the Antqween

        PRE : /
        POST : Return the data of the Antqween in a string.
        """
        return f"The qween ant have {self.life} lives left, she product {self.nbr_eggs_per_day} eggs per day."


class AntSolder(Ant):
    """Class for a solder ant"""

    def __init__(self, life: int, species: str, damage: int):
        """ Initialize the AntSolder class

        PRE :   - life (int) : tells you how many live the ant have.
                - species (str) : tells you what type of ant it is.
                - damage (int) : tell the number of domage the ant can do in one hit.
        POST : initalize the self.damage & initalize the super().__init__ variables.
        """
        super().__init__(life, species)
        self.damage = damage

    def __str__(self):
        """ Stingify the data of the AntSolder

        PRE : /
        POST : Return the data of the AntSolder in a string.
        """
        return f"The solder ant have {self.life} lives left, she can attack with {self.damage} domages per hit."


class Larva(Ant):
    """Class for a Larva"""
    def __init__(self, life: int, species: str):
        """ Initialize the Larva class

        PRE :   - life (int) : tells you how many live the Larva have before hatch.
                - species (str) : tells you what type of ant it is.
        POST : initalize the self.state & initalize the super().__init__ variables.
        """
        super().__init__(life, species)
        self.state = "egg"

    @property
    def update_state(self):
        """ Define larva state

        PRE : /
        POST : Change the larva state to an "larva" if his live before hatch is under o equal to 5.
        """
        if self.life <= 5:
            self.state = "larva"
        pass

    def __str__(self):
        """ stingify the data of the Larva

        PRE : /
        POST : Return the data of the Larva in a string.
        """
        return f"The larva have {self.life} days left before hatch, he is currently an {self.state}."



def generate_colony_workers(nbrworkers: int, life: int, species: str, nbr_food_collect_per_day: int):
    """ Generate and return some ant workers

    PRE :   - nbrworkers (int) : tells you the number of workers object the dict in return need to have.
            - life (int) : tells how many life the AntWorker have at the beggin of his live.
            - species (str) : tells you what type of ant it is.
            - nbr_food_collect_per_day (int) : tell you how many food can the worker collect per day.
    POST : return a dict with all the object with the class AntWorkers.
        exmeple :
            - {0: <libs.fourmis_generator.AntWorker object at 0x01932AB0>, 1: <libs.fourmis_generator.AntWorker object at 0x01932AD0>}
    """
    workers = {}
    for i in range(nbrworkers):
        workers[i] = AntWorker(life, species, nbr_food_collect_per_day)
    return workers


def generate_colony_qween(life: int, species: str, nbr_eggs_per_day: int):
    """ Generate and return à ant qween

    PRE :   - life (int) : tells how many life the qween  have at the beggin of his live.
            - species (str) : tells you what type of ant it is.
            - nbr_eggs_per_day (int) : tell you how many eggs can the qween porduce per day.
    POST : return a dict with the qween object that have the class Antqween.
        exmeple :
            - {0: <libs.fourmis_generator.Antqween object at 0x02633750>}
    """
    qween = {0: Antqween(life, species, nbr_eggs_per_day)}
    return qween


def generate_colony_soldiers(nbrSoldiers: int, life: int, species: str, damage: int):
    """ Generate and return some ant soldiers

    PRE :   - nbrSoldiers (int) : tells you the number of soldiers object the dict in return need to have.
            - life (int) : tells how many life the AntSoldiers have at the beggin of his live.
            - species (str) : tells you what type of ant it is.
            - damage (int) : tell you how many domange can the soldiers do in one hit.
    POST : return a dict with all the objects with the class Antsoldiers.
        exmeple :
            - {0: <libs.fourmis_generator.AntSolder object at 0x02663770>, 1: <libs.fourmis_generator.AntSolder object at 0x02663790>}
    """
    soldiers = {}
    for i in range(nbrSoldiers):
        soldiers[i] = AntSolder(life, species, damage)
    return soldiers

def generate_colony_larva(nbrLarva: int, life: int, species: str):
    """ Generate and return some larva

    PRE :   - nbrSoldiers (int) : tells you the number of larva object the dict in return need to have.
            - life (int) : tells how many life the larva have before hatch.
            - species (str) : tells you what type of ant it is.
    POST : return a dict with all the objects with the class larva.
        exmeple :
            - {0: <libs.fourmis_generator.Larva object at 0x01F33A90>, 1: <libs.fourmis_generator.Larva object at 0x01F4E1F0>}
    """
    larva = {}
    for i in range(nbrLarva):
        larva[i] = Larva(life, species)
    return larva


def generate_colony(type_ant_proprety: dict, species: str, nbrworkers: int, nbrsoldiers: int, nbrfood: int, nbrLarva: int=0):
    """ Generate and return a collonie of ants base on the type of ants

    PRE :   - type_ant_proprety (dict) : tells you the properties of an ant according to its type.
            - species (str) : tells you what type of ant it is.
            - nbrworkers (int) : tell you how many workers there are.
            - nbrsoldiers (int) : tell you how many soldiers there are.
            - nbrfood (int) : tell you how many food there are.
            - nbrLarva (int) : tell you how many larva there are.
    POST : return a dict with all the informations that the colony at the start need to have.
            The dict have 7 sub dict with all the information :
                - antProprety : all the property of the type of ant.
                - type : the name of the ant type.
                - workers : all the workers bjects.
                - qween : the qween objects.
                - soldiers : all the soldiers objects.
                - larva : all the larva objects.
                - food : the food object.
    """

    workers = generate_colony_workers(nbrworkers, type_ant_proprety["worker"]["life"], species,
                                      type_ant_proprety["worker"]["nbr_food_collect_per_day"])
    qween = generate_colony_qween(type_ant_proprety["qween"]["life"], species,
                                  type_ant_proprety["qween"]["nbr_eggs_per_day"])
    soldiers = generate_colony_soldiers(nbrsoldiers, type_ant_proprety["soldier"]["life"], species,
                                        type_ant_proprety["soldier"]["damage"])
    nourishment = generate_food(nbrfood)

    larva = generate_colony_larva(nbrLarva, type_ant_proprety["larva"]["life"], species)

    return {"antProprety": type_ant_proprety, "type": species, "workers": workers, "qween": qween, "soldiers": soldiers, "larva": larva,
            "food": nourishment}
