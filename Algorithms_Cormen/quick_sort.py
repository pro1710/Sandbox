import random

class QuickSort(object):
    class Partition(object):
        @staticmethod
        def simple(a, first, last):
            pivot = a[last]
            i = first - 1
            for j in range(first, last):
                if pivot > a[j]:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i + 1], a[last] = a[last], a[i + 1]
            return i + 1
        
        @staticmethod
        def randomized(a, first, last):
            i = random.randrange(last)
            a[i], a[last] = a[last], a[i]
            return QuickSort.Partition.simple(a, first, last)

        
    @staticmethod
    def sort(a, first=None, last=None, partition=Partition.simple):
        
        if first == None:
                first = 0
        if last == None:
                last = len(a) - 1
        
        if last > first:
            pivot_idx = partition(a, first, last)
            QuickSort.sort(a, first, pivot_idx-1)
            QuickSort.sort(a, pivot_idx+1, last)
    
    
# unit tests
import unittest

TEST_SIZE = 1000000
TEST_RANGE = 1000

class TestQuickSort(unittest.TestCase):
    
    def test_simple_partition(self):
        test = [random.randrange(TEST_SIZE) for _1 in range(TEST_RANGE)]
        #debug
        QuickSort.sort(test, partition=QuickSort.Partition.simple)
        expected = sorted(test)
        self.assertEqual(test, expected)
        
    def test_randomized_partition(self):
        test = [random.randrange(TEST_SIZE) for _1 in range(TEST_RANGE)]
        #debug
        QuickSort.sort(test, partition=QuickSort.Partition.randomized)
        expected = sorted(test)
        self.assertEqual(test, expected)
        
                      
if __name__ == '__main__':
    unittest.main()