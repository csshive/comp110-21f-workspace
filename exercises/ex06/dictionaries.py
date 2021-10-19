"""Practice with dictionaries."""

__author__ = "730330844"


def invert(list_of_str: dict[str, str]) -> dict[str, str]: 
    """Program to invert a list."""
    reversed_dictionary = {value: key for (key, value) in list_of_str.items()}
    return(reversed_dictionary)


def favorite_color(names_colors: dict[str, str]) -> str:
    """Program to identify the favorite color."""
    track = {}
    for key, value in names_colors.items():
        if value not in track:
            track[value] = 0
    else: 
        for key, value in names_colors.items():
            track[value] += 1
    return(max(track, key=track.get))


def count(string_list: list[str]) -> dict[str, int]:
    """Program to count frequency."""
    freq = {}
    for item in string_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return(freq)
