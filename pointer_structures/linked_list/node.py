# node implementation for DLL
class Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next
