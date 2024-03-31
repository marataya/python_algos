from typing import List

from hashing.entry import Entry


class Hashtable:
    """Weak Hashtable implementation with no collision strategy."""
    def __init__(self, M=10):
        self.table: List[Entry] = [None] * M
        self.M = M

    def get(self, k):
        hc = hash(k) % self.M
        return self.table[hc].value if self.table[hc] else None

    def put(self, k, v):
        hc = hash(k) % self.M
        entry = self.table[hc]
        if entry:
            if entry.key == k:
                entry.value = v
            # A collision occurs when two different keys map to the same bucket identified by its hash code value.
            else:
                raise RuntimeError(f'Key Collision: {k} and {entry.key}')
        else:
            self.table[hc] = Entry(k, v)

if __name__ == '__main__':
    table = Hashtable(1000)
    table.put('April', 30)
    table.put('May', 31)
    table.put('September', 30)

    print(table.get('August'))     # Miss: should print None since not present
    print(table.get('September'))  # Hit: should print 30
    print(table.get('May'))
