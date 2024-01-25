from queue import ArrayQueue
from random import randint

from exceptions import Empty


class ArrayDequeue(ArrayQueue):
    def __init__(self):
        super().__init__()
        self._back = 0

    def dequeu(self):
        raise NotImplementedError('Not implemented in the child class')

    def enqueu(self, e):
        raise NotImplementedError('Not implemented in the child class')

    def last(self):
        '''Return but do not remove the first element at the front of the queue'''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._back]

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._back = (self._front + self._size) % len(self._data)
        self._data[self._back] = e
        self._size += 1

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._size += 1
        self._front = len(self._data) - 1 if self._front == 0 else self._front - 1
        self._data[self._front] = e


if __name__ == '__main__':
    DQ = ArrayDequeue()
    print(len(DQ))
    print(len(DQ._data))
    for k in range(15):
        DQ.add_last(k + 1)
    print(DQ._data)
    for k in range(5):
        DQ.add_first(99+k)
    print(DQ._data)
    print(DQ.first())
    print(DQ.last())
    DQ.add_first(77)
    print(DQ._data)
