import time
from typing import List
import random

def quicksort(arr:List) -> List:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if pivot >= x]
        greater = [x for x in arr[1:] if pivot < x]
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    begin = time.time()
    n = 10000
    random_array = [random.randint(1,100) for _ in range(n)]
    end = time.time()
    print(f'{end - begin} sec elapsed generating {n} random numbers')
    print(random_array)
    begin = time.time()
    print(quicksort(random_array))
    end = time.time()
    print(f'{end - begin} sec quicksort took to sort it')
