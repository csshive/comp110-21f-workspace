"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730330844"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """Testing when function receives a list with no even numbers it returns an empty list."""
    xs: list[int] = ([1, 5, 3])
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None: 
    """When list is empty function returns an empty list."""
    xs: list[int] = ([])
    assert only_evens(xs) == []


def test_only_evens_items() -> None:
    """When function has multiple even items it returns all items.""" 
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_only_evens_items_again() -> None:
    """When one even number is found function returns list with item."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_sub_empty() -> None:
    """When list is empty function returns an empty list."""
    a_list: list[int] = ([])
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == []


def test_sub_items() -> None:
    """If start is greater than the length of the list returns empty list."""
    a_list: list[int] = ([1, 2, 3, 4])
    start_index: int = 5
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == []


def test_sub_again() -> None:
    """When one even number is found function returns list with item."""
    a_list: list[int] = ([10, 20, 30, 40])
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [20, 30]


def test_concat_empty() -> None:
    """When list is empty function returns an empty list."""
    list_one_of_int: list[int] = ([])
    list_two_of_int: list[int] = ([])
    assert concat(list_one_of_int, list_two_of_int) == []


def test_concat_items() -> None:
    """Two list of same integer."""
    list_one_of_int: list[int] = ([2, 2, 2])
    list_two_of_int: list[int] = ([2, 2, 2])
    assert concat(list_one_of_int, list_two_of_int) == [2, 2, 2, 2, 2, 2]


def test_concat_again() -> None:
    """One multiple list one empty list."""
    list_one_of_int: list[int] = ([2, 3, 4, 7])
    list_two_of_int: list[int] = ([])
    assert concat(list_one_of_int, list_two_of_int) == [2, 3, 4, 7]