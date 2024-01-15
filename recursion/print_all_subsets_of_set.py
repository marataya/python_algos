def subsets(arr, n):
    if n == 0:
        return [[]]
    else:
        return subsets(arr, n - 1) + [[arr[n - 1]] + subset for subset in subsets(arr, n - 1)]



if __name__ == '__main__':
    print(subsets([1, 2, 3, 77], 4))
