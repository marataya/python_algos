'''
Suppose we are given three sequences of numbers, A, B, and C. We will assume
that no individual sequence contains duplicate values, but that there may be some
numbers that are in two or three of the sequences. The THREE-WAY SET DISJOINTNESS
problem is to determine if the intersection of the three sequences is empty, namely,
that there is no element x such that x ∈ A, x ∈ B, and x ∈ C.
'''

from random import randint

def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    print('Common element: ', a)
                    return False
    return True
'''
We can improve upon the asymptotic performance with a simple observation.
Once inside the body of the loop over B, if selected elements a and b do not match
each other, it is a waste of time to iterate through all values of C looking for a
matching triple
'''
def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


if __name__ == '__main__':
    A = [randint(0, 37) for i in range(10)]
    B = [randint(0, 37) for i in range(10)]
    C = [randint(0, 37) for i in range(10)]
    print(A, B, C)
    print(disjoint1(A, B, C))

