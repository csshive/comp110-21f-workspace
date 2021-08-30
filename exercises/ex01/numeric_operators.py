"""Practicing with numeric operators, type conversions, and string concatenation."""
__author__: str = "730330844"

left_side_number: int = int(input("Left-hand side: "))
right_side_number: int = int(input("Right-hand side: "))

exponentiation: int = int(left_side_number) ** int(right_side_number)
division: int = int(left_side_number) / int(right_side_number)
integer_division: int = int(left_side_number) // int(right_side_number)
remainder_modulo: int = int(left_side_number) % int(right_side_number)

print(str(left_side_number) + " ** " + str(right_side_number) + " is " + str(exponentiation))
print(str(left_side_number) + " / " + str(right_side_number) + " is " + str(division))
print(str(left_side_number) + " // " + str(right_side_number) + " is " + str(integer_division))
print(str(left_side_number) + " % " + str(right_side_number) + " is " + str(remainder_modulo))