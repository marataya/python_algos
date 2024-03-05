import random
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

if __name__ == '__main__':
    A = [random.randint(0,10) for _ in range(10)]
    print(A)
    print(binary_array_search(A, 7))
