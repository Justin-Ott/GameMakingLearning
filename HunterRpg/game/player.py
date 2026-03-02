# Player class (stats, skills, exp)
class Player:
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.health = 100
        self.mana = 50
        self.strength = 10
        self.agility = 10
        self.intelligence = 10
        self.skills = []
        self.inventory = []

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.exp_to_next_level():
            self.level_up()

    def exp_to_next_level(self):
        return self.level * 100

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.health += 20
        self.mana += 10
        self.strength += 5
        self.agility += 5
        self.intelligence += 5