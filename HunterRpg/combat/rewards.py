# Combat rewards
class Rewards:
    def __init__(self, experience=0, items=None):
        self.experience = experience
        self.items = items if items is not None else []

    def add_experience(self, amount):
        self.experience += amount

    def add_item(self, item):
        self.items.append(item)

    def claim_rewards(self, player):
        player.gain_experience(self.experience)
        for item in self.items:
            player.add_to_inventory(item)