"""List utility functions."""

__author__ = "730330844"


def all(num: int, list_of_ints: list[int]) -> bool: 
    """Return True iff neddle is found in the list of ints. """
    i: int = 0 
    while i < len(list_of_ints): 
        item: int = list_of_ints[i]
        if item == num:
            return True
        i += 1
    return False


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    i: int = 0
    if len(list_one) != len(list_two):
        return False  
    while i < len(list_one):
        item: int = list_one[i]
        item_two: int = list_two[i]
        if item == item_two 
            i += 1 
            
             