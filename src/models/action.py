class Action:

    def eat(self):
        self.faim = max(0, self.faim - 10)
        self.bonheur = min(self.bonheurmax, self.bonheur + 5)
        self.energie = min(self.energiemax, self.energie + 3)
        self.health = min(self.healthmax, self.health + 2)

    def sleep(self):
        self.energie = min(self.energiemax, self.energie + 10)
        self.bonheur = min(self.bonheurmax, self.bonheur + 5)
        self.faim = min(self.faimmax, self.faim + 3)
        self.health = min(self.healthmax, self.health + 2)

    def play(self):
        self.bonheur = min(self.bonheurmax, self.bonheur + 10)
        self.energie = max(0, self.energie - 5)
        self.faim = min(self.faimmax, self.faim + 5)
    
    def Rien(self):
        self.bonheur = max(0, self.bonheur - 5)
        self.energie = max(0, self.energie - 3)
        self.faim = min(self.faimmax, self.faim + 6)

