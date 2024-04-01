'''
Find Greatest common divisor using recursion
Eucledean algorithm
Comparing two implementations: recursive and iterative
'''


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd_iterative(a, b):
    while b!= 0:
        remainder = a % b
        a = b
        b = remainder
    return a

if __name__ == '__main__':
    print(gcd_recursive(18, 12))
    print(gcd_iterative(18, 12))
