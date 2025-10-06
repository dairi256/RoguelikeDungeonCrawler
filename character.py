class Character:
    def __init__(self):
        self.name = "Character"
        self.health = 100
        self.mana = 100
        self.defense = 0
        self.inventory = []
        self.level = 1
        self.experience = 0
        self.experience_required = 100
        self.crafting_recipes = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item not found in inventory.")

    def use_item(self, item):
        if item in self.inventory:
            if isinstance(item,Potion):
                if item.heals > 0:
                    self.health += item.heals
                    print(f"Used {item.name} and gained {item.heals} health points.")
                else:
                    self.mana += item.heals
                    print(f"Used {item.name} and gained {item.heals} mana points.")
                self.remove_item(item)
            elif isinstance(item, Armor):
                self.defense = item.defense
                print(f"Used {item.name} and gained {item.defense} defense points.")
                self.remove_item(item)
            else:
                print("Invalid item type.")
        else:
            print("Item not found in inventory.")

    def level_up(self):
        if self.experience >= self.experience_required:
            self.level += 1
            self.experience_required *= 2
            self.health += 10
            self.mana += 10
            print(f"Level up! You are now level {self.level}.")
        else:
            print(f"You need {self.experience_required - self.experience} more experience points to level up.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"Gained {amount} experience points.")

    def craft_item(self, recipe_name):
        if recipe_name in [recipe.name for recipe in self.crafting_recipes]:
            recipe = next(recipe for recipe in self.crafting_recipes if recipe.name == recipe_name)
            if all(item in self.inventory for item in recipe.ingredients):
                for item in recipe.ingredients:
                    self.remove_item(item)
                if recipe.output not in [item.name for item in self.inventory]:
                    self.add_item(recipe.output)
                    print(f"Crafted {recipe.output}.")
                else:
                    print(f"Already have {recipe.output}.")
            else:
                print("Not enough ingredients to craft this item.")
        else:
            print("Recipe not found.")

class Item:
    def __init__(self, name, heals=0, defense=0, output=None, ingredients=None):
        self.name = name
        self.heals = heals
        self.defense = defense
        self.output = output
        self.ingredients = ingredients

class CraftingRecipe:
    def __init__(self, name, output, ingredients):
        self.name = name
        self.output = output
        self.ingredients = ingredients

class Player(Character):
    def __init__(self):
        super().__init__()
        self.name = "Player"