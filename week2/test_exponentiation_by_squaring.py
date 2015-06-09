import unittest
from exponentiation_by_squaring import fast_exp


class TestFastExponentiation(unittest.TestCase):
    def test_fast_exp(self):
        self.assertEqual(fast_exp(2,1), 2)
        self.assertEqual(fast_exp(46363463, 0), 1)
        self.assertEqual(fast_exp(4, 16), 4294967296)
        self.assertEqual(fast_exp(16, 4), 65536)

if __name__ == "__main__":
    unittest.main()