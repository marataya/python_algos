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
def selection_sort(arr: List):
    new_arr = []
    for i in range(len(arr)):
        smallest = min_idx(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

if __name__ == '__main__':
    print(selection_sort([5,3,6,2,10]))



