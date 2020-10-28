import unittest
from collections import defaultdict
import sys

class StatsList(list):
    def mean(self):
        return sum(self) / len(self)

    def median(self):
        if len(self) % 2:
            return self[len(self) / 2]
        else:
            idx = int(len(self) / 2)
            return (self[idx] + self[idx-1]) / 2
    
class TestValidInputs(unittest.TestCase):
    def setUp(self):
        self.stats = StatsList([1,2,2,3,3,4])

    def test_mean(self):
        self.assertEqual(self.stats.mean(), 2.5)

    @unittest.expectedFailure
    def test_median(self):
        self.assertEqual(self.stats.median(), 2)

    @unittest.skipUnless(sys.platform.startswith('linux'), 'Test is Useless')
    def test_fails(self):
        self.assertEqual(True, False)

if __name__ == "__main__":
    unittest.main()