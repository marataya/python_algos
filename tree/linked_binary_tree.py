from binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:  # Lighweight, nonpublic class for storing a node
        __slot__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """Constructor should not be invoked by user."""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at the Position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associate node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to the container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for a given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    # binary tree constructor
    def __init__(self):
        self._root = None
        self._size = 0

    #     public accessors
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty
        """
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e and return the old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size += 1
        node._parent = node
        return node._element

    def _attach(self, p, t1: BinaryTree, t2: BinaryTree):
        """Attach trees t1 and t2 as left and right subtrees of external p.
        """
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        print(type(self))
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
            raise TypeError('Tree types must be the same')
        self.size += len(t1) + len(t2)
        if not t1.is_empty():  # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set instance to empty
            t1._size = 0
        if not t2.is_empty():  # attach t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


if __name__ == '__main__':
    tree = LinkedBinaryTree()
    tree._add_root(7)
    tree._add_right(tree.root(), 5)
    tree._add_left(tree.root(), 3)
    tree._add_left(tree.left(tree.root()), 1)
    print(tree.num_children(tree.root()))
    print(tree.depth(tree.Position(tree, tree._validate(tree.root()))))
    t1 = LinkedBinaryTree()
    print(type(tree))
    print(type(t1))
    t1._add_root(99)
    t1._add_right(t1.root(), 87)
    t1._add_left(t1.root(), 73)
    tree._attach(tree.left(tree.left(tree.root())),t1, None)
