import random
import time
import timeit

print("N\tSum Time")
for trial in [2**_ for _ in range(1,9)]:
    numbers = [random.randint(1,9) for _ in range(trial)]
    m = timeit.timeit(stmt='sum = 0\nfor d in numbers:\n\tsum = sum + d',
                      setup='import random\nnumbers = '+ str(numbers))
    print(f'{trial:d}\t{m:f}')
