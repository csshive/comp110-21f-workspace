"""Drawing forests in a loop."""

__author__ = "730330844"

# The string constant for the pine tree emoji

TREE: str = '\U0001F332'

user_depth: int = int(input("Depth: ")) 
i: int = 0 
counter: int = 0 + 1
while counter < int(user_depth + 1):
    print(TREE * counter)
    i = i + 1
    counter = counter + 1 
