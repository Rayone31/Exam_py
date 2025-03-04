from models.action import Action
from colorama import Fore, Style, init

init(autoreset=True)


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_status(pokemon):
    statuses = []
    if pokemon.health <= 0:
        statuses.append(f"{pokemon.name}{Fore.RED + Style.BRIGHT} est KO.")
    if pokemon.energie <= 0:
        statuses.append(f"{pokemon.name}{Fore.YELLOW + Style.BRIGHT} est fatigué.")
    if pokemon.faim >= 100:
        statuses.append(f"{pokemon.name}{Fore.WHITE + Style.BRIGHT} a faim.")
    if pokemon.bonheur <= 0:
        statuses.append(f"{pokemon.name}{Fore.RED + Style.BRIGHT} est malheureux.")
    if pokemon.experience == 0 and pokemon.level > 1:
        statuses.append(f"{pokemon.name} {Fore.GREEN + Style.BRIGHT} est monté de 1 niveau.")
    if pokemon.health == pokemon.healthmax:
        statuses.append(f"{pokemon.name} {Fore.GREEN + Style.BRIGHT} est en pleine forme.")
    if pokemon.energie == pokemon.energiemax:
        statuses.append(f"{pokemon.name} {Fore.YELLOW + Style.BRIGHT} est plein d'énergie.")
    if pokemon.faim == 0:
        statuses.append(f"{pokemon.name} {Fore.BLUE + Style.BRIGHT} est rassasié.")
    if pokemon.bonheur == pokemon.bonheurmax:
        statuses.append(f"{pokemon.name} {Fore.MAGENTA + Style.BRIGHT}  est heureux.")
    if pokemon.condition == "Empoisonnement":
        statuses.append(f"{pokemon.name} {Fore.MAGENTA + Style.BRIGHT} est empoisonné.")
    if pokemon.condition == "Paralysie":
        statuses.append(f"{pokemon.name} {Fore.YELLOW + Style.BRIGHT} est paralysé.")
    if pokemon.condition == "Sommeil":
        statuses.append(f"{pokemon.name} {Fore.CYAN + Style.BRIGHT} est endormi.")
    if pokemon.condition == "Confusion":
        statuses.append(f"{pokemon.name} {Fore.BLACK + Style.BRIGHT} est confus.")
    
    

    if not statuses:
        print("Aucun statut actuel")
    for status in statuses:
        print(status)
        
def print_action(action):
    if action == 'Manger':
        print(f"{Fore.RED + Style.BRIGHT}vous avez mangé")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez perder 10 points de faim")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 5 points de bonheur")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 3 points d'énergie")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 2 points de santé")
    elif action == 'Dormir':
        print(f"{Fore.BLUE + Style.BRIGHT}vous avez dormi")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 10 points d'énergie")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 5 points de bonheur")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 3 points de faim")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 2 points de santé")
        print(f"{Fore.GREEN + Style.BRIGHT}En dormant, vous avez récupéré de votre condition")
    elif action == 'Jouer':
        print(f"{Fore.YELLOW + Style.BRIGHT}vous avez joué")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 10 points de bonheur")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez perdu 5 points d'énergie")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 5 points de faim")
    elif action == 'Rien':
        print(f"{Fore.WHITE + Style.BRIGHT}vous n'avez rien fait")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez perdu 5 points de bonheur")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez perdu 3 points d'énergie")
        print(f"{Fore.GREEN + Style.BRIGHT}vous avez gagné 6 points de faim")
    else:
        print(f"{Fore.RED + Style.BRIGHT}Action inconnue")
        
def get_ordered_actions():
    actions = [method for method in dir(Action) if callable(getattr(Action, method)) and not method.startswith("__")]
    order = ['Manger', 'Dormir', 'Jouer', 'Rien']
    return sorted(actions, key=lambda x: order.index(x) if x in order else len(order))

    