import os
from models.pokemon import Pokemon
from utils.game import game

def main():
    clear()
    base_pokemon = Pokemon("", "", 0, 0, 0, 0)
    pokemon = base_pokemon.Pokemon_parametre()
    clear()
    game(pokemon)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()