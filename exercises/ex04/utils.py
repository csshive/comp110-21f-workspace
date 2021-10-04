"""List utility functions."""

__author__ = "730330844"


def all(list_of_int: list[int], num: int) -> bool: 
    """Function to indicate whether or not a ll the ints in the list are the same as the given int."""
    if len(list_of_int) == 0: 
        return False
    i: int = 0
    while i < len(list_of_int):
        if list_of_int[i] == num: 
            return True
        else:
            return False 
    

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Function that when given two lists of int values, return True if every element at every index is equal in both lists."""
    if len(list_one) != len(list_two):
        return False
    if len(list_one) == 0:
        return True
    for x in list_one:
        for y in list_two:
            if x == y:
                return True
    else: 
        return False


def max(input: list[int]) -> int:
    """Function that given a list of ints, max should return the largest in the List."""    
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else: 
        my_max = input[0]
        for x in input:
            if x > my_max:
                my_max = x
        return my_max
