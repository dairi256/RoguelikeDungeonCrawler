import random
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.attack_power = 20
        self.accuracy = 0.8
        self.critical_hit_chance = 0.2

    def move(self, x, y):
        self.x += x
        self.y += y

    def attack(self, enemy):
        damage = 0
        if random.random() < self.accuracy:
            damage = int(self.attack_power * (1 + random.random() * 0.5))
            if random.random() < self.critical_hit_chance:
                damage *= 2
                print("Critical hit!")
        print(f"Player attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)