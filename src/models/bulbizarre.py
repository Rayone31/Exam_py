from models.pokemon import Pokemon
from models.action import Action
from models.event import Event

class Bulbizarre(Pokemon, Action, Event):
    def __init__(self, name,level):
        super().__init__(name, "Bulbizarre", "Plante", 100, level, 10, 30)