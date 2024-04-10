class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail
    def check_infinite(self):
        """check for infinite loop via next"""
        p1 = p2 = self
        while p1 is not None and p2 is not None:
            if p2.next == None: return False

            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2: return True
        return False

class LinkedList:
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        """Add value to front of the list. O(1)"""
        self.head = LinkedNode(value, self.head)

    def remove(self, value):
        """Remove value from the list"""
        n = self.head
        prev = None

        while n is not None:
            if n.value == value:
                if prev is None:
                    self.head = self.head.next
                else:
                    prev.next = n.next
                return True
            prev = n
            n = n.next
        return False

    def pop(self):
        """Remove first value from list"""
        if self.head is None:
            raise Exception('Empty list')
        value = self.head.value
        self.head = self.head.next
        return value

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

    def __repr__(self):
        """String representation of linked list"""
        if self.head is None:
            return 'linked-list: []'
        return f'linked-list: [{",".join(map(str, self))}]'

    def __len__(self):
        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.next
        return count

if __name__ == '__main__':
    a = LinkedList()
    a.prepend(1)
    a.prepend(2)
    a.prepend(3)
    print(a)
    print(a.pop())
    print(a)
    a.remove(1)
    print(a)
    a.remove(2)
    print(a)
