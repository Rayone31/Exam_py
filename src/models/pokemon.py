class Pokemon:
    def __init__(self, name, type, health, level, base_attack, base_defense, healthmax=100, energie=50, faim=50, bonheur=50):   
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
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.update_stats()

    def update_stats(self):
        self.attack = self.base_attack + (self.level - 1) * 2
        self.defense = self.base_defense + (self.level - 1) * 2

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Health: {self.health}/{self.healthmax}, Energie: {self.energie}/{self.energiemax}, Level: {self.level}, Experience: {self.experience}/{self.experience_max} Faim: {self.faim}/{self.faimmax}, Bonheur: {self.bonheur}/{self.bonheurmax}"
    
    def Pokemon_parametre(self):
        self.name = input("Enter the name of the Pokemon: ")
        types = ["Carapuce", "Bulbizare", "Salameche"]
        print("Choose of the Starter:")
        for i, t in enumerate(types, 1):
            print(f"{i}. {t}")
        
        while True:
            try:
                choice = int(input("Enter the number corresponding to the Starter: "))
                if 1 <= choice <= len(types):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        type_choice = types[choice - 1]
        level = 5
        
        pokemon_classes = {
            "Carapuce": "carapuce.Carapuce",
            "Bulbizare": "bulbizare.Bulbizare",
            "Salameche": "salameche.Salameche"
        }
        
        module_name, class_name = pokemon_classes[type_choice].rsplit(".", 1)
        module = __import__(f"models.{module_name}", fromlist=[class_name])
        pokemon_class = getattr(module, class_name)
        
        return pokemon_class(self.name, level)
        
    def levelUp(self):
        self.level += 1
        self.healthmax += 5
        self.energiemax += 5
        self.health = self.healthmax
        self.energie = self.energiemax
        self.experience = 0
        self.experience_max += 25
        self.update_stats()