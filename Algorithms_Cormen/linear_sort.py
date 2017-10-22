class LinearSort(object):
    @staticmethod
    def counting_sort(a):
        res = [0] * len(a)
        storage = [0] * (max(a)+1)
        
        for val in a:
            storage[val] += 1
            
        for i in range(1, len(storage)):
            storage[i] += storage[i-1]

        for val in a:
            res[storage[val]-1] = val
            storage[val] -= 1
            
        return res
    
    @staticmethod
    def radix_sort(a):
        return a
            
    
    
import random
import unittest

random.seed(42) # debug

TEST_RANGE = 10
TEST_SIZE = 20

class TestLinearSort(unittest.TestCase):
    def setUp(self):
        self.test = [random.randrange(TEST_RANGE) for _1 in range(TEST_SIZE)]
        print(self.test)
        self.expected = sorted(self.test)
        
    def tearDown(self):
        self.test = []
        self.expected = []
        
    def test_counting_sort(self):
        res = LinearSort.counting_sort(self.test)
        self.assertEqual(self.expected, res)
        
    def test_radix_sort(self):
        res = LinearSort.radix_sort(self.test)
        self.assertEqual(self.expected, res)
        
if __name__ == '__main__':
    unittest.main()