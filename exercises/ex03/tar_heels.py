"""An exercise in remainders and boolean logic."""

__author__ = "730330844"


user_integer: int = int(input("Enter an int: ")) 

if (user_integer % 2 == 0):
    if (user_integer % 7 == 0):
        print("TAR HEELS")
    else: 
        print("TAR")
else: 
    if (user_integer % 7 == 0):
        print("HEELS") 
    else: 
        print("CAROLINA")
