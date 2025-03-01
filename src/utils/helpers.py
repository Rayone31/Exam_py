from models.action import Action

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_status(pokemon):
    statuses = []
    if pokemon.health <= 0:
        statuses.append(f"{pokemon.name} est KO.")
    if pokemon.energie <= 0:
        statuses.append(f"{pokemon.name} est fatigué.")
    if pokemon.faim >= 100:
        statuses.append(f"{pokemon.name} a faim.")
    if pokemon.bonheur <= 0:
        statuses.append(f"{pokemon.name} est malheureux.")
    if pokemon.level >= 100:
        statuses.append(f"{pokemon.name} level Max.")
    if pokemon.experience == 0 and pokemon.level > 1:
        statuses.append(f"{pokemon.name} est monté de 1 niveau.")
    if pokemon.health == pokemon.healthmax:
        statuses.append(f"{pokemon.name} est en pleine forme.")

    if not statuses:
        print("Aucun statut actuel")
    for status in statuses:
        print(status)
        
def print_action(action):
    if action == 'eat':
        print("vous avez mangé")
        print("vous avez perder 10 points de faim")
        print("vous avez gagné 5 points de bonheur")
        print("vous avez gagné 3 points d'énergie")
        print("vous avez gagné 2 points de santé")
    elif action == 'sleep':
        print("vous avez dormi")
        print("vous avez gagné 10 points d'énergie")
        print("vous avez gagné 5 points de bonheur")
        print("vous avez gagné 3 points de faim")
        print("vous avez gagné 2 points de santé")
    elif action == 'play':
        print("vous avez joué")
        print("vous avez gagné 10 points de bonheur")
        print("vous avez perdu 5 points d'énergie")
        print("vous avez gagné 5 points de faim")
    elif action == 'Rien':
        print("vous n'avez rien fait")
        print("vous avez perdu 5 points de bonheur")
        print("vous avez perdu 3 points d'énergie")
        print("vous avez gagné 6 points de faim")
    else:
        print("Action inconnue")
        
def get_ordered_actions():
    actions = [method for method in dir(Action) if callable(getattr(Action, method)) and not method.startswith("__")]
    order = ['eat', 'sleep', 'play', 'Rien']
    return sorted(actions, key=lambda x: order.index(x) if x in order else len(order))

    