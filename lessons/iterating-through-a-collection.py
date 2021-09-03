"""Example of looping through all charracters in a string."""

user_string: str = input("Give me a string! ")

# The varibale i is a common countrer variable name in progrmaing.
# i is short for integration. 
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done!")