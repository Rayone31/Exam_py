from colorama import Fore, Style, init

class Pokemon:
    def __init__(self, name, categorie, type, health, level, base_attack, base_defense, healthmax=100, energie=50, faim=50, bonheur=50 ,condition="Normal"):   
        self.name = name
        self.categorie = categorie
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
        self.condition = condition
        self.inventory = {"Petite Potion": 0, "Moyenne Potion": 0, "Grande Potion": 0, "Potion Max": 0 , "Antidote": 0}
        
        self.update_stats()

    ## this function updates the statistics of the pokemon attack and defense according to its level
    def update_stats(self):
        self.attack = self.base_attack + (self.level - 1) * 2
        self.defense = self.base_defense + (self.level - 1) * 2

    ## this function shows the pokemon's statistics
    def __str__(self):
        return f"{Fore.BLUE}Nom: {self.name}, {Fore.GREEN}Categorie: {self.categorie}, {Fore.RED}Health: {self.health}/{self.healthmax}, {Fore.YELLOW}Energie: {self.energie}/{self.energiemax}, {Fore.BLACK}Level: {self.level}, {Fore.CYAN}Experience: {self.experience}/{self.experience_max}, {Fore.WHITE}Faim: {self.faim}/{self.faimmax},{Fore.MAGENTA} Bonheur: {self.bonheur}/{self.bonheurmax}, {Fore.BLACK}Condition: {self.condition}"

    ## this function allows the Pokemon parameters to be entered
    def Pokemon_parametre(self):
        self.name = input(f"{Fore.YELLOW + Style.BRIGHT}Entrez le nom du Pokémon: ")
        categories = ["Carapuce", "Bulbizarre", "Salameche"]
        categories_colored = [f"{Fore.CYAN + Style.BRIGHT}Carapuce", f"{Fore.GREEN + Style.BRIGHT}Bulbizarre", f"{Fore.RED + Style.BRIGHT}Salameche"]
        print(f"{Fore.MAGENTA + Style.BRIGHT}Choix du starter:")
        for i, t in enumerate(categories_colored, 1):
            print(f"{i}. {t}")
        
        while True:
            try:
                choice = int(input(f"{Fore.BLUE + Style.BRIGHT}Entrez le numéro correspondant au Starter: "))
                if 1 <= choice <= len(categories):
                    break
                else:
                    print("Choix invalide. Veuillez saisir un nombre entre 1 et 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        categorie_choice = categories[choice - 1]
        level = 5
        
        pokemon_classes = {
            "Carapuce": "carapuce.Carapuce",
            "Bulbizarre": "bulbizarre.Bulbizarre",
            "Salameche": "salameche.Salameche"
        }
        
        module_name, class_name = pokemon_classes[categorie_choice].rsplit(".", 1)
        module = __import__(f"models.{module_name}", fromlist=[class_name])
        pokemon_class = getattr(module, class_name)
        
        return pokemon_class(self.name, level)
    
    ## this function allows the level of the pokemon to increase
    def levelUp(self):
        self.level += 1
        self.healthmax += 5
        self.energiemax += 5
        self.condition = "Normal"
        self.health = self.healthmax
        self.energie = self.energiemax
        self.experience = 0
        self.experience_max += 25
        self.update_stats()

    ## This function adds an item to the inventory
    def add_to_inventory(self, item, quantity=1):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity