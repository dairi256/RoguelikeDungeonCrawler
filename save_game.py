import os
import json
import pickle

class SaveGame:
    def __init__(self):
        self.save_files = []

    def add_save(self, game_data):
        save_file = "save_{}.json".format(len(self.save_files) + 1)
        self.save_files.append(save_file)
        with open(save_file, "w") as f:
            json.dump(game_data, f)

    def load_save(self, save_number):
        if save_number <= len(self.save_files):
            save_file = self.save_files[save_number - 1]
            with open(save_file, "r") as f:
                return json.load(f)
        else:
            return None

    def delete_save(self, save_number):
        if save_number <= len(self.save_files):
            save_file = self.save_files[save_number - 1]
            os.remove(save_file)
            del self.save_files[save_number - 1]
        else:
            print("No save file exists at that number.")

    def list_saves(self):
        print("Available saves:")
        for i, save_file in enumerate(self.save_files, 1):
            print(f"{i}. {save_file}")

def save_game(game_data):
    save_game = SaveGame()
    save_game.add_save(game_data)
    print("Game saved successfully!")

def load_game(save_number):
    save_game = SaveGame()
    loaded_game = save_game.load_save(save_number)
    if loaded_game:
        return loaded_game
    else:
        return None

def delete_game(save_number):
    save_game = SaveGame()
    save_game.delete_save(save_number)

if __name__ == "__main__":
    game_data = {"player": {"health": 100}, "level": 1}
    save_game(game_data)
    game_data = load_game(1)
    print(game_data)