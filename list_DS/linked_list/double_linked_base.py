from node import Node
class _DoublyLinkedBase:
    def __init__(self):
        self._header = Node(None, None, None)
        self._trailer= Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predessor, successor):
        newest = Node(e, predessor, successor)
        predessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predessor = node._prev
        successor = node._next
        predessor._next = successor
        successor._prev = predessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None # deprecate node
        return element

