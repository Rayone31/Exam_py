from models.pokemon import Pokemon
from models.action import Action
from models.event import Event


class Salameche(Pokemon, Action, Event):
    def __init__(self, name,level):
        super().__init__(name, "Salameche",'Feu',100, level, 10, 30)