import unittest
import list_sorter


class TestListSorter(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(list_sorter.bubble_sort([50,50,50,50,40,10,30,24]),
                         [10,24,30,40,50,50,50,50])

    def test_selection_sort(self):
        self.assertEqual(list_sorter.bubble_sort([50, -50, 50, 50, 40, 10, 30, 24]),
                         [-50, 10, 24, 30, 40, 50, 50, 50])

    def test_insertion_sort(self):
        self.assertEqual(list_sorter.insertion_sort([4,3,17,44,31,51,26]),
                         [3,4,17,26,31,44,51])


if __name__ == "__main__":
    unittest.main()
