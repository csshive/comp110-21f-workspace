"""Practicing the relaional operators individually"""
__author__: str = "730330844"

left_side_number: int = int(input("Left-hand side: "))
right_side_number: int = int(input("Right-hand side: "))

less_than: int = int(left_side_number) < int(right_side_number)
at_least: int = int(left_side_number) >= int(right_side_number)
equal_to: int = int(left_side_number) == int(right_side_number)
not_equal_to: int = int(left_side_number) != int(right_side_number)

print(str(left_side_number) + " < " + str(right_side_number) + " is " + str(less_than))
print(str(left_side_number) + " >= " + str(right_side_number) + " is " + str(at_least))
print(str(left_side_number) + " == " + str(right_side_number) + " is " + str(equal_to))
print(str(left_side_number) + " != " + str(right_side_number) + " is " + str(not_equal_to))
