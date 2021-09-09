"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730330844"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint

# Begin your solution here...

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
