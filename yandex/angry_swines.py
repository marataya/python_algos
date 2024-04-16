if __name__ == '__main__':
    a = list(map(int, input().split()))
    a.sort()
    print(a[-3], a[-2], a[-1])
