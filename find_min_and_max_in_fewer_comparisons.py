'''
Describe an algorithm for finding both the minimum and maximum of n
numbers using fewer than 3n/2 comparisons. (Hint: First, construct a
group of candidate minimums and a group of candidate maximums.)
'''
from random import randint
def find_min_max(S):
    candidate_maxs = []
    candidate_mins = []
    for i in range(1, len(S), 2):
        if S[i-1] < S[i]:
            candidate_maxs.append(S[i])
            candidate_mins.append(S[i-1])
        else:
            candidate_mins.append(S[i-1])
            candidate_maxs.append(S[i])
    if len(S) & 1 == 1:
        if S[i-1] > S[i-2]:
            candidate_maxs.append(S[i])
        else:
            candidate_mins.append(S[i-1])
    print('mins:',candidate_mins)
    print('maxs:',candidate_maxs)
    min = 1000
    max = -1000
    for el in candidate_mins:
        if el < min:
            min = el
    for el in candidate_maxs:
        if el > max:
            max = el
    return min, max

if __name__ == '__main__':
    S = [randint(0, 1000) for i in range(26)]
    print(S)
    print(find_min_max(S))
    print('->', min(S))
    print('->', max(S))
