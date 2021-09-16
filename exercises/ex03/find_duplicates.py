"""Finding duplicate letters in a word."""

__author__ = "730330844"

user_word: str = input("Enter a word: ")
dup: bool = False 
i: int = 0
while i < len(user_word):
    char: str = str(user_word[i])
    j: int = i + 1 
    while j < len(user_word):
        dup = str(char) == str(user_word[j]) 
        j += 1
        if dup is True: 
            print("Found duplicate: " + str(dup))
    i += 1