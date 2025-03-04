from utils.helpers import print_status, get_ordered_actions, print_action, clear
from colorama import Fore, Style, init

init(autoreset=True)

selected_action = None

def menus(pokemon, event_message=None):
    global selected_action
    actions = get_ordered_actions()
    
    print(f"{Fore.YELLOW + Style.BRIGHT}===================================================================== Evenement ==============================================================================\n")
    if event_message:
        print(f"{Fore.YELLOW}{event_message}")
    else:
        print("Aucun événement passif pour le moment.")
    
    print(f"{Style.BRIGHT + Fore.BLUE}\n====================================================================== Information ===========================================================================\n")
    if selected_action:
        print_action(selected_action)
    else:
        print(f"{Fore.BLACK}Aucune action sélectionnée pour le moment.")
    
    print(f"{Fore.GREEN + Style.BRIGHT}\n====================================================================== Personnage ============================================================================\n")
    print(pokemon)

    print(f"{Fore.MAGENTA + Style.BRIGHT}\n======================================================================== Status ==============================================================================\n")
    print_status(pokemon)

    print(f"{Fore.WHITE + Style.BRIGHT}\n====================================================================== Inventaire ============================================================================\n")
    for item, quantity in pokemon.inventory.items():
        print(f"{Fore.GREEN + Style.BRIGHT}  - {item}: {quantity}")

    print(f"{Fore.CYAN + Style.BRIGHT}\n========================================================================= Action =============================================================================\n")
    ## Display actions
    for i, action in enumerate(actions, 1):
        print(f"{Fore.RED + Style.BRIGHT}{i}. {action.capitalize()}")
    print(f"{Fore.BLACK + Style.BRIGHT}\n______________________________________________________________________________________________________________________________________________________________")
    
    while True:
        try:
            choice = int(input(f"{Fore.YELLOW}Entrez votre choix:{Fore.RESET} "))
            if 1 <= choice <= len(actions):
                selected_action = actions[choice - 1]
                break
            else:
                print(f"{Fore.RED}Choix invalide. Veuillez saisir un numéro valide.")
        except ValueError:
            print(f"{Fore.RED}Entrée non valide. Veuillez saisir un nombre.")
    
    clear()
    if not pokemon.alive:
        print(f"{Fore.RED + Style.BRIGHT}Game Over")
        return False
    
    return choice, selected_action