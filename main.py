import time
import random
import argparse
from libs.fourmis_generator import generateAnts
from libs.nouriture_generator import generateFood


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-A", "--nbrAnts", help="set the number of ants at the beggin of the simulation")
    parser.add_argument("-F", "--food", help="set the quantity of food at the beggin of the simulation")
    parser.add_argument("-D", "--days", help="set the numbers of days that the simulation have to run")
    args = parser.parse_args()


    def showState (day, nbrFoodEaten, nbrFood, nbrDeathAnts, nbrAnts, TimeWaitPerDay = 0.5):
        """ show the state of the simulation """
        
        print(f"Jour n°: {day}")
        print(f"il y a {nbrFoodEaten} nouriture mangée, il vous reste {nbrFood} de nouriture")
        print(f"il y a {nbrDeathAnts} fourmis morte, il reste {nbrAnts} fourmis")
        time.sleep(TimeWaitPerDay)


    def launchSimulation(objectAllAnts, objectAllFood,nbrDays):
        """ launch the simulation """
        randomDeathRate = 1 / 0.01
        nbrAnts = len(objectAllAnts)
        nbrFood = len(objectAllFood)


        print(f"vous avez : {nbrAnts} fourmis et {len(objectAllFood)} de nouriture ")

        for day in range(1, nbrDays) :

            #delete one live to ant and add random death
            for i in objectAllAnts.copy():
                if objectAllAnts[i].everyDayLife :
                    del objectAllAnts[i]
                if random.randrange(randomDeathRate) == 1 :
                    del objectAllAnts[i]

            #every ant have to eat or die
            for i in objectAllAnts.copy() :
                if len(objectAllFood) >= 1 :
                    del objectAllFood[random.choice(list(objectAllFood.keys()))]
                else :
                    del objectAllAnts[random.choice(list(objectAllAnts.keys()))]


            showState(day, nbrFood - len(objectAllFood), len(objectAllFood), nbrAnts - len(objectAllAnts), len(objectAllAnts))

            nbrAnts = len(objectAllAnts)
            nbrFood = len(objectAllFood)



    print("Bienvenue dans votre MVP, nous allons initialiser votre fourmilière")
    time.sleep(0.5)

    #generate ant and food
    objectAllAnts = generateAnts(int(args.nbrAnts))
    objectAllFood = generateFood(int(args.food))


    launchSimulation(objectAllAnts, objectAllFood, int(args.days))