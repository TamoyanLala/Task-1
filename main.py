import random

def roll_dice():
    """Roll two dice and return their sum."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def play_game():
    """Play a single game of craps."""
    
    first_roll = roll_dice()
    print(f"You rolled {first_roll}")
    if first_roll in (7, 11):
        print("You win!")
    elif first_roll in (2, 3, 12):
        print("Craps! You lose.")
    else:
        print(f"Your goal is {first_roll}")
        
        while True:
            roll = roll_dice()
            print(f"You rolled {roll}")
            if roll == first_roll:
                print("You win!")
                break
            elif roll == 7:
                print("You lose.")
                break
play_game()
