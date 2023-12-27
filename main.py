# main.py

from gladiator import Gladiator
from action import Action

# ARGS = ("name", str_, agi, vit, sta, int_)
gladiator1 = Gladiator("AaaA", 5, 9, 5, 5, 5)
gladiator2 = Gladiator("VvvV", 8, 5, 5, 5, 5)

# Action ARGS = ("name", base_initiative, base_damage, damage_mod, energy_cost, hit_chance_modifier)
quick_attack = Action("Quick Attack", 13, 5, 2, 2, 2)
precise_attack = Action("Precise Attack", 18, 10, 3, 4, 2)
heavy_attack = Action("Heavy Attack", 23, 20, 4, 6, 2)

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
simulate_battle(gladiator1, gladiator2, heavy_attack, precise_attack)