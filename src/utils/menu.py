from utils.helpers import print_status, get_ordered_actions, print_action, clear

selected_action = None

def menus(pokemon, event_name=None):
    global selected_action
    actions = get_ordered_actions()
    
    print("=============================================== Evenement =======================================================")
    if event_name:
        print(f"Événement passif: {event_name}")
    else:
        print("Aucun événement passif pour le moment.")
    
    print("=============================================== Information =====================================================")
    if selected_action:
        print_action(selected_action)
    else:
        print("Aucune action sélectionnée pour le moment.")
    
    print("=============================================== Personnage ======================================================")
    print(pokemon)

    print("================================================= Status ========================================================")
    print_status(pokemon)

    print("================================================= Action ========================================================")
    for i, action in enumerate(actions, 1):
        print(f"{i}. {action.capitalize()}")
    print("_________________________________________________________________________________________________________________")
    choice = int(input("Enter your choice: "))
    selected_action = actions[choice - 1]
    
    clear()
    return choice, selected_action