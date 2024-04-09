from time import time
"""inserting 1st element and appending with reversing time """
if __name__ == '__main__':
    count = 10 ** 5
    nums = []
    # Linear time algo
    begin = time()
    for i in range(count):
        nums.append(i)
    nums.reverse()
    end = time()
    diff1 = end-begin
    print(f'{diff1} sec')
    nums = []
    # Quadratic time algo
    begin = time()
    for i in range(count):
        nums.insert(0, i)
    nums.reverse()
    end = time()
    diff2 = end-begin
    print(f'{diff2} sec')
    print(f'2nd algo is {diff2/diff1:0.2f} times slower')

