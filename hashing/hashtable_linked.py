"""
    Hashtable to store (key, value) pairs in a fixed hashtable of linked
    lists, using hash() % N as hash code.  This table can replace values
    associated with a given key.  When two keys attempt to use
    the same location, a linked list is constructed.

    Hashtable will never "run out" of storage, though performance suffers
    as more (key, value) pairs are added.
"""
from hashing.linked_entry import LinkedEntry


class Hashtable:
    """Hashtable using array of M linked lists."""
    def __init__(self, M=10):
        if M < 1:
            raise ValueError("Hashtable storage must be at least 1")
        self.table = [None]*M
        self.M = M
        self.N = 0

    def get(self, k):
        """Retrieve value associated with key, k."""
        hc = hash(k) % self.M       # First place it could be
        entry = self.table[hc]
        while entry:
            if entry.key == k:
                return entry.value
            entry = entry.next
        return None                 # Couldn't find

    def put(self, k, v):
        """Associate value, v, with the key, k."""
        hc = hash(k) % self.M       # First place it could be
        entry = self.table[hc]
        while entry:
            if entry.key == k:      # Overwrite if already here
                entry.value = v
                return
            entry = entry.next

        self.table[hc] = LinkedEntry(k, v, self.table[hc])
        self.N += 1

    def remove(self, k):
        """Remove (k,v) entry associated with k."""
        hc = hash(k) % self.M       # First place it could be
        entry = self.table[hc]
        prev = None
        while entry:
            if entry.key == k:
                if prev:
                    prev.next = entry.next
                else:
                    self.table[hc] = entry.next
                self.N -= 1
                return entry.value

            prev, entry = entry, entry.next

        return None                 # Nothing was removed

    def __iter__(self):
        """Generate all (k, v) tuples for entries in all linked lists table."""
        for entry in self.table:
            while entry:
                yield (entry.key, entry.value)
                entry = entry.next

class DynamicHashtable:
    def __init__(self, M=10):
        if M < 1:
            raise ValueError("Hashtable storage must be at least 1")
        self.table = [None]*M
        self.M = M
        self.N = 0
        self.load_factor = 0.75
        # Ensure for M <= 3 that threshold is no greater than M-1
        self.threshold = min(M * self.load_factor, M-1)

