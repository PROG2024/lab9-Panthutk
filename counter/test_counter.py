"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    def test_initial_count(self):
        counter = Counter()
        self.assertEqual(counter.count, 0)  # initial count should be 0

    def test_increment(self):
        counter = Counter()
        counter.increment()
        self.assertEqual(counter.count, 1)  # should be 1

    def test_singleton(self):
        counter1 = Counter()
        counter2 = Counter()
        self.assertIs(counter1, counter2)  # same instance


if __name__ == "__main__":
    unittest.main()
