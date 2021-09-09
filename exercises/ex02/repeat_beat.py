"""Repeating a beat in a loop."""

__author__ = "730330844"

counter: int = 0
user_string_beat: str = input("What beat do you want to repeat? ")
user_string_number: str = int(input("How many times do you want to repeat it? "))

while counter < user_string_number:
   print(user_string_beat + "" * user_string_number)
   counter = counter + 1

if user_string_number <= 0: 
    print("No beat...") 