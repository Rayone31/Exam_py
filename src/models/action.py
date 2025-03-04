import random
class Action:

    def Manger(self):
        self.faim = max(0, self.faim - 10)
        self.bonheur = min(self.bonheurmax, self.bonheur + 2)
        self.energie = min(self.energiemax, self.energie + 1)
        self.health = min(self.healthmax, self.health + 2)
        random_number = random.randint(1, 100)
        if random_number <= 3:
            self.condition = "Empoisonnement"

    def Dormir(self):
        self.energie = min(self.energiemax, self.energie + 10)
        self.bonheur = min(self.bonheurmax, self.bonheur + 3)
        self.faim = min(self.faimmax, self.faim + 5)
        self.health = min(self.healthmax, self.health + 2)
        self.condition = "Normal"

    def Jouer(self):
        self.bonheur = min(self.bonheurmax, self.bonheur + 10)
        self.energie = max(0, self.energie - 5)
        self.faim = min(self.faimmax, self.faim + 7)
        random_number = random.randint(1, 100)
        if random_number <= 3:
            self.condition = "Confusion"

    
    def Rien(self):
        self.bonheur = max(0, self.bonheur - 5)
        self.energie = max(0, self.energie - 3)
        self.faim = min(self.faimmax, self.faim + 6)
        random_number = random.randint(1, 100)
        if random_number <= 3:
            self.condition = "Sommeil"

