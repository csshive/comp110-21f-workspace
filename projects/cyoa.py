"""Choose your own adventure game."""

__author__ = "730330844"

from random import randint

player: str = str(" ")
pet_name: str = str(" ")
points: int = 0 
final_point = 0
CAT_EMOJI: str = U"\U0001F408"	


def main() -> None: 
    """The program's entrypoint."""
    greet()
    game_start = "yes"
    while game_start == "yes":
        choice: str = input(f'Would you like to a) feed and bathe {pet_name}, b) play and dress up {pet_name}, or c) end the experience? Please type the lowercase letter of your choice. ')
        if choice == "a":
            feed_bathe()
        if choice == "b":
            play_points = play(3, 7)
            print(play_points)
        if choice == "c":
            print(f'Goodbye! {pet_name} and I will miss you. You have accumulated {final_point} adventure points in the experience. Play again soon!')
        game_start = input(f"So far, you have accumulated adventure {final_point} points. Do you want to continue the game? Please enter yes or no. ")


def greet() -> None: 
    """Welcoming player."""
    global player
    player = input("What is your name? ") 
    global pet_name
    pet_name = input("What would you like to name your Webkinz? ")
    print(f'Welcome, {player}. Today, you will be taking care of {pet_name}!')
    print(CAT_EMOJI)


def feed_bathe() -> None: 
    """Feed and bathe if-then."""
    print(f'Thanks for choosing to feed and bathe {pet_name}')
    points: int = 0 + 10
    print("You have received 10 points") 
    happiness: str = input(f"Would you like to check {pet_name}'s level of happiness? Type yes or no. ")
    happiness_level = randint(1, 4)
    if happiness == "yes":
        if happiness_level <= 2: 
            if happiness_level < 2:
                print(f"{pet_name} is happy to be be your pet!") 
                points = points + 10
                print(f'You are awarded 10 points for checking on, {pet_name}! ')
            else:
                print(f"{pet_name} feels dirty and wants to take a bath! ") 
                points = points + 10
                print(f'You are awarded 10 points for checking on, {pet_name}! ')
        else: 
            if happiness_level == 3: 
                print(f"{pet_name} is feeling extra playful!") 
                points = points + 10
                print(f'You are awarded 10 points for checking on, {pet_name}! ')
            else:
                print(f"{pet_name} is sad. Maybe dressing {pet_name} up will make {pet_name} feel better.") 
                points = points + 10
                print(f'You are awarded 10 points for checking on, {pet_name}! So far, you have {points} points!')
    global final_point
    final_point = (final_point + points)


def play(a: int, b: int) -> int: 
    """Returns 10 points for play."""
    print(f"Thanks for playing with {pet_name}! You got 7 additional points")
    global final_point
    final_point = (final_point + points + b)
    if a >= b:
        return 0
    else: 
        return final_point
    

if __name__ == "__main__":
    main()