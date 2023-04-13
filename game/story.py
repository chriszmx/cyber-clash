import random


def story_intro(player_name):
    print(f"Welcome, {player_name}! You have just entered the mysterious world of PyBattle.")
    print("In this world, you will face challenging battles against powerful opponents.")
    print("The choices you make will determine your fate.")
    print("Good luck, and may the Python gods be with you!")


def event_1(player):
    print("\nAfter your battle, you come across a fork in the road.")
    choice = int(input("Do you want to go left (1) or right (2)?\n"))

    if choice == 1:
        print("You decided to go left.")
        player.hp += 10
        print("You found a small health potion and gained 10 HP.")
    elif choice == 2:
        print("You decided to go right.")
        player.energy += 10
        print("You found a small energy potion and gained 10 energy.")
    else:
        print("You hesitated and didn't make a choice. The path behind you is now blocked.")


def event_2(player):
    print("\nYou encounter a mysterious merchant who offers you a trade.")
    choice = int(input("Do you want to trade 10 HP for 10 energy (1) or keep your current stats (2)?\n"))

    if choice == 1:
        print("You decided to make the trade.")
        player.hp -= 10
        player.energy += 10
        print("You lost 10 HP and gained 10 energy.")
    else:
        print("You decided to keep your current stats.")

# Add more events as functions here


story_events = [event_1, event_2]  # Add new events to this list


def random_story_event(player):
    random_event = random.choice(story_events)
    random_event(player)
