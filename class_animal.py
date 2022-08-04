list_animaux = ["guepard","lapin","poisson","pigeon", "autres"]

class Animal:
    type = str
    deplacement = str
    habitat= str

    def __init__(self, type, deplacement, habitat):
        self.type = type
        self.deplacement = deplacement
        self.habitat = habitat
    
    def mode_deplacement(self):
        if  self.type in range ["guepard","lapin"]:
             self.deplacement = "marche"
        elif self.type == "poisson":
             self.deplacement = "nange"  
        elif self.type == "pigeon":
             self.deplacement = "vole"
        elif self.type == "autres":
            self.deplacement = "inconnu"
        
            print(f"Un {self.type} {self.deplacement}.")

    def lieu_habitat(self):
        if  self.type in range ["guepard","lapin"]:
             self.habitat = "terre"
        elif self.type == "poisson":
             self.habitat = "eau"  
        elif self.type == "pigeon":
             self.habitat = "air"
        elif self.type == "autres":
            self.habitat = "inconnu"
        
            print(f"Le lieu d'habitat pour un {self.type} est {self.habitat}.")
            

   


        
        

            

