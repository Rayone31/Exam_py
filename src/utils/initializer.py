from models.pokemon import Pokemon
from utils.helpers import clear

def initialize_pokemon():
    clear()
    base_pokemon = Pokemon("", "", "", 0, 0, 0, 0)
    pokemon = base_pokemon.Pokemon_parametre()
    clear()
    return pokemon