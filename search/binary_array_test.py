import random

from search.binary_search import binary_search_v2, binary_array_search

if __name__ == '__main__':
    arr = [random.randint(0, 10) for _ in range(10)]
    print(arr)
    print(binary_array_search(arr, 7))
    print(binary_search_v2(arr, 7))
