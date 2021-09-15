"""Repeating a beat in a loop."""

"""Repeating a beat in a loop."""

__author__ = "730330844"


counter: int = 0
i: str = ""
user_string_beat: str = input("What beat do you want to repeat? ")
user_string_number: str = input("How many times do you want to repeat it? ")

while counter < int(user_string_number):
    i = str = (user_string_beat)
    print((i), end = " ")
    counter = counter + 1
if int(user_string_number) <= 0: 
    print("No beat...") 
