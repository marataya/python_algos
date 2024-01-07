# sample algorithm analysis: first 2 funcs has O(n2) complexity and 3rd has O(n)

import time
from random import randint

def prefix_averages1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

def prefix_averages1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

def prefix_averages2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[:j+1]) / (j + 1)
    return A

def prefix_averages2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[:j+1]) / (j + 1)
    return A

def prefix_averages3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A



if __name__ == '__main__':
    S = [randint(0, 100) for i in range(100)]
    begin = time.time()
    result1 = prefix_averages1(S)
    end = time.time()
    print(result1[:10], f'{(end - begin)*100 : 0.10f} ms')

    begin = time.time()
    result2 = prefix_averages2(S)
    end = time.time()
    print(result2[:10], f'{(end - begin)*100 : 0.10f} ms')

    begin = time.time()
    result3 = prefix_averages3(S)
    end = time.time()
    print(result3[:10], f'{(end - begin)*100 : 0.10f} ms')

    # print(prefix_averages2(S))
