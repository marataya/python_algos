def bubble_sort(A):
    count = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                tmp = A[j]
                A[j] = A[j+1]
                A[j+1] = tmp
                count += 1
    print(count)


if __name__ == '__main__':
    A= [5, 7, 825, 1, 2, 4, 8, 77, 4, 1, 1, 1, 0]
    bubble_sort(A)
    print(A)
