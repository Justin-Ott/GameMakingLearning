# Enemy/buster class
class Buster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        print(f"{self.name} attacks and deals {self.damage} damage!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Remaining health: {self.health}")