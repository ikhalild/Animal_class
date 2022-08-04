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
            

   


        
        

            

