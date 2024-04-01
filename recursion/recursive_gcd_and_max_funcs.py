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
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


# recursive max function
def max_recursive(A):
    if len(A) == 2:
        return A[0] if A[0] > A[1] else A[1]
    submax = max(A[1:])
    return A[0] if A[0] > submax else submax


if __name__ == '__main__':
    print(gcd_recursive(18, 12))
    print(gcd_iterative(18, 12))
    print(max_recursive([1,5,5,5,1,7,5,7,45,4,21,5,1,20,-4]))
