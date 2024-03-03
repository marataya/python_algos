"""

"""

def pairs(k, arr):
    set = {x for x in arr}
    result = 0
    for x in arr:
        if x + k in set:
            result += 1
        if x - k in set:
            result += 1

    return result // 2

if __name__ == '__main__':
    # Sample Input
    k = 2
    arr = [1, 5, 3, 4, 2]
    print(pairs(k, arr))  # Output: 3
