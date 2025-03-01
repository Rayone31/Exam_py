import random
from utils.helpers import clear

def combat_interface(pokemon, opponent):
    original_pokemon_defense = pokemon.defense
    original_opponent_defense = opponent.defense

    while pokemon.alive and opponent.alive:
        clear()
        print("=============================================== Combat ========================================================")
        print(f"Votre Pokémon: {pokemon.name} | Vie: {pokemon.health} | Défense: {pokemon.defense}")
        print(f"Dresseur Pokémon: {opponent.name} | Vie: {opponent.health} | Défense: {opponent.defense}")
        print("1. Attaquer")
        print("2. Défendre")
        choice = int(input("Enter your choice: "))
        
        if choice not in [1, 2]:
            print("Invalid choice. Please enter a valid number.")
            continue
        
        opponent_choice = random.choice([1, 2])
        
        if choice == 1 and opponent_choice == 1:
            damage_to_opponent = pokemon.attack
            damage_to_pokemon = opponent.attack
            opponent.health -= damage_to_opponent
            pokemon.health -= damage_to_pokemon
            print(f"Vous avez attaqué {opponent.name} et infligé {damage_to_opponent} dégâts à sa santé!")
            print(f"{opponent.name} a attaqué {pokemon.name} et infligé {damage_to_pokemon} dégâts à votre santé!")
        elif choice == 1 and opponent_choice == 2:
            if opponent.defense > 0:
                damage_to_opponent_defense = min(pokemon.attack, opponent.defense)
                opponent.defense -= damage_to_opponent_defense
                print(f"Vous avez attaqué {opponent.name} et infligé {damage_to_opponent_defense} dégâts à sa défense!")
            else:
                damage_to_opponent = pokemon.attack
                opponent.health -= damage_to_opponent
                print(f"Vous avez attaqué {opponent.name} et infligé {damage_to_opponent} dégâts à sa santé!")
            print(f"{opponent.name} se défend contre votre attaque!")
        elif choice == 2 and opponent_choice == 1:
            if pokemon.defense > 0:
                damage_to_pokemon_defense = min(opponent.attack, pokemon.defense)
                pokemon.defense -= damage_to_pokemon_defense
                print(f"{opponent.name} a attaqué {pokemon.name} et infligé {damage_to_pokemon_defense} dégâts à votre défense!")
            else:
                damage_to_pokemon = opponent.attack
                pokemon.health -= damage_to_pokemon
                print(f"{opponent.name} a attaqué {pokemon.name} et infligé {damage_to_pokemon} dégâts à votre santé!")
            print(f"Vous vous défendez contre l'attaque de {opponent.name}!")
        elif choice == 2 and opponent_choice == 2:
            print("Les deux Pokémon se préparent à se défendre!")

        if opponent.health <= 0:
            print(f"{opponent.name} est mort.")
            opponent.alive = False
            experience_gained = random.randint(100, 200)
            pokemon.experience += experience_gained
            print(f"Votre Pokémon a gagné {experience_gained} points d'expérience!")
            break
        
        if pokemon.health <= 0:
            print(f"{pokemon.name} est mort.")
            pokemon.alive = False
            break
        
        input("Appuyez sur Entrée pour continuer...")

    pokemon.defense = original_pokemon_defense
    opponent.defense = original_opponent_defense