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


class AntQueen(Ant):
    """Class for a queen ant"""

    def __init__(self, life, species, nbr_eggs_per_day):
        super().__init__(life, species)
        self.nbr_eggs_per_day = nbr_eggs_per_day

    def __str__(self):
        return f"The queen ant have {self.life} lives left, she product {self.nbr_eggs_per_day} eggs per day."


class AntSolder(Ant):
    """Class for a solder ant"""

    def __init__(self, life, species, damage):
        super().__init__(life, species)
        self.damage = damage

    def __str__(self):
        return f"The solder ant have {self.life} lives left, she can attack with {self.damage} domages per hit."


def generate_colony_workers(nbrworkers, life, species, nbr_food_collect_per_day):
    """Generate and return some ant workers"""
    workers = {}
    for i in range(nbrworkers):
        workers[i] = AntWorker(life, species, nbr_food_collect_per_day)
    return workers


def generate_colony_queen(life, species, nbr_eggs_per_day):
    """Generate and return a ant queen"""
    queen = {0: AntQueen(life, species, nbr_eggs_per_day)}
    return queen


def generate_colony_soldiers(nbrworkers, life, species, damage):
    """Generate and return some ant soldiers"""
    soldiers = {}
    for i in range(nbrworkers):
        soldiers[i] = AntSolder(life, species, damage)
    return soldiers


def generate_colony(type_ant_proprety, species, nbrworkers, nbrsoldiers, food):
    """Generate and return a collonie of ants base on the type of ants"""

    workers = generate_colony_workers(nbrworkers, type_ant_proprety["worker"]["life"], species,
                                      type_ant_proprety["worker"]["nbr_food_collect_per_day"])
    queen = generate_colony_queen(type_ant_proprety["queen"]["life"], species,
                                  type_ant_proprety["queen"]["nbr_eggs_per_day"])
    soldiers = generate_colony_soldiers(nbrsoldiers, type_ant_proprety["soldier"]["life"], species,
                                        type_ant_proprety["soldier"]["damage"])

    return {"antProprety": type_ant_proprety, "type": species, "workers": workers, "queen": queen, "soldiers": soldiers,
            "food": food}
