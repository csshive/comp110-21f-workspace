"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730330844"


from random import randint


fortune_choice = randint(1, 4)

if fortune_choice <= 2: 
    if fortune_choice < 2:
        print("Your fortune cookie says...")
        print("You have a secret admirer.") 
    else:
        print("Your fortune cookie says...")
        print("A faithful friend is a strong defense.") 
else: 
    if fortune_choice == 3: 
        print("Your fortune cookie says...")
        print("A dubious friend may be an enemy in camouflage.") 
    else:
        print("Your fortune cookie says...")
        print("All your hard work will soon pay off.") 

print("Now, go spread positive vibes!")
