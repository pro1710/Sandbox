infinity = float('inf')

class Heap(object):
    def __init__(self, lst: list=[]):
        self._lst = list(lst)
        self.size = 0
        self.build_max_heap()
    
    def __str__(self):
        return str(self._lst)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, key):
        return self._lst[key]
    
    def __setitem__(self, key, value):
        self._lst[key] = value
        
    def list(self):
        return self._lst
    
    def parrent(self, i):
        '''
        Returns parrent node for i-th child
        '''
        return i // 2

    def left(self, i):
        '''
          Returns left child-node for i-th root
        '''
        return 2 * i

    def right(self, i):
        '''
          Returns right child-node for i-th root
        '''
        return 2 * i + 1

class MaxHeap(Heap):
    
    def max_heapify(self, root_idx):
        '''
          Maintain the heap property for heap _lst
        '''

        left_child_idx = self.left(root_idx)
        right_child_idx = self.right(root_idx)

        largest_node_idx = root_idx

        if self.size > left_child_idx and self._lst[left_child_idx] > self._lst[root_idx]:
            largest_node_idx = left_child_idx

        if self.size > right_child_idx and self._lst[right_child_idx] > self._lst[largest_node_idx]:
            largest_node_idx = right_child_idx

        if largest_node_idx != root_idx:
            self._lst[root_idx], self._lst[largest_node_idx] = self._lst[largest_node_idx], self._lst[root_idx]
            self.max_heapify(largest_node_idx)

    def build_max_heap(self):
        '''
          Build max heap from list _lst
        '''
        self.size = len(self._lst)
        for i in reversed(range(self.size // 2)):
            self.max_heapify(i)
            
    
def heapsort(lst: list):
    '''
    Sort elemnts of _lst using heapsort algorithm
    '''
    h = MaxHeap(lst)
    for i in reversed(range(1, len(h))):
        h[0], h[i] = h[i], h[0]
        h.size -= 1
        h.max_heapify(0)
    return h.list()
            
     
class MaxPriorityQueue(MaxHeap):
    def maximum(self):
        return self._lst[0]
    
    def extract_max(self):
        assert self.size > 0, 'heap underflow'
        
        max_element = self.maximum()
        
        self._lst[0] = self._lst[-1] # assign 1st element to last element
        self.size -= 1
        del self._lst[-1] # remove last element
        self.max_heapify(0)
        
        return max_element
        
    def increase_key(self, i, key):
        assert key > self._lst[i], 'new key smaller than current key'
        
        self._lst[i] = key
        while i > 0 and self.parrent(i) < self._lst[i]:
            self._lst[i], self._lst[self.parrent(i)] = self._lst[self.parrent(i)], self._lst[i]
            i = self.parrent(i)
            
    def insert(self, key):
        self.size += 1
        self._lst.append(-infinity)
        self.increase_key(self.size - 1, key)
        
        

# unit tests
import unittest
import random

class TestHeapSort(unittest.TestCase):
    pass    

class TestMaxPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.lst = [0, 4, 5, 100, 1, 2, 3, 101, 102, 103]
        self.queue = MaxPriorityQueue(self.lst)
        
    def test_insert(self):
        self.queue.insert(42)
        self.lst.append(42)
        
        self.assertEqual(self.queue.size, len(self.lst))
        
    def test_maximum_1(self):
        self.assertEqual(self.queue.maximum(), max(self.lst))
        
    def test_extract_max(self):
        extracted = self.queue.extract_max()
        expected = max(self.lst)
        del self.lst[self.lst.index(max(self.lst))]
        
        print(expected, extracted)
        
        self.assertTrue(extracted == expected and self.queue.size == len(self.lst))
                      
if __name__ == '__main__':
    TESTS_NUMBER = 10
    TEST_SIZE = 100
    TEST_RANGE = 1000
    
    test_lists = [[random.randrange(TEST_SIZE) for _1 in range(TEST_RANGE)] for _2 in range(TESTS_NUMBER)]
    test_lists.append(list(range(TEST_SIZE))) # already sorted
    test_lists.append(list(reversed(range(TEST_SIZE)))) # reversed
    
    for i in range(len(test_lists)):
        testmethodname = 'test_fn_{0}'.format(i)
        testmethod = lambda self: self.assertEqual(sorted(test_lists[i]), heapsort(test_lists[i]))
        setattr(TestHeapSort, testmethodname, testmethod)
    unittest.main()



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  