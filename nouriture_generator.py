import random

class nouriture :
    def __init__(self, type) :
        self.type = type

    def type_return(self) :
        object = {"type" : self.type }
        return object

def generation_nouriture(nbre_nouriture) :

    nouriture_type = ["fraise", "bannane", "pomme", "noisette", "graine"]  
    nouriture_object = {}

    for index in range(nbre_nouriture) :
        choix_nourriture = random.choice(nouriture_type)

        generation_nouriture = nouriture(choix_nourriture)
        nouriture_object[index] = generation_nouriture.type_return()
    
    return nouriture_object
