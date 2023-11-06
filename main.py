import time
import random
from libs.fourmis_generator import generation_fourmis
from libs.nouriture_generator import generation_nouriture

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

time.sleep(1)

# prompt - genere fourmis aléatoire en fct du nombre
nbre_fourmis = int(input("Combien de fourmis voulez-vous ?  "))
object_fourmis = generation_fourmis(nbre_fourmis)
time.sleep(1)

# prompt - genere un cota de nouriture en fct du nombre
nbre_nouriture = int(input("Combien de nouriture pour la galerie voulez-vous ?  "))
object_nouriture = generation_nouriture(nbre_nouriture)
time.sleep(1)

# lancement de la simulation en fct d'un nbre de jours 
simulation_choice = input("Voulez-vous lancer la simulation ? (o = oui ; n = non)  ")
if simulation_choice.lower() == 'o':
    nbre_jours = int(input("Combien de jours voulez vous simuler ? "))
    lancement_simulation(object_fourmis, object_nouriture, nbre_fourmis, nbre_nouriture, nbre_jours)
    
elif simulation_choice.lower() == 'n':
    print("Simulation annulée.")

else:
    print("Veuillez saisir 'o' pour oui ou 'n' pour non.")

#cle_ale = random.sample(list(object_fourmis.keys()), nombre_fourmis_morte)