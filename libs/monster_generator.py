import random




class Monster:
    """Class for Monster

        par : Gaetan Carbonnelle
        le : 30/11/2022

    """

    def __init__(self, domages: int=2, name: str="no_name", life: int=100 ):
        """ Initialize the Monster class

        PRE :   - domages (int) : tells you how many domages the monster have.
                - name (str) : tells you the name of the monster.
                - life (int) : tell you the life the monster have
        POST : initalize the self.live & self.domages & self.live.
                You can't have domanges less that are less than 0 and life that is lesse than 1
        """

        #the monster can't have a négative domage
        if domages < 0 :
            raise ValueError("You cant have a monster with less than 0 domages")
        self.domages = domages
        self.name = name

        #the monster can't have a negative live or equal to 0
        if life < 1 :
            raise ValueError("You cant have a monster with less than 1 life")
        self.life = life

    def every_day_life(self, colony: dict, monsters: list, me_monser:int):
        """ Do all the action a monster have to do every day

        PRE :   - colony (dict) : a dict with all the collony
                - monsters (list) : a list with all the monsters
                - me_monser (int) : tell you what is the index of the monster
        POST : Do all the action a monster have to do every day.
                It take one life per call and do the action the monster have to do with a random rate to do them.
        """
        #random rates
        random_attack_colony = int(1 / 0.1)
        random_attack_monster = int(1 / 0.01)
        random_reproduce = int(1 / 0.001)
        random_change_region = int(1 / 0.0001)

        #one life less for every day
        self.life += -1
        if self.life <= 0 :
            monsters.remove(me_monser)
            return colony, monsters

        #do the random actions
        if random.randrange(0, random_attack_colony) == 1 :
            colony = self.attack_colony(colony)

        if random.randrange(0, random_attack_monster) == 1 :
            self.attack_monsters(monsters, me_monser)

        if random.randrange(0, random_reproduce) == 1 :
            self.reproduce(monsters)

        if random.randrange(0, random_change_region) == 1 :
            self.change_region(monsters, me_monser)

        return colony, monsters

    def attack_colony(self, colony: dict):
        """ Make The monster attack à random colony

        PRE :   - colony (dict) : a dict with all the collony
        POST : choose on existing colony and kill the number of workers that the worker make domange.
                if there are less ants than damages, all the workers left will die.
                return all the colony, with those who have lost workers.
        """

        nbr_colony = len(colony)
        #return the colony if there ar no one to be attack
        if nbr_colony == 0 :
            return colony
        attack_colony = random.randrange(nbr_colony)

        #suprimer le nombres de fourmis que faire le monstre de dégats
        for i in range(len(colony[str(list(colony)[attack_colony])]["workers"])-self.domages, len(colony[str(list(colony)[attack_colony])]["workers"])):
            #check that there are enough ants to kill in relation to the damage, if not, we'll kill the one left.
            if i <= 0 :
                for index in range(len(colony[str(list(colony)[attack_colony])]["workers"])):
                    del colony[str(list(colony)[attack_colony])]["workers"][index]
                return colony

            #delete the last ant worker
            del colony[str(list(colony)[attack_colony])]["workers"][i]

        return colony


    def do_domages(self, domages: int):
        """ Do domage to the monster

        PRE :   - domages (int) : the number of damage the will hurt the monster.
        POST : do domange to the monsters.
        """
        self.life -= domages
        pass

    def attack_monsters(self, monsters: list, me_monser :int):
        """ Make The monster attack a other monster

        PRE :   - monsters (list) : a list that contain all the monsters.
                - me_monster (int) : containe the position of the monster to not damage himself .
        POST : do domange to all the monsters in the simulation exept himself.
                (it use the do_domages() methode of each object).
        """
        for i in range(len(monsters)) :
            if me_monser is not i :
                monsters[i].do_domages(self.domages)
        pass

    @staticmethod
    def change_region(monsters: list, me_monser: int):
        """ Delete a monster in the simulation

        PRE :   - monsters (list) : a list that contain all the monsters.
                - me_monster (int) : containe the position of the monster to remove himself.
        POST : remove a monster in the simulation for the reason that he change of région in the world.
                It return the update list of monsters.
        """
        monsters[me_monser].remove()
        return monsters

    @staticmethod
    def reproduce(monsters: list):
        """ Add a monster in the simulation

        PRE :   - monsters (list) : a list that contain all the monsters.
        POST : add a monster in the simulation. It need at least 2 monster to create à new one.
                It returns the update list of monsters.
        """
        monsters.append(Monster())
        return monsters

    def __str__(self):
        """ stingify the data of the monster

        PRE : /
        POST : Return the data of the monster in a string.
        """
        return f"The monster call {self.name}, have {self.life} life left and he does {self.domages} domage. "