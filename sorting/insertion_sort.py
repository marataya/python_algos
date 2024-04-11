'''
Algorithm InsertionSort(A):
Input: An array A of n comparable elements
Output: The array A with elements rearranged in nondecreasing order
for k from 1 to n − 1 do
    Insert A[k] at its proper location within A[0], A[1], ..., A[k].
Complexity: O(n^2)
Code Fragment 5.9: High-level description of the insertion-sort algorithm.
'''


def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur

def insertion_sort_v2(A):
    "Insertion sort v2"
    N = len(A)
    for i in range(1,N):
        for j in range(i,0,-1):
            if A[j-1] <= A[j]:
                break
            A[j],A[j-1] = A[j-1],A[j]

if __name__ == '__main__':
    A= [5, 7, 825, 1, 2, 4, 8, 77, 4, 1, 1, 1, 0]
    insertion_sort(A)
    print(A)
    A= [5, 7, 825, 1, 2, 4, 8, 77, 4, 1, 1, 1, 0]
    insertion_sort_v2(A)
    print(A)
