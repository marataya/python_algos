from typing import List


def quicksort(arr:List) -> List:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if pivot >= x]
        greater = [x for x in arr[1:] if pivot < x]
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    print(quicksort([10,5,3,2]))
