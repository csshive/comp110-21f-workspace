"""List utility functions."""

__author__ = "730330844"


def all(indicated_number: int, list_of_ints: list[int]) -> bool: 
    """Returns True iff all numbers match the indicated number, False otherwise or if the list is empty."""
    i: int = 0 
    list_of_ints_str: str = str(list_of_ints)
    if indicated_number == list_of_ints_str[i]:    
        return True
    else:
        return False

# else: list[] or indicated_number =! lists_of_ints