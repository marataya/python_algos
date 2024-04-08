import random
import timeit
from typing import List


def uniqueCheckFast(aList: List) -> bool:
    s = set()
    for x in aList:
        if x in s:
            return True
        s.add(x)
    return False
def uniqueCheckSlow(aList: List) -> bool:
    for i in range(len(aList)-1):
        for j in range(i+1, len(aList)):
            if aList[i] == aList[j]:
                return True
    return False


print ('N\tSlow     \tFast')
for trial in [2**_ for _ in range(1,13)]:
    numbers = [random.random() for _ in range(trial)]
    mSlow = timeit.timeit(stmt='uniqueCheckSlow(numbers)', setup='import random\nfrom __main__ import uniqueCheckSlow\nnumbers = ' + str(numbers), number=1000)
    mFast = timeit.timeit(stmt='uniqueCheckFast(numbers)', setup='import random\nfrom __main__ import uniqueCheckFast\nnumbers = ' + str(numbers), number=1000)
    print(f'{trial:d}\t{mSlow:f}\t{mFast:f}')
