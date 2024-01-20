import math


def binary_search(A, number) -> bool:
    lo = 0
    hi = len(A)
    while lo < hi:
        m = math.floor(lo + (hi - lo) / 2)
        v = A[m]
        if v == number:
            return True
        elif v > number:
            hi = m
        else:
            lo = m + 1


    return False
