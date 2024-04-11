# return idx of the smallest element in array
from typing import List


def min_idx(arr) -> int:
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx


# now
def selection_sort(arr: List) -> List:
    """Forms new array from original sorted with SelectionSort"""
    new_arr = []
    for i in range(len(arr)):
        smallest = min_idx(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


# in place selection sort
def selection_sort_v2(A) -> None:
    n = len(A)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


if __name__ == '__main__':
    print(selection_sort([5, 3, 6, 2, 10]))
    arr = [5, 3, 6, 2, 10]
    selection_sort_v2(arr)
    print('Selection Sort Version 2:', arr)
