import time
import argparse
import subprocess
import platform
from libs.fourmis_generator import *
from libs.nouriture_generator import *

# the program have to be launched from a command prompt
# example of prompt : "python main.py -AW 100 -AS 10 -F 1000 -D 110 -S 0.5  DarkAnt DarkAnt DarkAnt RedAnt"
"""bojout"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-AW", "--nbr_ants_workers", help="set the number of ants at the beginning of the simulation")
    parser.add_argument("-AS", "--nbr_ants_soldiers", help="set the number of ants at the beginning of the simulation")
    parser.add_argument("-F", "--food", help="set the quantity of food at the beginning of the simulation")
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


    def show_state(species, nbr_ants_workers, nbr_ants_soldiers, nbr_food):
        """ show the state of the simulation """
        print(f"{species} : Il reste {nbr_ants_workers} ouvrières, "
              f"{nbr_ants_soldiers} soldats et {nbr_food} de nouriture")


    def launch_simulation(anthill):
        """ launch the simulation for one day of a colony"""
        random_death_rate = 1000

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
        # delete one live to the ant (queen)
        for index in list(anthill["queen"].keys()):
            if anthill["queen"][index].every_day_life:
                del anthill["queen"][index]

        # every ant have to eat or die
        for index in anthill["workers"].copy():
            if anthill["food"] >= 1:
                anthill["food"] -= 1
            else:
                del anthill["workers"][index]
        for index in anthill["soldiers"].copy():
            if anthill["food"] >= 1:
                anthill["food"] -= 1
            else:
                del anthill["soldiers"][index]

        # generate the new ants from the queen
        if anthill["food"] >= 3:

            # make workers in function of nbr of eggs the queen can make
            nbr_workers = len(anthill["workers"])
            new_ants_workers = generate_colony_workers(anthill["antProprety"]["queen"]["nbrEgsPerDay"],
                                                       anthill["antProprety"]["worker"]["life"], anthill["type"],
                                                       anthill["antProprety"]["worker"]["nbrFoodCollectPerDay"])
            for index in range(anthill["antProprety"]["queen"]["nbrEgsPerDay"]):
                anthill["workers"][nbr_workers] = new_ants_workers[index]
                nbr_workers += 1

            # make soldiers in function of nbr of eggs the queen can make
            nbr_soldiers = len(anthill["soldiers"])
            new_ants_soldiers = generate_colony_soldiers(anthill["antProprety"]["queen"]["nbrEgsPerDay"],
                                                         anthill["antProprety"]["soldier"]["life"], anthill["type"],
                                                         anthill["antProprety"]["soldier"]["damage"])
            for index in range(anthill["antProprety"]["queen"]["nbrEgsPerDay"]):
                anthill["soldiers"][nbr_soldiers] = new_ants_soldiers[index]
                nbr_soldiers += 1

        # add food in fuction of the nbr of worker and the food he can collect per day
        anthill["food"] += len(anthill["workers"]) * anthill["antProprety"]["worker"]["nbrFoodCollectPerDay"]

        # show the state of the porgram
        show_state(anthill["type"], len(anthill["workers"]), len(anthill["soldiers"]), anthill["food"])


    # differents types of Ants
    typeAntProprety = {
        "DarkAnt": {
            "worker": {
                "life": 10,
                "nbrFoodCollectPerDay": 2
            },
            "queen": {
                "life": 300,
                "nbrEgsPerDay": 3
            },
            "soldier": {
                "life": 50,
                "damage": 2
            }
        },
        "RedAnt": {
            "worker": {
                "life": 100,
                "nbrFoodCollectPerDay": 1
            },
            "queen": {
                "life": 300,
                "nbrEgsPerDay": 5
            },
            "soldier": {
                "life": 502,
                "damage": 2
            }
        }
    }

    # creatre all collonies
    collonies = {}
    nbrCollonies = 0
    for i in args.AntsTypes:
        nbrCollonies += 1
        collonies[str(nbrCollonies) + ") " + i] = generate_colony(typeAntProprety[i],
                                                                  str(nbrCollonies) + ") " + i,
                                                                  int(args.nbr_ants_workers),
                                                                  int(args.nbr_ants_soldiers),
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
            launch_simulation(i)

        # time of sleep between every day
        time.sleep(float(args.sleepTime))
