class Heap(object):
    def __init__(self, lst: list):
        self._lst = lst
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
    
    def parrent(self):
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
      
    @staticmethod    
    def sort(lst: list):
        '''
        Sort elemnts of _lst using heapsort algorithm
        '''
        h = Heap(lst)
        for i in reversed(range(1, len(h))):
            h[0], h[i] = h[i], h[0]
            h.size -= 1
            h.max_heapify(0)
        return h.list()
            
        

# unit tests
import unittest
import random

class TestHeapSort(unittest.TestCase):
    pass    

def test():
    assert(1==1)
                      
if __name__ == '__main__':
    TESTS_NUMBER = 10
    TEST_SIZE = 10000
    TEST_RANGE = 1000
    
    test_lists = [[random.randrange(TEST_SIZE) for _1 in range(TEST_RANGE)] for _2 in range(TESTS_NUMBER)]
    test_lists.append(list(range(TEST_SIZE))) # already sorted
    test_lists.append(list(reversed(range(TEST_SIZE)))) # reversed
    
    for i in range(len(test_lists)):
        testmethodname = 'test_fn_{0}'.format(i)
        testmethod = lambda self: self.assertEqual(sorted(test_lists[i]), Heap.sort(test_lists[i]))
        setattr(TestHeapSort, testmethodname, testmethod)
    unittest.main()



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  