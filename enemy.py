import random
import math
class Dragon:
    def __init__(self):
        self.name = "Dragon"
        self.health = 100
        self.attack = 20

class Orc:
    def __init__(self):
        self.name = "Orc"
        self.health = 80
        self.attack = 15

class GiantSpider:
    def __init__(self):
        self.name = "Giant Spider"
        self.health = 70
        self.attack = 12

class Zombie:
    def __init__(self):
        self.name = "Zombie"
        self.health = 60
        self.attack = 10

class Werewolf:
    def __init__(self):
        self.name = "Werewolf"
        self.health = 90
        self.attack = 18

class Troll:
    def __init__(self):
        self.name = "Troll"
        self.health = 120
        self.attack = 22

class Golem:
    def __init__(self):
        self.name = "Golem"
        self.health = 110
        self.attack = 20

class Mummy:
    def __init__(self):
        self.name = "Mummy"
        self.health = 100
        self.attack = 18

class Vampire:
    def __init__(self):
        self.name = "Vampire"
        self.health = 80
        self.attack = 15

class Ghost:
    def __init__(self):
        self.name = "Ghost"
        self.health = 60
        self.attack = 10

class Enemy:
    def __init__(self):
        self.name = "Enemy"
        self.health = 50
        self.attack = 10
        self.ai = EnemyAI()

    def attack_player(self):
        self.ai.update(self)

    def set_player_position(self, player_position):
        self.ai.set_player_position(player_position)
class EnemyAI:
    def __init__(self, state=None):
        self.state = state if state else "CHASE"
        self.player_distance = 0
        self.attack_range = 5
        self.retreat_distance = 10
        self.health = 100
        self.injured = False

    def update(self, player_position):
        if self.state == "CHASE":
            if self.player_distance <= self.attack_range:
                print("The enemy is attacking the player!")
                self.state = "ATTACK"
            elif self.player_distance >= self.retreat_distance:
                print("The enemy is retreating from the player!")
                self.state = "RETREAT"
            else:
                print("The enemy is still chasing the player!")
                if not random.random() < 0.5:
                    self.state = "ATTACK"
        elif self.state == "ATTACK":
            print("The enemy is attacking the player!")
            if not random.random() < 0.5:
                print("The enemy is retreating from the player!")
                self.state = "RETREAT"
            else:
                print("The enemy is still attacking the player!")
                if self.injured:
                    self.state = "INJURED"
        elif self.state == "RETREAT":
            print("The enemy is retreating from the player!")
            if random.random() < 0.5:
                print("The enemy is retreating from the player!")
                self.state = "RETREAT"
            else:
                print("The enemy is still retreating from the player!")
        elif self.state == "INJURED":
            print("The enemy is injured and stumbling towards the player!")
            if random.random() < 0.5:
                print("The enemy is stumbling towards the player!")
                if self.player_distance <= self.attack_range:
                    self.state = "ATTACK"
            else:
                print("The enemy is slowly retreating from the player!")

        if not self.injured and self.health < 50:
            print("The enemy is injured and falling to its knees!")
            self.injured = True
        elif self.injured and random.random() < 0.5:
            print("The enemy is slowly recovering from its injury!")
            self.injured = False

    def set_player_position(self, player_position):
        self.player_position = player_position

    def get_player_distance(self, player_position):
        return math.sqrt((player_position[0] - self.player_position[0]) ** 2 + (player_position[1] - self.player_position[1]) ** 2)

    def get_state(self):
        return self.state