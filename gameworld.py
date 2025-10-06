import random
class GameWorld:
    def __init__(self):
        self.player_position = [4,2]
        self.enemy_position = [2, 3]
        self.item_position = [3, 2]
        self.finish_position = [4, 4]
        self.game_world = self.generate_game_world()

    def generate_game_world(self):
        game_world = []
        for i in range(8):
            row = []
            for j in range(8):
                if i == 0 or i == 7:
                    row.append("#")
                elif j == 0 or j == 7:
                    row.append("#")
                elif [i, j] == self.player_position:
                    row.append("P")
                elif [i, j] == self.enemy_position:
                    row.append("E")
                elif [i, j] == self.item_position:
                    row.append("I")
                elif [i, j] == self.finish_position:
                    row.append("F")
                else:
                    row.append(random.choice(["#", " "]))
            game_world.append(row)
        return game_world

    def print_game_world(self):
        for row in self.game_world:
            print(" ".join(row))

    def move_player(self, direction):
        if direction == "up":
            if self.player_position[0] > 0:
                self.player_position[0] -= 1
        elif direction == "down":
            if self.player_position[0] < 7:
                self.player_position[0] += 1
        elif direction == "left":
            if self.player_position[1] > 0:
                self.player_position[1] -= 1
        elif direction == "right":
            if self.player_position[1] < 7:
                self.player_position[1] += 1

        # Update game world
        new_game_world = self.generate_game_world()
        for i in range(8):
            for j in range(8):
                if [i, j] == self.player_position:
                    new_game_world[i][j] = "P"
                else:
                    new_game_world[i][j] = self.game_world[i][j]
        self.game_world = new_game_world

    def is_player_at_finish(self):
        return self.player_position == self.finish_position

    def is_player_at_enemy(self):
        return self.player_position == self.enemy_position

    def is_player_at_item(self):
        return self.player_position == self.item_position

# Create a new game world
game = GameWorld()

# Print the initial game world
game.print_game_world()

# Move the player
while True:
    direction = input("Enter a direction (up, down, left, right): ")
    game.move_player(direction)
    game.print_game_world()
    if game.is_player_at_finish():
        print("You have reached the finish!")
        break
    elif game.is_player_at_enemy():
        print("You have encountered the enemy!")
        # Add enemy logic here
    elif game.is_player_at_item():
        print("You have found an item!")
        # Add item logic here