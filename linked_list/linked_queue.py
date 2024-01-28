import sys
from exceptions import Empty
class LinkedQueue:
    class Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head  = None
        self._tail  = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self.Node(e, self._head) # create and link a new node
        self._size += 1

    def first(self):
        '''return but not remove the element at the top of the stack'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        # if remove node was single then it was the tail and tail should be set None
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


if __name__ == '__main__':
    queue = LinkedQueue()
    print(queue._head, queue._tail)
    queue.enqueue(5)
    print(queue._head._element, queue._tail._element)
    queue.enqueue(7)
    print(queue._head._element, queue._tail._element)
