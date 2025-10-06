import random

class DamageCalculator:
    def __init__(self, attack_power, critical_hit, elemental_bonus, absorption_rate, reflect_chance, magical_attack, physical_attack, elemental_weakness, elemental_resistance):
        self.attack_power = attack_power
        self.critical_hit = critical_hit
        self.elemental_bonus = elemental_bonus
        self.absorption_rate = absorption_rate
        self.reflect_chance = reflect_chance
        self.magical_attack = magical_attack
        self.physical_attack = physical_attack
        self.elemental_weakness = elemental_weakness
        self.elemental_resistance = elemental_resistance

    def calculate_damage(self, enemy_defense, enemy_resistance, enemy_absorption, enemy_reflect):
        base_damage = 0
        if self.magical_attack:
            base_damage = (self.attack_power * (1 + self.critical_hit) * (1 + self.elemental_bonus) * (1 + self.elemental_weakness))
        else:
            base_damage = (self.attack_power * (1 + self.critical_hit) * (1 + self.elemental_bonus))

        adjusted_damage = base_damage - (enemy_defense * (1 - enemy_resistance))
        absorbed_damage = adjusted_damage * self.absorption_rate
        reflected_damage = 0
        if enemy_reflect and random.random() < self.reflect_chance:
            reflected_damage = adjusted_damage - absorbed_damage
            absorbed_damage = 0

        damage = adjusted_damage - absorbed_damage + reflected_damage

        return damage

    def calculate_absorbed_damage(self, damage):
        return damage * self.absorption_rate

    def calculate_reflected_damage(self, damage):
        if random.random() < self.reflect_chance:
            return damage - self.calculate_absorbed_damage(damage)
        return 0

    def calculate_elemental_damage(self):
        return (self.attack_power * (1 + self.critical_hit)) * self.elemental_bonus

    def calculate_enemy_elemental_defense(self, enemy_resistance):
        return enemy_resistance * (self.elemental_bonus)

    def calculate_enemy_physical_defense(self, enemy_resistance):
        return enemy_resistance

    def calculate_enemy_magical_defense(self, enemy_resistance):
        return enemy_resistance

# Example usage
attack_power = 20
critical_hit = 0.5
elemental_bonus = 0.2
absorption_rate = 0.3
reflect_chance = 0.4
magical_attack = True
physical_attack = False
elemental_weakness = 0.2
elemental_resistance = 0.3
enemy_defense = 15
enemy_resistance = 0.3
enemy_absorption = 0.2
enemy_reflect = True

calculator = DamageCalculator(attack_power, critical_hit, elemental_bonus, absorption_rate, reflect_chance, magical_attack, physical_attack, elemental_weakness, elemental_resistance)
damage = calculator.calculate_damage(enemy_defense, calculator.calculate_enemy_magical_defense(enemy_resistance), enemy_absorption, enemy_reflect)
print(f"Damage: {damage:.2f}")
print(f"Absorbed Damage: {calculator.calculate_absorbed_damage(damage):.2f}")
print(f"Reflected Damage: {calculator.calculate_reflected_damage(damage):.2f}")
print(f"Elemental Damage: {calculator.calculate_elemental_damage():.2f}")
print(f"Enemy Elemental Defense: {calculator.calculate_enemy_elemental_defense(elemental_resistance):.2f}")
print(f"Enemy Physical Defense: {calculator.calculate_enemy_physical_defense(elemental_resistance):.2f}")
print(f"Enemy Magical Defense: {calculator.calculate_enemy_magical_defense(elemental_resistance):.2f}")