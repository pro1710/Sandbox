class QuickSort(object):
    class Utils(object):
        @staticmethod
        def simple_partitioning(a, first, last):
            if last > first:
                pivot = a[last]
                i = first - 1
                for j in range(first, last):
                    if pivot > a[j]:
                        i += 1
                        a[i], a[j] = a[j], a[i]
                a[i + 1], a[last] = a[last], a[i + 1]
                return i + 1
            else:
                return 0
        
    @staticmethod
    def sort(a, first=None, last=None):
        
        if first == None:
                first = 0
        if last == None:
                last = len(a) - 1
        
        if last > first:
            pivot_idx = QuickSort.Utils.simple_partitioning(a, first, last)
            QuickSort.sort(a, first, pivot_idx-1)
            QuickSort.sort(a, pivot_idx+1, last)
    
    
# unit tests
import unittest
import random

class TestMaxPriorityQueue(unittest.TestCase):
    def test_sort_once(self):
        TEST_SIZE = 1000000
        TEST_RANGE = 1000
        test = [random.randrange(TEST_SIZE) for _1 in range(TEST_RANGE)]
        #debug
        QuickSort.sort(test)
        expected = sorted(test)
        self.assertEqual(test, expected)
        
                      
if __name__ == '__main__':
    unittest.main()