import random

class fourmis :
    
    def __init__(self,type, sexe, vie) :
        self.type = type
        self.sexe = sexe
        self.vie = vie
    
    def object_return(self) :
        object = {"type" : self.type , "sexe" : self.sexe , "vie" : self.vie}
        return object

    def __str__(self) :
        return f"type : {self.type} - sexe : {self.sexe} - vie : {self.vie}"


def generation_fourmis(nombre_fourmis):

    ant_type = ["Atta","Camponotus","Formica","Formica","Solenopsis"]
    ant_sexe = ["M", "F"]
    ant_vie = range(23)

    fourmis_object = {}
    
    for index in range(nombre_fourmis) :
        choix_type = random.choice(ant_type)
        choix_sexe = random.choice(ant_sexe)
        choix_vie = random.choice(ant_vie)

        generation_fourmis = fourmis(choix_type,choix_sexe, choix_vie)
        fourmis_object[index] = generation_fourmis.object_return()

    return fourmis_object

