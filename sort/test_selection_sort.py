import unittest
from selection_sort import sort


class SelectionSortTest(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(sort([2, 3, 1]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
