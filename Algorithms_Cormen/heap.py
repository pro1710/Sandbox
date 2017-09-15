class Heap(object):
  def __init__(self, A: list):
    self.A = A
    
  def __str__(self):
    return str(self.A)
    
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
      Maintain the heap property for heap A
    '''

    left_child_idx = self.left(root_idx)
    right_child_idx = self.right(root_idx)

    largest_node_idx = root_idx

    if len(self.A) > left_child_idx and self.A[left_child_idx] > self.A[root_idx]:
      largest_node_idx = left_child_idx

    if len(self.A) > right_child_idx and self.A[right_child_idx] > self.A[left_child_idx]:
      largest_node_idx = right_child_idx
      
    if largest_node_idx != root_idx:
      self.A[root_idx], self.A[largest_node_idx] = self.A[largest_node_idx], self.A[root_idx]
      self.max_heapify(largest_node_idx)

  def build_max_heap(self):
    '''
      Build max heap from list A
    '''
    for i in reversed(range(len(self.A) // 2)):
      self.max_heapify(i)



