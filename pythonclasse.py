class etre_vivant:
    """Classe abstraite concernant les etres vivants """
    def __init__(self):
        self = self
    def marche(self):
        self=True
        raise NotImplementedError
    
     

class humain(etre_vivant):
    

    """Classe modelisant un humain"""

    nom = " "
    prenom = " "
    age = " "
    sexe = " "
    holidays = " "
    worker = " "
    
    def iswoman(self):
        """Permet de connaitre la nature de l'individu (Homme ou Femme) """
        if(self.sexe == "F"):
            self = "VRAI"
            return self
        else:
            self = "FAUX"
            return self
     

    def IsOnHolidays(self):
        if(self.holidays == "yes"):
            self = "VRAI"
            return self
        else:
            self = "FAUX"
            return self
    
    def IsWorker(self):
        if(self.worker == "yes"):
            self = "VRAI"
            return self
        else:
            self = "FAUX"
            return self
        
class animal(etre_vivant):
    def marche(self):
        self = marche
        return  self
