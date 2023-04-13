import time


def game_intro():
    # game intro logic here
    pass


def twp(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(.01)
    print()


def display_player_stats(player):
    print(f"\n{player.name}'s Stats:")
    print(f"Health: {player.hp}")
    print(f"Energy: {player.energy}")
    print(f"Total Damage Dealt: {player.total_damage_dealt}")
    print(f"Total Damage Taken: {player.total_damage_taken}")
    print(f"Battles Won: {player.battles_won}")
