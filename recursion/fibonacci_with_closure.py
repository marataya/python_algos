def fibo():
    a, b = 0, 1

    def f():
        nonlocal a, b
        a = b
        b = a + b
        return b

    return f


if __name__ == '__main__':
    f = fibo()
    while (x := f()) < 100:
        print(x)
