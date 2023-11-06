import time
import random
import argparse
from libs.fourmis_generator import generation_fourmis
from libs.nouriture_generator import generation_nouriture


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-A","--nbrAnts", help="set the number of ants at the beggin of the simulation")
    parser.add_argument("-F","--food", help="set the quantity of food at the beggin of the simulation")
    parser.add_argument("-D", "--days", help="set the numbers of days that the simulation have to run")
    args = parser.parse_args()


    def lancement_simulation(obj_fourm, obj_nour, nbre_fourmis_choice, nbre_nouriture_choice, nbre_jours_choice):

        for index1 in range(1, nbre_jours_choice + 1) :

            #suppression vie fourmis
            for i in obj_fourm:
                obj_fourm[i]["vie"] -= 1

            #suppression fourmis
            nombre_fourmis_a_supprimer = random.randint(0, len(obj_fourm))
            for _ in range(0,nombre_fourmis_a_supprimer) :
                if obj_fourm:
                    del obj_fourm[random.choice(list(obj_fourm.keys()))]

            #suppression nouriture
            nombre_nourriture_a_supprimer = random.randint(0, len(obj_nour))
            for _ in range(0,nombre_nourriture_a_supprimer) :
                if obj_nour:
                    del obj_nour[random.choice(list(obj_nour.keys()))]

            print(f"Jour n°: {index1}")
            time.sleep(0.5)
            print(f"il y a {nombre_nourriture_a_supprimer} nouriture mangée, il vous reste {len(obj_nour)}")
            time.sleep(0.5)
            print(f"il y a {nombre_fourmis_a_supprimer} fourmis morte, il reste {len(obj_fourm)} fourmis")
            time.sleep(2)



    print("Bienvenue dans votre MVP, nous allons initialiser votre fourmilière")
    time.sleep(0.5)

    # prompt - genere fourmis en fct du nombre
    object_fourmis = generation_fourmis(int(args.nbrAnts))

    # prompt - genere un cota de nouriture en fct du nombre
    object_nouriture = generation_nouriture(int(args.food))

    # lancement de la simulation en fct d'un nbre de jours
    lancement_simulation(object_fourmis, object_nouriture, int(args.nbrAnts), int(args.food), int(args.days))


    #cle_ale = random.sample(list(object_fourmis.keys()), nombre_fourmis_morte)