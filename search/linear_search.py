def linear_search(haystack:list, needle:int) -> bool:
    for el in haystack:
        if needle == el:
            return True
    return False
