from queue import ArrayQueue
from random import randint

from exceptions import Empty


class ArrayDequeue(ArrayQueue):
    def __init__(self):
        super().__init__()
        self._back = 0

    def _resize(self, cap):
        super()._resize(cap)
        self._back = self._size-1

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
        self._size += 1
        self._back = (self._front + self._size-1) % len(self._data)
        self._data[self._back] = e

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._size += 1
        self._front = len(self._data) - 1 if self._front == 0 else self._front - 1
        self._data[self._front] = e

    def delete_first(self):
        if self.is_empty():
            raise Empty('Dequeue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty('Dequeue is empty')
        answer = self._data[self._back]
        self._data[self._back] = None
        self._back = len(self._data) - 1 if self._front == 0 else self._back - 1
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer


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
    print(DQ.first())
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    DQ.delete_first()
    print(DQ._data)
    print(DQ.first())
    print(DQ.last())
    DQ.delete_last()
    DQ.delete_last()
    print(DQ._data)
    print(DQ.first())
    print(DQ.last())


