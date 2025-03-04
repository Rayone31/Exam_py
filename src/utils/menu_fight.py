import random
from utils.helpers import clear
from utils.fight import defend, use_potion, type_avantages
from colorama import Fore, Style, init

init(autoreset=True)

## This function is the combat interface
# This function handles the combat interface between the player's pokemon and the opponent's pokemon.
def combat_interface(pokemon, opponent):
    original_pokemon_defense = pokemon.defense
    original_opponent_defense = opponent.defense

    while pokemon.alive and opponent.alive:
        clear()
        print(f"{Fore.RED +Style.BRIGHT}=============================================== Combat ========================================================\n")
        print(f"{Fore.GREEN}Votre Pokémon: {pokemon.categorie} | {Fore.RED}Vie: {pokemon.health} | {Fore.CYAN}Défense: {pokemon.defense} | {Fore.YELLOW}Niveau: {pokemon.level} | {Fore.BLACK}Condition: {pokemon.condition}")
        print(f"\n{Fore.BLUE + Style.BRIGHT}------------------------------------------------ Vs -----------------------------------------------------------\n")
        print(f"{Fore.GREEN}Dresseur Pokémon: {opponent.name} | {Fore.RED}Vie: {opponent.health} | {Fore.CYAN}Défense: {opponent.defense} | {Fore.YELLOW}Niveau: {opponent.level}")
        print(f"{Fore.MAGENTA + Style.BRIGHT}\n___________________________________________ Choix d'attaque ___________________________________________________\n")
        print(f"{Fore.RED + Style.BRIGHT}1. Attaquer")
        print(f"{Fore.BLUE + Style.BRIGHT}2. Défendre")
        print(f"{Fore.GREEN + Style.BRIGHT}3. Se soigner")
        print(f"{Fore.BLACK + Style.BRIGHT}\n_______________________________________________________________________________________________________________")
        
        ## Handle player choice
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW + Style.BRIGHT}Entre ton choix: "))
                if choice in [1, 2, 3]:
                    break
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Choix invalide. Merci de rentrer un choix valide.")
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}Entrée invalide. Merci de rentrer un nombre.")
        
        opponent_choice = random.choice([1, 2])

        # Effets des conditions
        if pokemon.condition == "Paralysie":
            if random.randint(1, 3) == 1:
                print(f"{pokemon.name}{Fore.YELLOW + Style.BRIGHT} est paralysé et ne peut pas attaquer ce tour-ci!")
                choice = 0
        elif pokemon.condition == "Sommeil":
            if random.randint(1, 2) == 1:
                print(f"{pokemon.name}{Fore.BLUE + Style.BRIGHT} se réveille!")
                pokemon.condition = "Normal"
            else:
                print(f"{pokemon.name}{Fore.CYAN + Style.BRIGHT} dort et ne peut pas attaquer ce tour-ci!")
                choice = 0
        elif pokemon.condition == "Empoisonnement":
            pokemon.health -= 5
            print(f"{pokemon.name}{Fore.MAGENTA + Style.BRIGHT} souffre d'empoisonnement et perd 5 points de vie.")
        elif pokemon.condition == "Confusion":
            if random.randint(1, 2) == 1:
                print(f"{pokemon.name}{Fore.GREEN + Style.BRIGHT} est confus et s'attaque lui-même!")
                pokemon.health -= 15
                choice = 0

        # Actions du dresseur
        if opponent_choice == 1:
            if choice == 2:
                damage_to_pokemon_defense, damage_to_pokemon = defend(pokemon, opponent)
                if damage_to_pokemon_defense > 0:
                    print(f"{Fore.RED + Style.BRIGHT} {opponent.name} a attaqué {pokemon.name} et infligé {damage_to_pokemon_defense} dégâts à votre défense!")
                else:
                    print(f"{Fore.RED + Style.BRIGHT} {opponent.name} a attaqué {pokemon.name} et infligé {damage_to_pokemon} dégâts à votre santé!")
            else:
                damage_to_pokemon = opponent.attack
                pokemon.health -= damage_to_pokemon
                print(f"{Fore.RED + Style.BRIGHT} {opponent.name} a attaqué {pokemon.name} et infligé {damage_to_pokemon} dégâts à votre santé!")
        elif opponent_choice == 2:
            print(f"{Fore.BLUE + Style.BRIGHT}{opponent.name} se défend contre votre prochaine attaque!")

        # Actions du joueur
        if choice == 1:
            if opponent_choice == 2:
                damage_to_opponent_defense, damage_to_opponent = defend(opponent, pokemon)
                if damage_to_opponent_defense > 0:
                    print(f"{Fore.GREEN + Style.BRIGHT}Vous avez attaqué {opponent.name} et infligé {damage_to_opponent_defense} dégâts à sa défense!")
                else:
                    print(f"{Fore.GREEN + Style.BRIGHT}Vous avez attaqué {opponent.name} et infligé {damage_to_opponent} dégâts à sa santé!")
            else:
                damage_to_opponent = pokemon.attack
                opponent.health -= damage_to_opponent
                print(f"{Fore.GREEN + Style.BRIGHT}Vous avez attaqué {opponent.name} et infligé {damage_to_opponent} dégâts à sa santé!")
        elif choice == 2:
            print(f"{Fore.CYAN + Style.BRIGHT}Vous vous défendez contre l'attaque de {opponent.name}!")
        elif choice == 3:
            if all(quantity == 0 for quantity in pokemon.inventory.values()):
                print(f"{Fore.RED + Style.BRIGHT}Vous n'avez pas de potions disponibles!")
            else:
                while True:
                    print(f"{Fore.GREEN + Style.BRIGHT}Choisissez une potion pour vous soigner:")
                    for i, (item, quantity) in enumerate(pokemon.inventory.items(), 1):
                        print(f"{Fore.BLUE + Style.BRIGHT}{i}. {item} (Quantité: {quantity})")
                    print(f"{Fore.WHITE + Style.BRIGHT}{len(pokemon.inventory) + 1}. Retour")
                
                    try:
                        ## Handle potion choice
                        potion_choice = int(input(f"{Fore.BLUE + Style.BRIGHT}Entrez le numéro de la potion: "))
                        if 1 <= potion_choice <= len(pokemon.inventory):
                            potion_name = list(pokemon.inventory.keys())[potion_choice - 1]
                            if pokemon.inventory[potion_name] > 0:
                                pokemon.inventory[potion_name] -= 1
                                use_potion(pokemon, potion_name)
                                print(f"{Fore.GREEN + Style.BRIGHT}Vous avez utilisé {potion_name} et restauré votre santé!")
                                break
                            else:
                                print(f"{Fore.YELLOW + Style.BRIGHT}Vous n'avez plus de cette potion. Choisissez une autre.")
                        elif potion_choice == len(pokemon.inventory) + 1:
                            break
                        else:
                            print(f"{Fore.RED + Style.BRIGHT}Choix invalide. Merci de rentrer un choix valide.")
                    except ValueError:
                        print(f"{Fore.RED + Style.BRIGHT}Entrée invalide. Merci de rentrer un nombre.")
                
                if potion_choice != len(pokemon.inventory) + 1:
                    if opponent_choice == 1:
                        damage_multiplier = type_avantages.get(opponent.type, {}).get(pokemon.type, 1)
                        damage_to_pokemon = opponent.attack * damage_multiplier
                        pokemon.health -= damage_to_pokemon
                        print(f"{Fore.RED + Style.BRIGHT}{opponent.name} a attaqué {pokemon.name} et infligé {damage_to_pokemon} dégâts à votre santé!")
                    elif opponent_choice == 2:
                        print(f"{Fore.BLUE + Style.BRIGHT}{opponent.name} se défend contre votre prochaine attaque!")

        ## Check if the combat is over
        if opponent.health <= 0 and pokemon.health <= 0:
            clear()
            print(f"{Fore.RED + Style.BRIGHT}Les deux Pokémon sont KO.")
            opponent.alive = False
            pokemon.alive = False
            print(f"{Fore.BLUE + Style.BRIGHT}Le combat se termine par un match nul.")
            return False

        if opponent.health <= 0:
            clear()
            print(f"{Fore.GREEN + Style.BRIGHT}{opponent.name} est KO.")
            opponent.alive = False
            base_experience = 25
            experience_gained = base_experience + (pokemon.level - 1) * 25
            pokemon.experience += experience_gained
            print(f"{Fore.BLUE + Style.BRIGHT}Votre Pokémon a gagné {experience_gained} points d'expérience!")
            break
        
        if pokemon.health <= 0:
            clear()
            print(f"{Fore.RED + Style.BRIGHT}{pokemon.name} est KO.")
            print(f"{Fore.BLUE + Style.BRIGHT}Vous avez perdu le combat.")
            print(f"{Fore.RED + Style.BRIGHT}Vous vous rediriger vers le centre pokemon le plus proche.")
            pokemon.alive = False
            return False
        
        input(f"{Fore.GREEN + Style.BRIGHT}Appuyez sur Entrée pour continuer...")

    pokemon.defense = original_pokemon_defense
    opponent.defense = original_opponent_defense
    return True