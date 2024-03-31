import math

# Returns If item exists in array
def binary_array_search(A, target):
    lo = 0
    hi = len(A) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < A[mid]:
            hi = mid-1
        elif target > A[mid]:
            lo = mid + 1
        else:
            return True
    return False


# Return pos
def binary_search_v2(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
