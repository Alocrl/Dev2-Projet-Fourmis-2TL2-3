import argparse
import subprocess
import platform
import time

from libs.fourmis_generator import *
from libs.nouriture_generator import *
from libs.monster_generator import *

# the program have to be launch from an command prompt
# example of prompt : "python main.py -AW 100 -AS 10 -F 1000 -D 110 -S 0.5 -M 2 DarkAnt DarkAnt DarkAnt RedAnt"

def clear_screen():
    """ Clear the command line for wondown, mac and linux
        It does nont work in the pycharm command line !

    PRE : /
    POST : /
    """
    if platform.system() == 'Windows':
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


def show_state(ant_type: str, nbr_ants_workers: int, nbr_ants_soldiers: int, nbr_larva: int, nbr_food: int, nbr_eat_type: int):
    """ Show the state of the simulation for one colony

    PRE :   - ant_type (string) : the type of ant and his colony number.
            - nbr_ants_workers (int) : the number of workers the colony have
            - nbr_ants_soldiers (int) : the number of soldiers the colony have.
            - nbr_larva (int) : the number of larva the colony have.
            -nbr_food (int) : the number of food the colony have.
    POST : print à string with all the informations in the params of one colony.
        exemple :
            - 1) DarkAnt : Il reste 4 ouvrières, 0 soldats, 4 larva/eggs et 33218 de nouriture
            - 2) RedAnt : Il reste 90 ouvrières, 8 soldats, 7 larva/eggs et 25173 de nouriture
    """
    print(f"{ant_type} : Il reste {nbr_ants_workers} ouvrières, {nbr_ants_soldiers} soldats, {nbr_larva} larva/eggs et {nbr_food} de nouriture (de {nbr_eat_type} type)")

def launch_simulation(anthill: dict):
    """ Launch the simulation for one day of a collonie

    PRE :  - anthill (dict) : is a dictionaire with all the information about the colony that will simulate.

    POST : execute all the code to simulate à day, and then  call the "show_state" function to show
            the state of the colony.
    """
    random_death_rate = int(1 / 0.001)

    # delete one live to the ant and add a possible random death (workers)
    for index in list(anthill["workers"].keys()):
        if anthill["workers"][index].every_day_life:
            del anthill["workers"][index]
        if random.randrange(random_death_rate) == 1:
            if index in anthill["workers"]:
                del anthill["workers"][index]
    # delete one live to the ant and add a possible random death (soldiers)
    for index in list(anthill["soldiers"].keys()):
        if anthill["soldiers"][index].every_day_life:
            del anthill["soldiers"][index]
        if random.randrange(random_death_rate) == 1:
            if index in anthill["soldiers"]:
                del anthill["soldiers"][index]
    # delete one live to the ant (qween)
    for index in list(anthill["qween"].keys()):
        if anthill["qween"][index].every_day_life:
            del anthill["qween"][index]

    # update larva state + create workers if larva hatch
    for index in list(anthill["larva"].keys()):
        anthill["larva"][index].update_state()
        if anthill["larva"][index].every_day_life:
            del anthill["larva"][index]
            # ajouter une workers
            anthill["workers"][len(anthill["workers"])] = \
            generate_colony_workers(1, anthill["antProprety"]["worker"]["life"], anthill["type"],
                                    anthill["antProprety"]["worker"]["nbr_food_collect_per_day"])[0]
        if random.randrange(int(random_death_rate / 10)) == 1:
            if index in anthill["larva"]:
                del anthill["larva"][index]
                pass

    # every ant have to eat or die
    for index in anthill["workers"].copy():
        if anthill["food"].check_class():
            anthill["food"].del_food()
        else:
            del anthill["workers"][index]
    for index in anthill["soldiers"].copy():
        if anthill["food"].check_class():
            anthill["food"].del_food()
        else:
            del anthill["soldiers"][index]

    # generate the new eggs/larva from the qween
    if anthill["food"].all_storage_food() >= 5:
        # make workers in function of nbr of eggs the qween can make
        nbr_larva = len(anthill["larva"])
        new_ant_larva = generate_colony_larva(anthill["antProprety"]["qween"]["nbr_eggs_per_day"],
                                            anthill["antProprety"]["larva"]["life"], anthill["type"])
        for index in range(anthill["antProprety"]["qween"]["nbr_eggs_per_day"]):
            anthill["larva"][nbr_larva] = new_ant_larva[index]
            nbr_larva += 1

    # add food in fuction of the nbr of worker and the food he can collect per day
    # anthill["food"] += len(anthill["workers"])*anthill["antProprety"]["worker"]["nbr_food_collect_per_day"]
    nbr_to_add = len(anthill["workers"]) * anthill["antProprety"]["worker"]["nbr_food_collect_per_day"]
    anthill["food"].add_food(nbr_to_add)

    # show the state of the porgram
    show_state(anthill["type"], len(anthill["workers"]), len(anthill["soldiers"]), len(anthill["larva"]),
              anthill["food"].all_storage_food(), anthill["food"].all_type_food() )







if __name__ == '__main__':
    """ Launch the simulation code """

    parser = argparse.ArgumentParser()
    parser.add_argument("-AW", "--nbrAntsWorkers", help="set the number of ants at the beggin of the simulation")
    parser.add_argument("-AS", "--nbrAntsSoldiers", help="set the number of ants at the beggin of the simulation")
    parser.add_argument("-F", "--food", help="set the quantity of food at the beggin of the simulation")
    parser.add_argument("-D", "--days", help="set the numbers of days that the simulation have to run")
    parser.add_argument("-S", "--sleepTime", help="set sleep time between every day (in seconds)")
    parser.add_argument("-M", "--nbrMonsters", help="set the number of Monsters at the beggin of the simulation")
    parser.add_argument("AntsTypes", nargs=argparse.REMAINDER, help="Use all additional arguments to create colonies with ants of those type.")

    args = parser.parse_args()


    # differents types of Ants
    try:
        with open("data/typeAntProprety.json") as file:
            typeAntProprety = json.load(file)
    except IOError as e:
        print(f"IOERROR : {e}")

    # creatre all colony
    collonies = {}
    nbrCollonies = 0
    for i in args.AntsTypes:
        nbrCollonies += 1
        collonies[str(nbrCollonies) + ") " + i] = generate_colony(typeAntProprety[i], str(nbrCollonies) + ") " + i, int(args.nbrAntsWorkers), int(args.nbrAntsSoldiers), int(args.food))

    print(collonies)

    time.sleep(100)
    # creatre all monsters
    monsters = []

    for i in range(int(args.nbrMonsters)):
        monsters.append(Monster())

    # begin message
    clear_screen()
    print("Bienvenue dans votre MVP, nous allons initialiser votre fourmilière")
    time.sleep(1)

    # start simulation
    for day in range(1, int(args.days) + 1):
        clear_screen()
        print(f"Jour n°: {day}")

        # play the colony
        for i in collonies.values():
            launch_simulation(i)

        #play the monsters
        for i in range(len(monsters)) :
            collonies, monsters = monsters[i].every_day_life(collonies, monsters, i)


        # time of sleep between every day
        time.sleep(float(args.sleepTime))
