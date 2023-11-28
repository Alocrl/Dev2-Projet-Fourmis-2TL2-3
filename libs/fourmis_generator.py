from libs.nouriture_generator import generate_food


class Ant:
    """Main class for the ants"""

    def __init__(self, life, species):
        self.life = life
        self.species = species

    @property
    def every_day_life(self):
        """Delete a day in the life of the ant and return True if she has less than 1 life"""
        self.life -= 1
        return self.life <= 0


class AntWorker(Ant):
    """Class for a worker ant"""

    def __init__(self, life, species, nbr_food_collect_per_day):
        super().__init__(life, species)
        self.nbr_food_collect_per_day = nbr_food_collect_per_day

    def __str__(self):
        return f"The worker ant have {self.life} lives left, she product {self.nbr_food_collect_per_day} food per day."


class Antqween(Ant):
    """Class for a qween ant"""

    def __init__(self, life, species, nbr_eggs_per_day):
        super().__init__(life, species)
        self.nbr_eggs_per_day = nbr_eggs_per_day

    def __str__(self):
        return f"The qween ant have {self.life} lives left, she product {self.nbr_eggs_per_day} eggs per day."


class AntSolder(Ant):
    """Class for a solder ant"""

    def __init__(self, life, species, damage):
        super().__init__(life, species)
        self.damage = damage

    def __str__(self):
        return f"The solder ant have {self.life} lives left, she can attack with {self.damage} domages per hit."


class Larva(Ant):
    def __init__(self, life, species):
        super().__init__(life, species)
        self.state = "egg"

    @property
    def update_state(self):
        """define larva state"""
        if self.life <= 5:
            self.state = "larva"
        pass


def generate_colony_workers(nbrworkers, life, species, nbr_food_collect_per_day):
    """Generate and return some ant workers"""
    workers = {}
    for i in range(nbrworkers):
        workers[i] = AntWorker(life, species, nbr_food_collect_per_day)
    return workers


def generate_colony_qween(life, species, nbr_eggs_per_day):
    """Generate and return a ant qween"""
    qween = {0: Antqween(life, species, nbr_eggs_per_day)}
    return qween


def generate_colony_soldiers(nbrworkers, life, species, damage):
    """Generate and return some ant soldiers"""
    soldiers = {}
    for i in range(nbrworkers):
        soldiers[i] = AntSolder(life, species, damage)
    return soldiers

def generate_colony_larva(nbrLarva, life, species):
    """generate and return some larva"""
    larva = {}
    for i in range(nbrLarva):
        larva[i] = Larva(life, species)
    return larva


def generate_colony(type_ant_proprety, species, nbrworkers, nbrsoldiers, nbrfood, nbrLarva=0):
    """Generate and return a collonie of ants base on the type of ants"""

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
