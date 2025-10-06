import random
class Ingredient:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Item:
    def __init__(self):
        self.name = "Item"
        self.description = "A generic item"

class Potion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Potion"
        self.description = "A healing potion"
        self.heals = 20

class HealthPotion(Potion):
    def __init__(self):
        super().__init__()
        self.name = "Health Potion"
        self.description = "A potion that restores 20 health points"
        self.heals = 20
        self.ingredients = [Ingredient("Herb", "A magical herb"), Ingredient("Water", "Fresh water")]

class ManaPotion(Potion):
    def __init__(self):
        super().__init__()
        self.name = "Mana Potion"
        self.description = "A potion that restores 20 mana points"
        self.heals = 0
        self.ingredients = [Ingredient("Mystic Crystal", "A magical crystal"), Ingredient("Moonstone", "A piece of moonstone")]

class ShieldPotion(Potion):
    def __init__(self):
        super().__init__()
        self.name = "Shield Potion"
        self.description = "A potion that gives you temporary shield"
        self.heals = 10
        self.ingredients = [Ingredient("Dragon's Breath", "A dragon's breath scale"), Ingredient("Unicorn Tears", "Tears of a unicorn")]

class HealingPotion(Potion):
    def __init__(self):
        super().__init__()
        self.name = "Healing Potion"
        self.description = "A potion that heals you for 10 health points per second"
        self.heals = 10
        self.ingredients = [Ingredient("Golden Flower", "A rare golden flower"), Ingredient("Holy Water", "Holy water")]

class Armor(Item):
    def __init__(self):
        super().__init__()
        self.name = "Armor"
        self.description = "A set of leather armor"
        self.defense = 5

class IronArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Iron Armor"
        self.description = "A set of iron armor"
        self.defense = 10
        self.ingredients = [Ingredient("Iron Ore", "Iron ore"), Ingredient("Leather Strips", "Leather strips")]

class SteelArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Steel Armor"
        self.description = "A set of steel armor"
        self.defense = 15
        self.ingredients = [Ingredient("Steel Ingot", "Steel ingot"), Ingredient("Steel Plate", "Steel plate")]

class CraftableItem:
    def __init__(self, item_name, item_class, chance=10):
        self.item_name = item_name
        self.item_class = item_class
        self.chance = chance

class Game1:
    def __init__(self):
        self.craftable_items = [
            CraftableItem("Health Potion", HealthPotion),
            CraftableItem("Mana Potion", ManaPotion),
            CraftableItem("Shield Potion", ShieldPotion),
            CraftableItem("Healing Potion", HealingPotion),
            CraftableItem("Iron Armor", IronArmor, chance=20),
            CraftableItem("Steel Armor", SteelArmor, chance=30)
        ]

    def generate_item(self):
        random_number = random.randint(1, 100)
        for item in self.craftable_items:
            if random_number <= item.chance:
                return item.item_class()
                break
        return None

game = Game1()
generated_item = game.generate_item()
print(generated_item)