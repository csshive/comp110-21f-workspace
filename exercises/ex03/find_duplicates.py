"""Finding duplicate letters in a word."""

__author__ = "730330844"

user_word: str = input("Enter a word: ")
dup: bool = False 
i: int = 0
while i < len(user_word):
    char = user_word[0]
    j: int = i + 1 
    while j < len(user_word):
        dup = char == j 
        j += 1
    i += 1

print("Found duplicate: " + str(dup))