def binary_search(data, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = 0
    if low > high:
        return False
    else:
        mid: int = (high + low) // 2
        if target == data[mid]:
            return True
        elif target < mid:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    a = [1, 2, 5, 7, 55]
    print(binary_search(a, 7))
