import unittest
import bubble_sort as bs


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bs.bubble_sort([5, 7, 3]), [3, 5, 7])
        self.assertEqual(bs.bubble_sort([16, 235, 1, 25, 90, 1000, 0, 3, 15, 29]),
                         [0, 1, 3, 15, 16, 25, 29, 90, 235, 1000])
        self.assertEqual(bs.bubble_sort([0, 1]), [0, 1])
        self.assertEqual(bs.bubble_sort([5]), [5])
        self.assertEqual(bs.bubble_sort([]), [])
        self.assertEqual(bs.bubble_sort([0, -1]), [-1, 0])

if __name__ == "__main__":
    unittest.main()