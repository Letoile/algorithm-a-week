import unittest
from tree_factorial import fact_tree


class TestFastExponentiation(unittest.TestCase):
    def test_fact_tree(self):
        self.assertEqual(fact_tree(0), 1)
        self.assertEqual(fact_tree(1), 1)
        self.assertEqual(fact_tree(2), 2)
        self.assertEqual(fact_tree(-235235), 0)
        self.assertEqual(fact_tree(10), 3628800)

if __name__ == "__main__":
    unittest.main()
