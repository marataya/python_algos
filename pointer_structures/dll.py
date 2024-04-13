from typing import Optional

from pointer_structures.node import Node


class DoublyLinkedList:
    def __init__(self):
        self.len = 0
        self.head: Node = None
        self.tail: Node = None

    def prepend(self, item):
        node = Node(item, None, None)
        self.len += 1
        if not self.head:
            self.head = self.tail = node
            return

        node._next = self.head
        self.head._prev = node
        self.head = node

    def insertAt(self, item: int, idx: int):
        if idx > self.len:
            raise IndexError('Wrong index')
        if idx == self.len:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return

        self.len += 1
        curr: Node = self.head

        i = 0
        while curr and i < idx:
            curr = curr._next
            i += 1

        node = Node(item)
        node._next = curr
        node._prev = curr._prev
        if curr._prev:
            curr._prev._next = node

        curr._prev = node

    def append(self, item: int):
        self.len += 1
        node = Node(item)

        if not self.tail:
            self.head = self.tail = node
            return

        node._prev = self.tail
        self.tail._next = node
        self.tail = node

    def remove(self, item: int) -> Optional[int]:
        """Removes 1st element whose value is equal to item"""
        if self.len == 0:
            return None

        curr = self.head

        while curr:
            if curr._element == item:
                break
            curr = curr._next

        return self.removeNode(curr)



    def removeAt(self, idx: int) -> Optional[int]:
        node = self.getAt(idx)
        if not node or self.len == 0:
            return None

        curr = self.head

        i = 0
        while curr and i < idx:
            curr = curr._next
            i += 1

        return self.removeNode(curr)


    def removeNode(self, curr: Node) -> Optional[int]:
        if not curr:
            return None

        if curr._prev:
            curr._prev._next = curr._next
        if curr._next:
            curr._next._prev = curr._prev

        if curr == self.head:
            self.head = curr._next
        if curr == self.tail:
            self.tail = curr._prev

        curr._prev = curr._next = None

        self.len -= 1
        if curr:
            return curr._element
        else:
            return None


    def get(self, idx: int) -> int:
        return self.getAt(idx)._element


    def getAt(self, idx: int) -> Optional[Node]:
        curr = self.head
        i = 0
        while curr and i < idx:
            curr = curr._next
            i += 1

        return curr


if __name__ == '__main__':
    list = DoublyLinkedList()
    list.append(5)
    list.append(7)
    list.append(9)

    print(list.get(2))
    print(list.removeAt(1))
    print(list.len)

    list.append(11)
    print(list.removeAt(1))
    print(list.remove(9))
    print(list.removeAt(0))
    print(list.removeAt(0))
    print(list.len)

    print('prepend')
    list.prepend(5)
    list.prepend(7)
    list.prepend(9)


    print(list.get(2))
    print(list.get(0))
    print(list.remove(9))
    print(list.len)
    print(list.get(0))
