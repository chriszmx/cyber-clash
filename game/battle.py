import random
import time
from utility import twp


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = self.first_go()

    def first_go(self):
        go = random.randint(0, 2)
        if go == 0:
            return self.player2
        else:
            return self.player1

    def battle_loop(self):
        while self.player1.hp > 0 and self.player2.hp > 0:
            twp(f"\n{self.turn.name}'s turn!")
            if self.turn == self.player1:
                action = int(input(f"{self.player1.name}, please choose an action:\n) Normal Attack\n2) Special Attack\n3) Heal"))
                if action == 1:
                    player_normal_attack = self.player1.normal_atk()
                    self.player2.hp -= player_normal_attack
                    self.player1.energy += 10
                    time.sleep(1)
                    twp(f"\n{self.player1.name} just did {player_normal_attack} damage!")
                    twp(f"{self.player1.name} now has {self.player1.hp} health and {self.player1.energy} energy")
                    time.sleep(1)
                    twp(f"The computer now has {self.player2.hp} and {self.player2.energy} energy")
                    self.turn = self.player2
                elif action == 2 and self.player1.energy >= 20:
                    player_special_attack = self.player1.spec_attack()
                    self.player2.hp -= player_special_attack
                    self.player1.energy -= 20
                    time.sleep(1)
                    twp(f'\n{self.player1.name} just did {player_special_attack} damage!')
                    twp(f'{self.player1.name} now has {self.player1.hp} health and {self.player1.energy} energy')
                    time.sleep(1)
                    twp(f'The computer now has {self.player2.hp} and {self.player2.energy} energy')
                    self.turn = self.player2
                elif action == 3 and self.player1.energy >= 15:
                    player_heal = self.player1.heal()
                    self.player1.hp += player_heal
                    self.player1.energy -= 15
                    time.sleep(1)
                    twp(f'\n{self.player1.name} just healed themselves for {player_heal}!')
                    twp(f"\n{self.player1.name} has {self.player1.hp} health and {self.player1.energy} energy")
                    self.turn = self.player2
                    time.sleep(1)
                elif action == 2 or action == 3 and self.player1.energy < 15:
                    twp(f'\n{self.player1.name} you have {self.player1.hp} health and {self.player1.energy} energy')
                    twp(f'\n{self.player1.name} your energy is too low, please choose 1) Normal Attack: ')
                else:
                    twp("Please enter a correct action! It's simple. 1...2....or 3.....")
            else:
                if self.player2.energy >= 20:
                    comp_spec_attack = self.player2.spec_attack()
                    self.player1.hp -= comp_spec_attack
                    self.player2.energy -= 20
                    time.sleep(1)
                    twp(f'The computer now has {self.player2.hp} health and {self.player2.energy} energy')
                    self.turn = self.player1
                elif self.player2.hp < 50 and self.player2.energy >= 15:
                    comp_healing = self.player2.heal()
                    self.player2.hp += comp_healing
                    self.player2.energy -= 15
                    time.sleep(1)
                    twp(f'The computer just healed themselves for {comp_healing}!')
                    twp(f'{self.player1.name} now has {self.player1.hp} health and {self.player1.energy} energy')
                    time.sleep(1)
                    twp(f'The computer now has {self.player2.hp} health and {self.player2.energy} energy')
                    self.turn = self.player1
                else:
                    comp_norm_attack = self.player2.normal_atk()
                    self.player1.hp -= comp_norm_attack
                    self.player2.energy -= 10
                    time.sleep(1)
                    twp(f'\nComp just did {comp_norm_attack} damage!')
                    twp(f'\n{self.player1.name} now has {self.player1.hp} health and {self.player1.energy} energy')
                    twp(f'The computer now has {self.player2.hp} health and {self.player2.energy} energy')
                    self.turn = self.player1
                # rest of p1 logic here
                # dont forget to update the turn at end of each turn
            # Your battle loop logic goes here
            # Replace all instances of "player_hp", "player_energy", "comp_hp", "comp_energy"
            # with "self.player1.hp", "self.player1.energy", "self.player2.hp", "self.player2.energy"
            # Replace all instances of "name" with "self.player1.name"
            # Replace all instances of "Comp" with "self.player2.name"

        if self.player1.hp <= 0:
            twp(f'{self.player2.name} has won this round!')
        elif self.player2.hp <= 0:
            twp(f'{self.player1.name} has won this round!')
