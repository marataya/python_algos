import random
import time

def flawed(A):
    my_max = 0
    for v in A:
        if my_max < v:
            my_max = v
    return my_max


def largest(A):
    my_max = A[0]
    for idx in range(1, len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
    return my_max


def alternate(A):
    for v in A:
        v_is_largest = True
        for x in A:
            if v < x:
                v_is_largest = False
                break
        if v_is_largest:
            return v
    return None


def largest_two(A):
    my_max, second = A[:2]
    if my_max < second:
        my_max, second = second, my_max
    for idx in range(2, len(A)):
        if my_max < A[idx]:
            my_max, second = A[idx], my_max
        elif second < A[idx]:
            second = A[idx]
    return (my_max, second)


def sorting_two(A):
    return tuple(sorted(A, reverse=True)[:2])


def double_two(A):
    my_max = max(A)
    copy = list(A)
    copy.remove(my_max)
    return (my_max, max(copy))


def mutable_two(A: list):
    idx = max(range(len(A)), key=A.__getitem__)
    my_max = A[idx]
    del A[idx]
    second = max(A)
    A.insert(idx, my_max)
    return (my_max, second)


def tournament_two(A):
    N = len(A)
    winner = [None] * (N - 1)
    loser = [None] * (N - 1)
    prior = [-1] * (N - 1)

    idx = 0
    for i in range(0, N, 2):
        if A[i] < A[i + 1]:
            winner[idx] = A[i + 1]
            loser[idx] = A[i]
        else:
            winner[idx] = A[i]
            loser[idx] = A[i + 1]
        idx += 1

    m = 0
    while idx < N - 1:
        if winner[m] < winner[m + 1]:
            winner[idx] = winner[m + 1]
            loser[idx] = winner[m]
            prior[idx] = m + 1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m+1]
            prior[idx] = m
        m += 2
        idx += 1

    largest = winner[m]
    second = loser[m]
    m = prior[m]
    while m >= 0:
        if second < loser[m]:
            second = loser[m]
        m = prior[m]

    return (largest, second)

if __name__ == '__main__':
    """Both algorithms need non-empty list because of Index out of bounds exception"""
    print(flawed([-5, -3, -11]))  # definitely flawed
    print(largest([-5, -3, -11]))  # working as it should
    print(alternate([-5, -3, -11]))  # shitty performance

    # p = [3, 1, 4, 1, 5, 9, 2, 6]
    begin = time.perf_counter()
    for _ in range(100000):
        l = [random.randint(0, 10) for _ in range(10)]
        tournament_two(l)
    end = time.perf_counter()
    print(f"Execution time: {(end - begin):.4f} seconds")

    begin = time.perf_counter()
    for _ in range(100000):
        l = [random.randint(0, 10) for _ in range(10)]
        mutable_two(l)
    end = time.perf_counter()
    print(f"Execution time: {(end - begin):.4f} seconds")

