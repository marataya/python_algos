from double_linked_base import _DoublyLinkedBase
from exceptions import Empty


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._header._next._element
    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)
    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)
    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)


if __name__ == '__main__':
    deque = LinkedDeque()
    deque.insert_first(5)
    deque.insert_first(7)
    print(deque.first())
    print(deque.last())

