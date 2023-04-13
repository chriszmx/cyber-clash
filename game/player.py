import random


class Player:
    def __init__(self, name="Computer"):
        self.name = name
        self.hp = 100
        self.energy = 0
        self.total_damage_dealt = 0
        self.total_damage_taken = 0
        self.battles_won = 0

    def normal_atk(self):
        attack = random.randint(0, 15)
        return attack

    def spec_attack(self):
        spec_atk = random.randint(20, 40)
        return spec_atk

    def heal(self):
        healing = random.randint(5, 25)
        return healing


# rest of player class remains the same
