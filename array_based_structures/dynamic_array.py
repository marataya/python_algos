import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def len(self):
        '''Return number of elements stored in the array.'''
        return self._n

    def __getitem__(self, k):
        '''Return element at index k.'''
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]  # retrieve from array

    def append(self, obj):
        '''Add object to end of the array.'''
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        '''Resize internal array to capacity c.'''
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _make_array(self, c):
        '''Return new array with capacity c.'''
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1


if __name__ == '__main__':
    arr = DynamicArray()
    arr.append(5)
    arr.append(7)
    arr.insert(1, 99)
    for i in arr:
        print(i)
    print('Len:', len(arr))
