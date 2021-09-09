"""Counting letters in a string."""

__author__ = "730330844"

user_letter: str = input("What letter do you want to seach for?: ")
user_word: str = input("Enter a word: ")
count: int = 0
i: int = 0  
while i < len(user_word):
    if(user_word[i] == user_letter):
        count: int = count + 1
    i = i + 1
print("Count: " + str(count))
