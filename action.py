# action.py

import random

class Action:
    def __init__(self, name, base_initiative, base_damage, damage_mod, energy_cost, hit_chance_modifier, isSpell):
        self.name = name
        self.base_initiative = base_initiative
        self.base_damage = base_damage
        self.damage_mod = damage_mod
        self.energy_cost = energy_cost
        self.hit_chance_modifier = hit_chance_modifier
        self.isSpell = isSpell

    def calculate_damage(self, gladiator):
        # Formula for calculating damage based on gladiator's attributes
        if (self.isSpell):
            damage = (gladiator.int_ * self.damage_mod) + self.base_damage
        else:
            damage = (gladiator.str_ * self.damage_mod) + self.base_damage
        return damage

    def calculate_initiative(self, gladiator):
        # Formula for calculating initiative based on gladiator's attributes
        initiative = self.base_initiative - (gladiator.agi * 1.25)
        return initiative

    def perform_action(self, gladiator):
        # Check if the gladiator has enough energy for the action
        if gladiator.sp < self.energy_cost:
            print(f"{gladiator.name} does not have enough energy to perform {self.name}. RESTING")
            gladiator.sp += gladiator.sp_regen
            if (gladiator.sp_regen > 0):
                gladiator.sp_regen -= 1
            return 0  # Return 0 damage if not enough energy
            

        # Calculate damage and initiative
        damage = self.calculate_damage(gladiator)
        initiative = self.calculate_initiative(gladiator)

        # Simulate hit chance
        hit_chance = 80 + self.hit_chance_modifier * gladiator.agi
        if random.randint(1, 100) <= hit_chance:
            print(f"{gladiator.name} successfully performs {self.name} \n DAMAGE: {damage} \n INITATIVE: {initiative}")
            gladiator.sp -= self.energy_cost  # Deduct energy cost
            return damage
        else:
            print(f"{self.name} by {gladiator.name} misses!")
            return 0  # Return 0 damage if the action misses