import random

class Event:
    def __init__(self, name, event_type, action=None):
        self.name = name
        self.event_type = event_type
        self.action = action

    def trigger(self, pokemon):
        if self.event_type == 'passive':
            return self._trigger_passive(pokemon)
        elif self.event_type == 'active':
            return self._trigger_active()
        else:
            raise ValueError("Unknown event type")

    def _trigger_passive(self, pokemon):
        if self.name == "Votre Pokémon a trouvé un objet":
            return self._found_item(pokemon)
        elif self.name == "Votre Pokémon a trouvé une baie":
            return self._found_baia(pokemon)
        return f"Événement passif déclenché: {self.name}"

    def _trigger_active(self):
        return f"Événement actif déclenché: {self.name}. Action requise: {self.action}"

    def _found_item(self, pokemon):
        items = ["Petite Potion", "Moyenne Potion", "Grande Potion", "Potion Max", "Antidote"]
        weights = [0.4, 0.2, 0.15, 0.05, 0.2]
        found_item = random.choices(items, weights=weights, k=1)[0]
        pokemon.add_to_inventory(found_item)
        return f"Votre Pokémon a trouvé un objet: {found_item}"
    
    def _found_baia(self, pokemon):
        baies = ["Kébia", "Sitrus", "Mepo", "Wiki", "Framby"]
        weights = [0.2, 0.2, 0.2, 0.1, 0.3]
        found_baie = random.choices(baies, weights=weights, k=1)[0]
        
        if pokemon.condition == "Normal":
            if found_baie == "Kébia":
                pokemon.condition = "Empoisonnement"
            elif found_baie == "Sitrus":
                pokemon.condition = "Paralysie"
            elif found_baie == "Mepo":
                pokemon.condition = "Sommeil"
            elif found_baie == "Wiki":
                pokemon.condition = "Confusion"
            elif found_baie == "Framby":
                pokemon.condition = "Normal"
                pokemon.health = min(pokemon.health + 25, pokemon.healthmax)
        elif found_baie == "Framby":
            pokemon.condition = "Normal"
            pokemon.health = min(pokemon.health + 25, pokemon.healthmax)
        
        return f"Votre Pokémon a trouvé une baie: {found_baie} et l'a mangée"

def generate_random_event():
    events = [
        Event("Rien d'anormal n'est arrivé", "passive"),
        Event("Votre Pokémon a trouvé un objet", "passive"),
        Event("Votre Pokémon a trouvé une baie", "passive"),
        Event("Un dresseur veut vous combattre", "active", "Combattre le dresseur")
    ]
    weights = [0.7, 0.1, 0.12, 0.07]  
    return random.choices(events, weights=weights, k=1)[0]