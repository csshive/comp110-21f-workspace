
# def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    i: int = 0
    if len(list_one) != len(list_two):
        return False  
    while i < len(list_one):
        item: int = list_one[i]
        item_two: int = list_two[i]
        if item == item_two:
            i += 