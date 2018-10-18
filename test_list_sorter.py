import unittest
import list_sorter



class TestListSorter(unittest.TestCase):

    def setUp(cls):
        cls.unsorted_list1 = [50,40,10,30,24]
        cls.unsorted_list2 = [50, -50, 50, 50, 40, 10, 30, 24]

        cls.sorted_list1 = [10,24,30,40,50]
        cls.sorted_list2 = [-50, 10, 24, 30, 40, 50, 50, 50]

        cls.size1 = len(cls.unsorted_list1)
        cls.size2 = len(cls.unsorted_list2)

    def test_bubble_sort(self):
        self.assertEqual(list_sorter.bubble_sort(self.unsorted_list1),
                         self.sorted_list1)

    def test_selection_sort(self):
        self.assertEqual(list_sorter.bubble_sort(self.unsorted_list2),
                         self.sorted_list2)

    def test_insertion_sort(self):
        self.assertEqual(list_sorter.insertion_sort(self.unsorted_list1),
                         self.unsorted_list1)
        
    def test_merge_sort(self):
        self.assertEqual(list_sorter.merge_sort(self.unsorted_list2),
                         self.sorted_list2)


if __name__ == "__main__":
    unittest.main()
