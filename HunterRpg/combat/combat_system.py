# Battle mechanics
class CombatSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_attack(self):
        damage = self.player.attack()
        self.enemy.take_damage(damage)
        print(f"You attack the {self.enemy.name} for {damage} damage!")

    def enemy_attack(self):
        damage = self.enemy.attack()
        self.player.take_damage(damage)
        print(f"The {self.enemy.name} attacks you for {damage} damage!")

    def is_combat_over(self):
        return self.player.is_defeated() or self.enemy.is_defeated()

    def get_winner(self):
        if self.player.is_defeated():
            return "Enemy"
        elif self.enemy.is_defeated():
            return "Player"
        else:
            return None