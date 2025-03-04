from utils.helpers import clear, get_ordered_actions
from utils.menu import menus
from models.event import generate_random_event
from utils.menu_fight import combat_interface
from models.dresseur import Dresseur
from colorama import Fore, Style, init

init(autoreset=True)

## Game function
# This function is the main function of the game. It will generate random events and handle the game logic.
def game(pokemon):
    while pokemon.alive:
        event = generate_random_event()
        event_message = event.trigger(pokemon)

        if event.event_type == 'active':
            dresseur = Dresseur("Dresseur", pokemon.level)
            combat_result = combat_interface(pokemon, dresseur.pokemon)
            if not combat_result:
                print(f"{Fore.RED + Style.BRIGHT}Game Over")
                return
        else:
            ## Handle passive events
            if pokemon.health <= 0:
                print(f"{pokemon.name} est mort.")
                pokemon.alive = False
                print(f"{Fore.RED + Style.BRIGHT}Game Over")
                return

            elif pokemon.energie <= 0:
                pokemon.health -= 5
                pokemon.bonheur -= 2

            elif pokemon.faim >= 100:
                pokemon.health -= 7
                pokemon.energie -= 2
                pokemon.bonheur -= 2

            elif pokemon.bonheur <= 0:
                pokemon.health -= 4

            if pokemon.condition == "Empoisonnement":
                pokemon.health -= 5
                pokemon.bonheur -= 2
            elif pokemon.condition == "Paralysie":
                pokemon.energie -= 5
                pokemon.bonheur -= 2
            elif pokemon.condition == "Sommeil":
                pokemon.energie += 3
                pokemon.bonheur -= 2
            elif pokemon.condition == "Confusion":
                pokemon.health -= 3
                pokemon.energie -= 3
                pokemon.bonheur -= 2

            if pokemon.experience >= pokemon.experience_max:
                pokemon.levelUp()

            if pokemon.health <= 0:
                print(f"{pokemon.name} est KO.")
                pokemon.alive = False
                print(f"{Fore.RED + Style.BRIGHT}Game Over")
                return
            
        menu_result = menus(pokemon, event_message)
        if not menu_result:
            print(f"{Fore.RED + Style.BRIGHT}Game Over")
            return

        ## Get the choice and action
        choice, action = menu_result
        actions = get_ordered_actions()
        if 1 <= choice <= len(actions):
            action_method = getattr(pokemon, actions[choice - 1])
            action_method()
            pokemon.experience += 10

            if pokemon.health <= 0:
                print(f"{pokemon.name} est KO.")
                pokemon.alive = False
                print(f"{Fore.RED + Style.BRIGHT}Game Over")
                return
        else:
            print(f"{Fore.RED + Style.BRIGHT}Invalid choice. Please enter a valid number.")

        clear()