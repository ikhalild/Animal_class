list_animaux = ["guepard","lapin","poisson","pigeon", "autres"]

class Animal:
    type = str
    deplacement = str
    habitat= str

    def __init__(self, type):
        self.type = type
        
    def mode_deplacement(self):
        if  self.type in  ["guepard","lapin"]:
             self.deplacement = "marche"
        elif self.type == "poisson":
             self.deplacement = "nage"  
        elif self.type == "pigeon":
             self.deplacement = "vole"
        elif self.type == "autres":
            self.deplacement = "inconnu"
        
        print(f"Un {self.type} {self.deplacement}.")

    def lieu_habitat(self):
        if  self.type in ["guepard","lapin"]:
             self.habitat = "terre"
        elif self.type == "poisson":
             self.habitat = "eau"  
        elif self.type == "pigeon":
             self.habitat = "air"
        else:
             self.type == "autres"
             self.habitat = "inconnu"
        
        print(f"Le lieu d'habitat pour un {self.type} est {self.habitat}.")

                  
animal1 = Animal("guepard")
animal1.mode_deplacement()
animal1.lieu_habitat()
            
animal2 = Animal("poisson")
animal2.mode_deplacement()
animal2.lieu_habitat()

animal3 = Animal("pigeon")
animal3.mode_deplacement()
animal3.lieu_habitat()

animal4 = Animal("autres")
animal4.mode_deplacement()
animal4.lieu_habitat()
        
        

            

