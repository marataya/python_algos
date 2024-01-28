import sys
from exceptions import Empty
class LinkedStack:
    # ---------------------------Nested Node class---------------------
    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

#      ----------------------Stack methods----------------------------

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

    def top(self):
        '''return but not remove the element at the top of the stack'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ == '__main__':
    stack = LinkedStack()
    stack.push(5)
    stack.push(7)
    stack.push(9)
    print(stack.top())
    print(len(stack))

