# Skill class
class Skill:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def use(self):
        print(f"{self.name} used! It deals {self.damage} damage.")