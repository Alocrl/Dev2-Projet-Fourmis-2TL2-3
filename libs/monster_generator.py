import random

class Monster:
    """Class for Monster

        par : Gaetan Carbonnelle
        le : 30/11/2022

    """

    def __init__(self, damage: int=2, name: str="no_name", life: int=100 ):
        """ Initialize the mMonster

        PRE :   - damage (int) : tells you how much damage the monster have.
                - name (str) : tells you the name of the monster.
                - life (int) : tell you the life the monster have
        POST : initialize the number of live that the monster have (self.live), the number of damage that he can make (self.damage)
                and the number of live that the monster will have (self.live). Those three variables are the characteristic of the monster.
        RAISE ValueError : Your monster cant have less than zéro damages.
        RAISE ValueError : Your monster cant have his number of live that are equal to 0 or à négative number.

        """

        #the monster can't have a négative damage
        if damage < 0 :
            raise ValueError("You cant have a monster with less than 0 damage")
        self.damage = damage
        self.name = name

        #the monster can't have a negative live or equal to 0
        if life < 1 :
            raise ValueError("You cant have a monster with less than 1 life")
        self.life = life

    def every_day_life(self, colony: dict, monsters: list, me_monster:int):
        """ Do all the actions a monster have to do every day

        PRE :   - colony (dict) : a dict with all the colony. The dict can be empty.
                - monsters (list) : a list with all the monsters. It may have at least one monster (=> the monster that we are playing right now)
                - me_monster (int) : tell you what is the index of the monster
        POST : The every_day_life function do all the action à monster have to do per day.
                    - It reduce the number of live the monster have by one. if the monster have less than 0 lives, he died and is remove from the list of monsters. It whill also end the function and return the new stats of the colony dict and the monster list.
                    - It have a random chance to attack à colony. If there are no colony in the dict, it simply does nothing.
                    - It have a random chance to attack à other monster. If there are no other monster in the list, it simply does nothing.
                    - It have a random chance to reproduce and create a new monster in the list. It needs at least 2 monster to do it.
                    - The monster have a random chance change of région. It will more concretely say that he left the monster list.
                After all the action that ar randomly made, it return the new stats of the colony dict and the monster list.


        """
        #random rates
        random_attack_colony = int(1 / 0.1)
        random_attack_monster = int(1 / 0.01)
        random_reproduce = int(1 / 0.001)
        random_change_region = int(1 / 0.0001)

        #one life less for every day
        self.life += -1
        if self.life <= 0 :
            monsters.remove(me_monster)
            return colony, monsters

        #do the random actions
        if random.randrange(0, random_attack_colony) == 1 and len(colony) >= 1:
            colony = self.attack_colony(colony)

        if random.randrange(0, random_attack_monster) == 1 and len(monsters) > 1 :
            self.attack_monsters(monsters, me_monster)

        if random.randrange(0, random_reproduce) == 1 and len(monsters) >= 2 :
            self.reproduce(monsters)

        if random.randrange(0, random_change_region) == 1 :
            self.change_region(monsters, me_monster)

        return colony, monsters

    def attack_colony(self, colony: dict):
        """ Make The monster attack à random colony

        PRE :   - colony (dict) : a dict with all the colony, It has at least one colony in the dict.
        POST : Choose randomly an existing colony and kill and do damage to then. The number of damage are decide by the characteristic of the monster (self.damage)
                More concretely, per damage the monster can do, it will kill on worker ant in the random chosen colony.
                In the case the damage the monster can do is greater than the number of workers ants, it will kill all the last ant workers.
                It return the colony dict, with the one that have been attack (lose workers).
        """

        nbr_colony = len(colony)
        #return the colony if there ar no one to be attack
        if nbr_colony == 0 :
            return colony
        attack_colony = random.randrange(nbr_colony)

        #suprimer le nombres de fourmis que faire le monstre de dégats
        for i in range(len(colony[str(list(colony)[attack_colony])]["workers"])-self.damage, len(colony[str(list(colony)[attack_colony])]["workers"])):
            #check that there are enough ants to kill in relation to the damage, if not, we'll kill the one left.
            if i <= 0 :
                for index in range(len(colony[str(list(colony)[attack_colony])]["workers"])):
                    del colony[str(list(colony)[attack_colony])]["workers"][index]
                return colony

            #delete the last ant worker
            del colony[str(list(colony)[attack_colony])]["workers"][i]

        return colony


    def do_damage(self, damage: int):
        """ Do damage to the monster

        PRE :   - damage (int) : the number of damage it will hurt the monster.
        POST : do damage to the current monsters. This function is use when another monster do damage to another.
                The function return nothing.
        """
        self.life -= damage
        pass

    def attack_monsters(self, monsters: list, me_monster :int):
        """ Make The monster attack another monster

        PRE :   - monsters (list) : a list that contain all the monsters. It needs to have at least 2 monster to be sure it can hurt another monster than himself
                - me_monster (int) : contain the position of the monster to not damage himself .
        POST : do damage to all the monsters in the simulation except himself. it will use the do_damage() methode of each monster to do damage to each monster object.
                The function return nothing.
        """
        for i in range(len(monsters)) :
            if me_monster is not i :
                monsters[i].do_damage(self.damage)
        pass

    @staticmethod
    def change_region(monsters: list, me_monster: int):
        """ Delete a monster in the simulation because he changes of region.

        PRE :   - monsters (list) : a list that contain all the monsters. It contains at least one monster (the monster that is playing)
                - me_monster (int) : contain the position of the monster to remove/find himself.
        POST : remove a monster in the simulation for the reason that he change of région in the world.
                It return the update list of monsters.
        """
        monsters[me_monster].remove()
        return monsters

    @staticmethod
    def reproduce(monsters: list):
        """ Add a monster in the simulation

        PRE :   - monsters (list) : a list that contain all the monsters. it needs at least 2 monster to reproduce. (already check before executing the function)
        POST : add a monster in the simulation by adding one in the monster list.
                It return nothing.
        """
        monsters.append(Monster())
        pass


    def __str__(self):
        """ stringify the data of the monster

        PRE : /
        POST : Return the data of the monster in a string.
        """
        return f"The monster call {self.name}, have {self.life} life left and he does {self.damage} damage. "