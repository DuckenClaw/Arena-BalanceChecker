# main.py

from gladiator import Gladiator
from action import Action

# ARGS = ("name", str_, agi, vit, sta, int_)
gladiator1 = Gladiator("AaaA", 5, 5, 5, 5, 5)
gladiator2 = Gladiator("VvvV", 5, 5, 5, 5, 5)

# Action ARGS = ("name", base_initiative, base_damage, damage_mod, energy_cost, hit_chance_modifier, isSpell)
quick_attack = Action("Quick Attack", 13, 5, 2, 2, 2, False)
precise_attack = Action("Precise Attack", 18, 10, 3, 4, 2, False)
heavy_attack = Action("Heavy Attack", 23, 20, 4, 6, 2, False)
fire_ball = Action("Fireball", 20, 0, 5, 5, 20, True)
water_burst = Action("Water Burst", 20, 5, 3, 5, 20, True)
earth_catapult = Action("Earth Catapult", 20, 10, 2, 5, 20, True)

def execute_turn(attacker, defender, action):
    print(f"\n{attacker.name}'s Turn:")
    damage = action.perform_action(attacker)
    defender.hp = defender.hp - damage
    print(f"{defender.name} receives {damage} damage.")

def simulate_battle(gladiator1, gladiator2, action1, action2):
    round_count = 1

    while gladiator1.hp > 0 and gladiator2.hp > 0:
        print(f"\n--- Round {round_count} ---")

        # Order of actions based on initiative
        if action1.calculate_initiative(gladiator1) <= action2.calculate_initiative(gladiator2):
            print(f"\n{gladiator1.name} won initiative!")
            execute_turn(gladiator1, gladiator2, action1)
            if gladiator1.hp <= 0:
                print(f"\n{gladiator2.name} wins!")
                break
            elif gladiator2.hp <= 0:
                print(f"\n{gladiator1.name} wins!")
                break
            execute_turn(gladiator2, gladiator1, action2)
        else:
            print(f"\n{gladiator2.name} won initiative!")
            execute_turn(gladiator2, gladiator1, action2)
            if gladiator1.hp <= 0:
                print(f"\n{gladiator2.name} wins!")
                break
            elif gladiator2.hp <= 0:
                print(f"\n{gladiator1.name} wins!")
                break
            execute_turn(gladiator1, gladiator2, action1)

        # log current HP
        print(f"\nCurrent HP:")
        print(f"{gladiator1.name}: {gladiator1.hp} HP")
        print(f"{gladiator2.name}: {gladiator2.hp} HP")

        round_count += 1



# Simulate the battle
simulate_battle(gladiator1, gladiator2, precise_attack, fire_ball)