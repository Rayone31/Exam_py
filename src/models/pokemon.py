class Pokemon:
    def __init__(self, name, type, health, level,  attack, defense, healthmax =100, energie=50, faim=50, bonheur=50):   
        self.name = name
        self.type = type
        self.health = health 
        self.level = level
        self.energie = energie
        self.faim = faim
        self.bonheur = bonheur
        self.alive = True
        self.healthmax = healthmax
        self.energiemax = 100
        self.faimmax = 100
        self.bonheurmax = 100
        self.action = None
        self.experience = 0
        self.experience_max = 100
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Health: {self.health}/{self.healthmax}, Energie: {self.energie}/{self.energiemax}, Level: {self.level}, Experience: {self.experience}/{self.experience_max} Faim: {self.faim}/{self.faimmax}, Bonheur: {self.bonheur}/{self.bonheurmax}"
    
    def Pokemon_parametre(self):
        self.name = input("Enter the name of the Pokemon: ")
        types = ["Carapuce", "Bulbizare", "Samaleche"]
        print("Choose of the Starter:")
        for i, t in enumerate(types, 1):
            print(f"{i}. {t}")
        choice = int(input("Enter the number corresponding to the Starter: "))
        type_choice = types[choice - 1]
        
        if type_choice == "Carapuce":
            from .carapuce import Carapuce 
            return Carapuce(self.name)
        elif type_choice == "Bulbizare":
            from .bulbizare import Bulbizare 
            return Bulbizare(self.name)
        elif type_choice == "Salameche":
            from .salameche import Salameche  
            return Salameche(self.name)
        
    def levelUp(self):
        self.level += 1
        self.healthmax += 5
        self.energiemax += 5
        self.attack += 5
        self.defense += 5
        self.health = self.healthmax
        self.energie = self.energiemax
        self.experience = 0
        self.experience_max += 25
    

        
    