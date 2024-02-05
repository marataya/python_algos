from positional_list import PositionalList


class FavouritesList:

    # ----------------------- nested Item class ---------------------
    class _Item:
        __slots__ = '_value','_count'
        def __init__(self, e):
            self._value = e
            self._count = 0 # access count

    # --------------------- nonpublic utilites -----------------------------------
    def _find_position(self, e) -> PositionalList.Position:
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element() != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p: PositionalList.Position):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))   # delete/reinsert
    # ----------------------- end of nonpublic utilities -------------------------
    def __init__(self, pl: PositionalList):
        self._data = pl

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e) # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e)) # if new, place at end
            p.element()._count += 1 # always increment count
            self._move_up(p) # consider moving forward

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e) # try to locate existing element
        if p is not None:
            self._data.delete(p) # delete, if found

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for _ in range(k):
            item = walk.element() # element of list is Item
            yield item # report user’s element
            walk = self._data.after(walk)


if __name__ == '__main__':
    pl = PositionalList()
    pl.add_last(5)
    pl.add_last(7)
    pl.add_last(9)
    fl = FavouritesList(pl)
    for e in fl.top(3):
        print(e)
