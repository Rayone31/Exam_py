import random

class Event:
    def __init__(self, name, event_type, action=None):
        self.name = name
        self.event_type = event_type
        self.action = action

    def trigger(self):
        if self.event_type == 'passive':
            return self._trigger_passive()
        elif self.event_type == 'active':
            return self._trigger_active()
        else:
            raise ValueError("Unknown event type")

    def _trigger_passive(self):
        # Actions automatiques pour les événements passifs
        return f"Événement passif déclenché: {self.name}"

    def _trigger_active(self):
        # Actions nécessitant une interaction pour les événements actifs
        return f"Événement actif déclenché: {self.name}. Action requise: {self.action}"

def generate_random_event():
    events = [
        Event("rien ne c'est passer", "passive"),
        Event("Votre Pokémon a trouvé un objet", "passive"),
        Event("Votre Pokémon a trouvé une baie", "passive"),
        Event("Votre Pokémon est tombé malade", "passive"),
        Event("Un dresseur veut vous combattre", "active", "Combattre le dresseur")
    ]
    return random.choice(events)

# Exemple d'utilisation
if __name__ == "__main__":
    event = generate_random_event()
    print(event.trigger())