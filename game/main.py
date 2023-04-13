from player import Player
from battle import Battle
from story import story_intro, random_story_event
from utility import game_intro, display_stats


def main():
    game_intro()

    player_name = input('Please enter your name:\n    ')
    player1 = Player(player_name)
    player2 = Player('Comp')  # You can set the name of the computer player here

    story_intro(player_name)

    battle1 = Battle(player1, player2)
    battle1.battle_loop()
    display_stats(player1, player2)

    random_story_event(player1)

    # add more battles and story elements here


if __name__ == '__main__':
    main()
