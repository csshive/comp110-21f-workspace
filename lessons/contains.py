"""Example of writing a funcation to process a list."""


def main() -> None: 
    """Entrypoint of program. """
    names: list[str] = ["Kris", "Kaki"]
    print(contains('Kevin', names))


def contains(needle: str, haystack: list[str]) -> bool: 
    """Return True iff neddle is found in the haystack. """
    # Move through each item in licst findinig needle
    i: int = 0 
    while i < len(haystack): 
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
    return False


if __name__ == "__main__":
    main()