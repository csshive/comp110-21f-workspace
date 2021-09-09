"""Counting letters in a string."""

__author__ = "730330844"

user_letter: str = input("What letter do you want to seach for?: ")
user_word: str = input("Enter a word: ")

i: int = 0  
while i < len(user_word):
    print(user_word[i])  
    i = i + 1
