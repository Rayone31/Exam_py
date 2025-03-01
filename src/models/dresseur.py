import random
from .carapuce import Carapuce
from .bulbizare import Bulbizare
from .salameche import Salameche

class Dresseur:
    def __init__(self, name):
        self.name = name
        self.pokemon = self.choose_random_pokemon()

    def choose_random_pokemon(self):
        pokemons = [Carapuce("Carapuce"), Bulbizare("Bulbizare"), Salameche("Salameche")]
        return random.choice(pokemons)