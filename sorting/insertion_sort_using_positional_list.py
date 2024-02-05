import sys
sys.path.append('../linked_list')
from linked_list.positional_list import PositionalList

'''
Algorithm InsertionSort(A):
Input: An array A of n comparable elements
Output: The array A with elements rearranged in nondecreasing order
for k from 1 to n − 1 do
    Insert A[k] at its proper location within A[0], A[1], ..., A[k].
Code Fragment 5.9: High-level description of the insertion-sort algorithm.
'''
# from linked_list.positional_list1 import PositionalList
#
def insertion_sort_1(L:PositionalList) -> None:
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


if __name__ == '__main__':
    A = PositionalList()
    A.add_last(5)
    A.add_last(7)
    A.add_last(825)
    A.add_last(1)
    A.add_last(2)
    insertion_sort_1(A)
    for x in A:
        print(x)


