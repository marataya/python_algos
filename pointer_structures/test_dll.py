import unittest

from dll import DoublyLinkedList

class TestDLL(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def tearDown(self):
        self.list = None

    def test_basic(self):
        self.list.append(5)
        self.list.append(7)
        self.list.append(9)

        self.assertEqual(self.list.get(2), 9)
        self.assertEqual(self.list.removeAt(1), 7)
        self.assertEqual(self.list.len, 2)

        self.list.append(11)
        self.assertEqual(self.list.removeAt(1), 9)
        self.assertEqual(self.list.remove(9), None)
        self.assertEqual(self.list.removeAt(0), 5)
        self.assertEqual(self.list.removeAt(0), 11)
        self.assertEqual(self.list.len, 0)
    def test_prepend(self):
        print('prepend')

        self.list.prepend(5)
        self.list.prepend(7)
        self.list.prepend(9)


        self.assertEqual(self.list.get(2), 5)
        self.assertEqual(self.list.get(0), 9)
        self.assertEqual(self.list.remove(9), 9)
        self.assertEqual(self.list.len, 2)
        self.assertEqual(self.list.get(0), 7)

if __name__ == '__main__':
    unittest.main()
