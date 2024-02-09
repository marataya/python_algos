class Tree:
    """Abstract base class representing a tree structure"""
    class Position:
        """An abstraction representing position of an element"""
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not self == other

    # ----------------------- abstract methods concrete classes should support

    def root(self):
        """Return position representing the tree's root or None if empty"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return position representing p's root or None if empty"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of element in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    # ------------- concrete method implemented in this class --------------------
    def is_root(self, p):
        """Return True if p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p doenst have any child"""
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of the tree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(p) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p
        If p is None return the height of the entire tree."""
        if p == None:
            p = self.root()
        return self._height2(p)


