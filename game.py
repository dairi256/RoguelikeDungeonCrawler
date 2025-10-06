import random
import sys

sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/player.py")
sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/item.py")
sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/enemy.py")
sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/damage_calculator.py")
sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/game_world.py")
sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/save_game.py")
sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/start_menu.py")
sys.path.append("D:/Personal Python Projects/Roguelike Dungeon Crawler/character.py")

import player
import item
import enemy
import damage_calculator
import gameworld
import save_game
import start_menu
import character



class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def get_adjacent_rooms(self):
        adjacent_rooms = []
        if random.random() < 0.5:
            adjacent_rooms.append(Room(self.x - 1, self.y))
        if random.random() < 0.5:
            adjacent_rooms.append(Room(self.x + 1, self.y))
        if random.random() < 0.5:
            adjacent_rooms.append(Room(self.x, self.y - 1))
        if random.random() < 0.5:
            adjacent_rooms.append(Room(self.x, self.y + 1))
        return adjacent_rooms

class Game:
    def __init__(self):
        self.rooms = []
        self.current_room = None
        self.player = player.Player()

    def generate_floor(self):
        for i in range(20):
            for j in range(20):
                room = Room(i, j)
                if random.random() < 0.2:
                    room.add_enemy(enemy.Enemy("Goblin"))
                if random.random() < 0.1:
                    room.add_enemy(enemy.GiantSpider())
                if random.random() < 0.05:
                    room.add_enemy(enemy.Zombie())
                if random.random() < 0.05:
                    room.add_enemy(enemy.Werewolf())
                self.rooms.append(room)

    def start_game(self):
        self.generate_floor()
        for room in self.rooms:
            if random.random() < 0.2:
                room.enemies[0].add_enemy(enemy.Goblin())
                room.enemies[0].add_enemy(enemy.GiantSpider())
                room.enemies[0].add_enemy(enemy.Zombie())
                room.enemies[0].add_enemy(enemy.Werewolf())
        for i in range(20):
            for j in range(20):
                if random.random() < 0.2:
                    if i > 0 and random.random() < 0.5:
                        self.rooms[i-1][j].get_adjacent_rooms().append(self.rooms[i][j])
                    if i < 19 and random.random() < 0.5:
                        self.rooms[i+1][j].get_adjacent_rooms().append(self.rooms[i][j])
                    if j > 0 and random.random() < 0.5:
                        self.rooms[i][j-1].get_adjacent_rooms().append(self.rooms[i][j])
                    if j < 19 and random.random() < 0.5:
                        self.rooms[i][j+1].get_adjacent_rooms().append(self.rooms[i][j])
        current_room = random.choice(self.rooms)
        self.current_room = current_room
        while True:
            print(f"You are in room {current_room.x}, {current_room.y}.")
            for enemy in current_room.enemies:
                print(f"There is a {enemy.name} in the room!")
            print("\n")
            print(" Floor:")
            for i in range(20):
                for j in range(20):
                    if i == current_room.x and j == current_room.y:
                        print("#", end=" ")
                    elif i == current_room.x and j == current_room.y - 1:
                        print("^", end=" ")
                    elif i == current_room.x and j == current_room.y + 1:
                        print("v", end=" ")
                    elif i == current_room.x - 1 and j == current_room.y:
                        print("<", end=" ")
                    elif i == current_room.x + 1 and j == current_room.y:
                        print(">", end=" ")
                    else:
                        print(" ", end=" ")
                print()
            response = input("Do you want to move (n/s/e/w) or fight? (f): ")
            if response.lower() == "n":
                if current_room.x > 0 and current_room.get_adjacent_rooms()[0] in self.rooms:
                    current_room = current_room.get_adjacent_rooms()[0]
                else:
                    print("You can't go that way!")
            elif response.lower() == "s":
                if current_room.x < 19 and current_room.get_adjacent_rooms()[1] in self.rooms:
                    current_room = current_room.get_adjacent_rooms()[1]
                else:
                    print("You can't go that way!")
            elif response.lower() == "e":
                if current_room.y < 19 and current_room.get_adjacent_rooms()[2] in self.rooms:
                    current_room = current_room.get_adjacent_rooms()[2]
                else:
                    print("You can't go that way!")
            elif response.lower() == "w":
                if current_room.y > 0 and current_room.get_adjacent_rooms()[3] in self.rooms:
                    current_room = current_room.get_adjacent_rooms()[3]
                else:
                    print("You can't go that way!")
            elif response.lower() == "f":
                for enemy in current_room.enemies:
                    enemy.attack(self.player)
                self.player.attack(current_room.enemies[0])
                if not self.player.is_alive():
                    print("You died! Game over.")
                    break
            else:
                print("Invalid command!")

    def main(self):
        self.start_game()

if __name__ == "__main__":
    game = Game()
    game.main()