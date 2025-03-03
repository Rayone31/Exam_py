from utils.helpers import clear, get_ordered_actions
from utils.menu import menus
from models.event import generate_random_event
from utils.fight import combat_interface
from models.dresseur import Dresseur

def game(pokemon):
    while pokemon.alive:
        event = generate_random_event()
        event_name = event.name if event.event_type == 'passive' else None

        if event.event_type == 'active':
            print(event.trigger())
            dresseur = Dresseur("Dresseur")
            combat_interface(pokemon, dresseur.pokemon)
        else:
            if pokemon.health <= 0:
                print(f"{pokemon.name} est mort.")
                pokemon.alive = False

            elif pokemon.energie <= 0:
                pokemon.health -= 5

            elif pokemon.faim >= 100:
                pokemon.health -= 7
                pokemon.energie -= 2
                pokemon.bonheur -= 2

            elif pokemon.bonheur <= 0:
                pokemon.health -= 4

            if pokemon.experience >= pokemon.experience_max:
                pokemon.levelUp()

        while True:
            try:
                choice, action = menus(pokemon, event_name)
                actions = get_ordered_actions()
                if 1 <= choice <= len(actions):
                    action_method = getattr(pokemon, actions[choice - 1])
                    action_method()
                    pokemon.experience += 10
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        clear()