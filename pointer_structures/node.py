# node implementation for DLL
class Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, prev=None, next=None):
        self._element = element
        self._prev = prev
        self._next = next
