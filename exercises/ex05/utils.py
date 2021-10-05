"""List utility functions part 2."""

__author__ = "730330844"


def only_evens(list_of_int: list[int]) -> list[int]: 
    """Return a list containing only the elements of the input list that were even."""
    evens = []
    for number in list_of_int:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a List which is a subset of the given list, between the specified start index and the end index."""
    new_list: list[int] = []
    if len(a_list) == 0:
        return new_list
    if start_index > len(a_list):
        return new_list
    if end_index <= 0: 
        return new_list
    else:
        new_list = a_list[start_index:end_index]
        return new_list


def concat(list_one_of_int: list[int], list_two_of_int: list[int]) -> list[int]:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list.""" 
    for i in list_two_of_int:
        list_one_of_int.append(i)
    return list_one_of_int