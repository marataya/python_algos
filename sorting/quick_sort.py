import time
from typing import List
import random


def quick_sort_v1(arr: List) -> List:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if pivot >= x]
        greater = [x for x in arr[1:] if pivot < x]
        return quick_sort_v1(less) + [pivot] + quick_sort_v1(greater)


def partition(A, lo, hi, idx):
    """
    Partition using A[idx] as value. Note lo and hi are INCLUSIVE on both
    ends and idx must be valid index. Count the number of comparisons
    by populating A with RecordedItem instances.
    """
    if lo == hi:
        return lo

    A[idx], A[lo] = A[lo], A[idx]  # swap into position
    i = lo
    j = hi + 1
    while True:
        while True:
            i += 1
            if i == hi: break
            if A[lo] < A[i]: break

        while True:
            j -= 1
            if j == lo: break
            if A[j] < A[lo]: break

        # doesn't count as comparing two values
        if i >= j: break

        A[i], A[j] = A[j], A[i]

    A[lo], A[j] = A[j], A[lo]
    return j


def quick_sort_v2(A):
    """Quicksort using a random pivot select."""

    def qsort(lo, hi):
        if hi <= lo:
            return

        pivot_idx = random.randint(lo, hi)
        location = partition(A, lo, hi, pivot_idx)

        qsort(lo, location - 1)
        qsort(location + 1, hi)

    qsort(0, len(A) - 1)


def quick_sort_v3(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_v3(left) + middle + quick_sort_v3(right)


def quick_sort_v4(A):
    def partition(A, lo, hi):
        pivot = A[hi]
        idx = lo - 1
        for i in range(lo, hi):
            if A[i] <= pivot:
                idx += 1
                A[i], A[idx] = A[idx], A[i]
        idx += 1
        A[hi], A[idx] = A[idx], A[hi]
        return idx

    def qsort(A, lo, hi):
        if lo >= hi: return
        pivotIdx = partition(A, lo, hi)
        qsort(A, lo, pivotIdx - 1)
        qsort(A, pivotIdx + 1, hi)

    qsort(A, 0, len(A) - 1)


if __name__ == '__main__':
    begin = time.time()
    n = 10000
    random_array = [random.randint(1, 100) for _ in range(n)]
    # end = time.time()
    # print(f'{end - begin} sec elapsed generating {n} random numbers')
    # print(random_array)
    # begin = time.time()
    # print(quick_sort_v1(random_array))
    # end = time.time()
    # print(f'{end - begin} sec quicksort took to sort it')
    A = list(random_array)
    quick_sort_v4(A)
    print(A)

    # print(quick_sort_v3(A))
