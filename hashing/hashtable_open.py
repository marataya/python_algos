"""
    Hashtable to store (key, value) pairs in a fixed hashtable using hash() % N as hash code.
    This table can replace values associated with a given key.  When two keys attempt to use
    the same location, OPEN ADDRESSING resolves the conflict.

    Always leaves at least ONE empty spot so code is simpler, which means that an
    open addressing hashtable must have M >= 2.
"""
from hashing.entry import Entry


class Hashtable:
    """Open Addressing Hashtable."""
    def __init__(self, M=10):
        if M < 2:
            raise ValueError('Hashtable must contain space for at least two (key, value) pairs.')

        self.table = [None] * M
        self.M = M
        self.N = 0

    def get(self, k):
        """Retrieve value associated with key, k."""
        hc = hash(k) % self.M       # First place it could be
        while self.table[hc]:
            if self.table[hc].key == k:
                return self.table[hc].value
            hc = (hc + 1) % self.M
        return None                 # Couldn't find

    def is_full(self):
        """Determine if Hashtable is full."""
        return self.N >= self.M - 1

    def put(self, k, v):
        """Associate value, v, with the key, k."""
        hc = hash(k) % self.M       # First place it could be
        while self.table[hc]:
            if self.table[hc].key == k:     # Overwrite if already here
                self.table[hc].value = v
                return
            hc = (hc + 1) % self.M

        if self.N >= self.M - 1:
            raise RuntimeError('Table is Full: cannot store {} -> {}'.format(k, v))

        self.table[hc] = Entry(k, v)
        self.N += 1

    def __iter__(self):
        """Generate all (k, v) tuples for actual (i.e., non-deleted) entries."""
        for entry in self.table:
            if entry:
                yield (entry.key, entry.value)

if __name__ == '__main__':
    ht = Hashtable(5)
    ht.put(1,1)
    ht.put(2,2)
    ht.put(3,3)
    ht.put(4,4)
    # ht.put(5,5) causes runtime error
    print(ht.get(1))
    print(ht.get(4))
