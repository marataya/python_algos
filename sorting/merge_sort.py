# Recursive divide and conquer algorithm
import random


def merge_sort(A):
    """Recursive O(n logn) sorting algo"""
    aux = [None] * len(A)  # Allocate auxiliary storage equal in size to original array.

    def rsort(lo, hi):
        if hi <= lo: return
        mid = (hi + lo) // 2
        rsort(lo, mid)
        rsort(mid + 1, hi)
        merge(lo, mid, hi)

    def merge(lo, mid, hi):
        aux[lo: hi + 1] = A[lo: hi + 1]  # copy sorted subarray to aux to prepare for merge
        left = lo
        right = mid + 1
        for i in range(lo, hi + 1):
            if left > mid: # when left subarray is exhausted take values from right subarray
                A[i] = aux[right]
                right+=1
            elif right > hi: # when right subarray is exhausted take values from left subarray
                A[i] = aux[left]
                left+=1
            elif aux[left] < aux[right]:
                A[i] = aux[left]
                left += 1
            else:
                A[i] = aux[right]
                right += 1

    rsort(0, len(A)-1)


if __name__ == '__main__':
    A = [random.randint(0,50) for _ in range(100)]
    print(A)
    merge_sort(A)
    print(A)
