from models.pokemon import Pokemon
from models.action import Action
from models.event import Event

class Carapuce(Pokemon, Action, Event):
    def __init__(self, name):
        super().__init__(name, "Carapuce", 100, 1, 10, 30)