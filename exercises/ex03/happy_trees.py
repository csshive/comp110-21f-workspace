"""Drawing forests in a loop."""

__author__ = "730330844"

# The string constant for the pine tree emoji

TREE: str = '\U0001F332'

user_depth: int = int(input("Depth: ")) 
counter: int = 0
i: str = ""
while counter < int(user_depth):
    i = str = (TREE * user_depth)
    print(i)
    counter = counter + 1
