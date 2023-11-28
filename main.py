import time
import argparse
import subprocess
import platform
import json
from libs.fourmis_generator import *
from libs.nouriture_generator import *

# the program have to be launch from an command prompt
# example of prompt : "python main.py -AW 100 -AS 10 -F 1000 -D 110 -S 0.5  DarkAnt DarkAnt DarkAnt RedAnt"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-AW", "--nbrAntsWorkers", help="set the number of ants at the beggin of the simulation")
    parser.add_argument("-AS", "--nbrAntsSoldiers", help="set the number of ants at the beggin of the simulation")
    parser.add_argument("-F", "--food", help="set the quantity of food at the beggin of the simulation")
    parser.add_argument("-D", "--days", help="set the numbers of days that the simulation have to run")
    parser.add_argument("-S", "--sleepTime", help="set sleep time between every day (in seconds)")
    parser.add_argument("AntsTypes", nargs=argparse.REMAINDER,
                        help="Use all additional arguments to create colonies with ants of those type.")
    args = parser.parse_args()


    def clear_screen():
        if platform.system() == 'Windows':
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear", shell=True)


    def showState(type, nbrAntsWorkers, nbrAntssoldiers, nbrFood):
        """ show the state of the simulation """
        print(f"{type} : Il reste {nbrAntsWorkers} ouvrières, {nbrAntssoldiers} soldats et {nbrFood} de nouriture ")


    def launchSimulation(anthill):
        """ launch the simulation for one day of a collonie"""
        randomDeathRate = 1 / 0.001

        # delete one live to the ant and add a possible random death (workers)
        for i in list(anthill["workers"].keys()):
            if anthill["workers"][i].every_day_life:
                del anthill["workers"][i]
            if random.randrange(randomDeathRate) == 1:
                if i in anthill["workers"]:
                    del anthill["workers"][i]
        # delete one live to the ant and add a possible random death (soldiers)
        for i in list(anthill["soldiers"].keys()):
            if anthill["soldiers"][i].every_day_life:
                del anthill["soldiers"][i]
            if random.randrange(randomDeathRate) == 1:
                if i in anthill["soldiers"]:
                    del anthill["soldiers"][i]
        # delete one live to the ant (qween)
        for i in list(anthill["qween"].keys()):
            if anthill["qween"][i].every_day_life:
                del anthill["qween"][i]
        # create/update ants from larva
        for i in list(anthill["larva"].keys()):
            anthill["larva"][i].update_state
            if anthill["larva"][i].every_day_life:
                del anthill["larva"][i]
                generate_colony_workers(1, anthill["antProprety"]["worker"]["life"], anthill["type"],anthill["antProprety"]["worker"]["nbr_food_collect_per_day"])
            if random.randrange(randomDeathRate) == 1:
                if i in anthill["larva"]:
                    del anthill["larva"][i]

        """
        test food to eat, mange un nombre random de noruiture par jours
        
        """

        # every ant have to eat or die
        for i in anthill["workers"].copy():
            if anthill["food"].check_class():
                anthill["food"].del_food()
            else:
                del anthill["workers"][i]
        for i in anthill["soldiers"].copy():
            if anthill["food"].check_class():
                anthill["food"].del_food()
            else:
                del anthill["soldiers"][i]

        # generate the new ants from the qween
        if anthill["food"].all_storage_food() >= 3:

            # make workers in function of nbr of eggs the qween can make
            nbrLarva = len(anthill["larva"])
            newAntLarva = generate_colony_larva(anthill["antProprety"]["qween"]["nbr_eggs_per_day"], anthill["antProprety"]["larva"]["life"], anthill["type"])
            for i in range(anthill["antProprety"]["qween"]["nbr_eggs_per_day"]):
                anthill["larva"][nbrLarva] = newAntLarva[i]
                nbrLarva += 1


        # add food in fuction of the nbr of worker and the food he can collect per day
        # anthill["food"] += len(anthill["workers"])*anthill["antProprety"]["worker"]["nbr_food_collect_per_day"]
        nbr_to_add = len(anthill["workers"]) * anthill["antProprety"]["worker"]["nbr_food_collect_per_day"]
        anthill["food"].add_food(nbr_to_add)
        # show the state of the porgram
        showState(anthill["type"], len(anthill["workers"]), len(anthill["soldiers"]),
                  anthill["food"].all_storage_food())


    # differents types of Ants

    try:
        with open("data/typeAntProprety.json") as file:
            typeAntProprety = json.load(file)
    except IOError as e:
        print(f"IOERROR : {e}")

    # creatre all collonies
    collonies = {}
    nbrCollonies = 0
    for i in args.AntsTypes:
        nbrCollonies += 1
        collonies[str(nbrCollonies) + ") " + i] = generate_colony(typeAntProprety[i], str(nbrCollonies) + ") " + i,
                                                                  int(args.nbrAntsWorkers), int(args.nbrAntsSoldiers),
                                                                  int(args.food))

    # begin message
    clear_screen()
    print("Bienvenue dans votre MVP, nous allons initialiser votre fourmilière")
    time.sleep(2)

    # start simulation
    for day in range(1, int(args.days) + 1):
        clear_screen()
        print(f"Jour n°: {day}")

        for i in collonies.values():
            launchSimulation(i)
        print(collonies)
        time.sleep(0.2)
        # time of sleep between every day
        time.sleep(float(args.sleepTime))
