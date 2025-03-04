import random
from .carapuce import Carapuce
from .bulbizarre import Bulbizarre
from .salameche import Salameche

class Dresseur:
    def __init__(self, name, player_level):
        self.name = name
        self.player_level = player_level
        self.pokemon = self.choose_random_pokemon()

    ## Choose a random pokemon for the dresseur
    def choose_random_pokemon(self):
        level = random.randint(self.player_level - 3, self.player_level)
        pokemons = [Carapuce("Carapuce", level), Bulbizarre("Bulbizarre", level), Salameche("Salameche", level)]
        return random.choice(pokemons)