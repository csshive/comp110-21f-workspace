"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730330844"


"""Test for the sum function."""


def test_invert_first() -> None: 
    """Testing when basic function with multiple variables."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_two() -> None:
    """Testing when function has only one dict.""" 
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def test_invert_three() -> None: 
    """Testing when function has two dicts."""
    xs: dict[str, str] = {'kris': 'jordan', 'michael': 'bill'}
    assert invert(xs) == {'jordan': 'kris', 'bill': 'michael'}


def test_favorite_color_first() -> None: 
    """Testing when function has two same color."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "NCSU": "blue"}
    assert favorite_color(xs) == str("blue")


def test_favorite_color_two() -> None: 
    """Testing when function has all same color."""
    xs: dict[str, str] = {"Marc": "green", "Ezri": "green", "NCSU": "green"}
    assert favorite_color(xs) == str("green")


def test_favorite_color_three() -> None: 
    """Testing when function has one color."""
    xs: dict[str, str] = {'Mat': 'yellow'}
    assert favorite_color(xs) == str("yellow")


def test_count_first() -> None:
    """Testing large str.""" 
    xs: list[str] = ["a", "a", "a", "b", "b", "b", "c", "c", "c"]
    assert count(xs) == {"a": 3, "b": 3, "c": 3}


def test_count_two() -> None: 
    """Testing when function has diff amounts of str."""
    xs: list[str] = ["a", "a", "b", "b", "b", "c"]
    assert count(xs) == {"a": 2, "b": 3, "c": 1}


def test_count_three() -> None: 
    """Testing when function has varying amounts of str."""
    xs: list[str] = ["a", "a", "a", "b", "c", "c", "c"]
    assert count(xs) == {"a": 3, "b": 1, "c": 3}
